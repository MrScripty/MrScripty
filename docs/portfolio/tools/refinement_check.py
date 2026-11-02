#!/usr/bin/env python3
"""Exercise composition keys, current presentation structure, and real touch gestures."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import os
import threading,json,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'review';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{server.server_port}/';checks=[]
def check(name,value):
 checks.append({'check':name,'passed':bool(value)});assert value,name
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path=os.environ.get('PORTFOLIO_CHROMIUM','/usr/bin/chromium'),args=['--no-sandbox'])
  for name,w,h in [('desktop',1440,1050),('tablet',768,1024),('mobile',390,844),('narrow',320,800)]:
   page=browser.new_page(viewport={'width':w,'height':h},has_touch=w<=560,is_mobile=w<=560,reduced_motion='reduce');page.goto(url,wait_until='networkidle')
   check(name+' no status or scope widgets',page.locator('.pill,details.project-boundary,.primary-link').count()==0)
   check(name+' plain-language hero',page.locator('h1 .visually-hidden').inner_text()=='I build local AI systems you can inspect, trace, audit, compose and understand.' and page.locator('.verb-word[data-active]').inner_text()=='inspect.' and page.locator('.hero-focus').inner_text()=='Model systems, visual tools, data provenance, observability and local AI.')
   check(name+' project map links every project',all(page.locator(f'.graph a.node[href="#{i}"]').count()==1 for i in ['pumas','pantograph','chrema','tuldok','rheon-surrogate-lab','book-be-gone','eidetic','whip-docs','standards','phased-memory','passeur','lanternwake','rheon','kenoma']))
   check(name+' no image labels or captions',page.locator('.capture-heading,figcaption,#dialog-caption').count()==0)
   check(name+' no reserved image strip',all(f.evaluate('(e)=>{let r=e.getBoundingClientRect(),a=e.querySelector(".capture-button").getBoundingClientRect();return Math.abs(r.height-a.height-2)<1}') for f in page.locator('figure.app-capture:visible').all()))
   check(name+' single hero heading',page.locator('.hero h1').count()==1)
   check(name+' BC+AI and devLab biography','I’m a cofounder of BC+AI and founded its developer subgroup, devLab.' in page.locator('#about').inner_text())
   groups={'infrastructure':['pumas','pantograph','chrema'],'models':['rheon-surrogate-lab','tuldok'],'context':['eidetic','standards','phased-memory'],'agents':['whip-docs','passeur'],'research':['rheon','kenoma'],'applications':['book-be-gone','lanternwake']}
   check(name+' project grouping',all(page.locator(f'#{g} #{i}').count()==1 for g,ids in groups.items() for i in ids))
   check(name+' books separate',page.locator('#books .paired-book').count()==1 and page.locator('#context .paired-book').count()==0)
   check(name+' meaningful tags for 14 projects',page.locator('.capability-tags').count()==14)
   check(name+' no per-project language bars',page.locator('.language-profile,.language-bar').count()==0)
   check(name+' languages explained once',page.locator('#languages dt').all_text_contents()==['Rust','Python','TypeScript and JavaScript','C#','Lean'])
   for selector in ['header a[href="https://github.com/MrScripty"]','footer a[href="https://github.com/MrScripty"]','a[href="https://www.linkedin.com/in/jeremybayley"]']:
    link=page.locator(selector);check(name+' accessible brand link '+selector,link.is_visible() and link.inner_text() in ['GitHub','LinkedIn'] and link.locator('svg[aria-hidden="true"]').count()==1)
   for ident in [i for ids in groups.values() for i in ids]:
    head=page.locator(f'#{ident} > .project-head');status=head.locator('.status')
    check(name+' status in project header '+ident,head.locator('h3.project-title').count()==1 and status.count()==1 and status.get_attribute('data-level') in ('1','2','3') and status.inner_text().strip()!='')
    check(name+' project panel separated '+ident,page.locator('#'+ident).evaluate('(e)=>getComputedStyle(e).borderTopStyle')=='solid')
   wires=page.locator('.wires path').evaluate_all('(ps)=>ps.filter(p=>p.getAttribute("d")).length')
   check(name+' project map wires',wires==(4 if w>720 else 3))
   check(name+' fluid background static under reduced motion',page.locator('canvas.flow-field').count()==1)
   gallery=page.locator('#kenoma .capture-gallery');check(name+' arm image first',gallery.locator('figure').first.locator('img').get_attribute('src').startswith('assets/kenoma-held-anatomy-scene.png'))
   gallery=page.locator('#pantograph .capture-gallery');gallery.scroll_into_view_if_needed();page.locator('#pantograph h3').click();page.mouse.move(0,0)
   arrow=gallery.locator('button').last
   if w<=560:
    check(name+' touch arrows discoverable',arrow.evaluate('(e)=>getComputedStyle(e).opacity')=='1' and page.evaluate('navigator.maxTouchPoints>0 && document.documentElement.classList.contains("touch-input")'))
    cdp=page.context.new_cdp_session(page)
    def swipe(dx,dy):
     frame=gallery.locator('figure:not([hidden]) .capture-frame');frame.scroll_into_view_if_needed();box=frame.bounding_box();x=box['x']+box['width']/2-dx/2;y=box['y']+box['height']/2-dy/2
     cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
     for j in range(1,9):cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x+dx*j/8,'y':y+dy*j/8}]})
     cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    swipe(-100,0);check(name+' actual touch swipe left',gallery.locator('.gallery-status').inner_text()=='2 / 4');check(name+' swipe avoids enlargement',not page.locator('#image-dialog').evaluate('(d)=>d.open'))
    swipe(100,0);check(name+' actual touch swipe right',gallery.locator('.gallery-status').inner_text()=='1 / 4')
    swipe(0,60);check(name+' vertical touch preserves gallery',gallery.locator('.gallery-status').inner_text()=='1 / 4')
    gallery=page.locator('#book-be-gone .capture-gallery');swipe(-100,0);check(name+' Book-Be-Gone real touch swipe',gallery.locator('.gallery-status').inner_text()=='2 / 2' and not page.locator('#image-dialog').evaluate('(d)=>d.open'));swipe(100,0);check(name+' Book-Be-Gone touch returns',gallery.locator('.gallery-status').inner_text()=='1 / 2')
   else:
    check(name+' desktop arrows hidden at rest',arrow.evaluate('(e)=>getComputedStyle(e).opacity')=='0');arrow.focus();check(name+' keyboard reveals arrows',arrow.evaluate('(e)=>getComputedStyle(e).opacity')=='1')
   page.locator('footer').scroll_into_view_if_needed();page.screenshot(path=str(OUT/f'{name}-footer.png'))
   check(name+' no overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
   page.goto(url+'image-credits.html');check(name+' credits preserve licensors',all(t in page.locator('body').inner_text() for t in ['BodyParts3D','DBCLS','Arm26/OpenSim','CC BY 4.0','CC BY 3.0','Font Awesome']))
   check(name+' credits fit viewport',page.evaluate('document.documentElement.scrollWidth<=innerWidth'));page.close()
  browser.close()
 check('Book-Be-Gone scan original bytes',hashlib.sha256((ROOT/'assets/book-be-gone_scan.jpg').read_bytes()).hexdigest()=='5d8d069abc099c531abe5787a056d35b0dce2421f6cbce18cb24f489916aa971')
 check('Book-Be-Gone OCR original bytes',hashlib.sha256((ROOT/'assets/book-be-gone_ocr.jpg').read_bytes()).hexdigest()=='eaefc20b598d732f34f96b213f06e0720c2c19a415ecf950b68bf81215d2e05b')
 check('Lanternwake original bytes',hashlib.sha256((ROOT/'assets/Lanternwake_2026-10-07_13-43-35.jpg').read_bytes()).hexdigest()=='ab4fe6f43ae12109f3858fe66eb54868617efe86fcade84a7bb571c64e1dcbcc')
finally:
 server.shutdown();server.server_close();report={'checks':len(checks),'failures':[c for c in checks if not c['passed']]};(OUT/'refinement-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

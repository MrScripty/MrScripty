#!/usr/bin/env python3
"""Exercise composition keys, current presentation structure, and real touch gestures."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,json,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'review';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{server.server_port}/';checks=[]
def check(name,value):
 checks.append({'check':name,'passed':bool(value)});assert value,name
stats=json.loads((ROOT/'assets/language-stats.json').read_text())
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for name,w,h in [('desktop',1440,1050),('tablet',768,1024),('mobile',390,844),('narrow',320,800)]:
   page=browser.new_page(viewport={'width':w,'height':h},has_touch=w<=560,is_mobile=w<=560,reduced_motion='reduce');page.goto(url,wait_until='networkidle')
   check(name+' no status or scope widgets',page.locator('.pill,details.project-boundary,.primary-link').count()==0)
   check(name+' exact hero concepts',page.locator('.hero-signature span').all_text_contents()==['Local AI','Data provenance','Observability'])
   check(name+' context grouping',all(page.locator('#context #'+i).count()==1 for i in ['tuldok','eidetic','whip-docs','standards']))
   check(name+' books separate',page.locator('#books .paired-book').count()==1 and page.locator('#context .paired-book').count()==0)
   check(name+' meaningful tags for 11 projects',page.locator('.capability-tags').count()==11)
   check(name+' 12 independent composition bars',page.locator('.language-profile').count()==12)
   for selector in ['header a[href="https://github.com/MrScripty"]','footer a[href="https://github.com/MrScripty"]','a[href="https://www.linkedin.com/in/jeremybayley"]']:
    link=page.locator(selector);check(name+' accessible brand link '+selector,link.is_visible() and link.inner_text() in ['GitHub','LinkedIn'] and link.locator('svg[aria-hidden="true"]').count()==1)
   for repo in stats['repositories']:
    profile=page.locator(f'.language-profile[data-repository="{repo["repository"]}"]');segments=profile.locator('.language-bar>span')
    actual=segments.evaluate_all('(es)=>es.map(e=>({name:e.dataset.language,width:parseFloat(e.style.width),color:e.style.background}))')
    check(name+' measured proportions '+repo['repository'],len(actual)==len(repo['languages']) and all(a['name']==b['name'] and abs(a['width']-100*b['bytes']/repo['total_bytes'])<.0001 for a,b in zip(actual,repo['languages'])))
    button=profile.locator('button');button.focus();check(name+' keyboard language key '+repo['repository'],profile.locator('.language-key').is_visible());page.keyboard.press('Escape');check(name+' Escape key '+repo['repository'],not profile.locator('.language-key').is_visible())
   bar=page.locator('#rheon .language-profile').first;button=bar.locator('button')
   if w<=560:
    button.tap();check(name+' touch opens composition',bar.locator('.language-key').is_visible());button.tap();check(name+' touch closes composition',not bar.locator('.language-key').is_visible())
   else:
    page.locator('#rheon h3').click();button.hover();check(name+' hover composition',bar.locator('.language-key').is_visible());page.locator('#rheon h3').hover();check(name+' mouse leave closes composition',not bar.locator('.language-key').is_visible())
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
   else:
    check(name+' desktop arrows hidden at rest',arrow.evaluate('(e)=>getComputedStyle(e).opacity')=='0');arrow.focus();check(name+' keyboard reveals arrows',arrow.evaluate('(e)=>getComputedStyle(e).opacity')=='1')
   page.locator('footer').scroll_into_view_if_needed();page.screenshot(path=str(OUT/f'{name}-footer.png'))
   check(name+' no overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
   page.goto(url+'image-credits.html');check(name+' credits preserve licensors',all(t in page.locator('body').inner_text() for t in ['BodyParts3D','DBCLS','Arm26/OpenSim','CC BY 4.0','CC BY 3.0','Font Awesome']))
   check(name+' credits fit viewport',page.evaluate('document.documentElement.scrollWidth<=innerWidth'));page.close()
  browser.close()
 check('Lanternwake original bytes',hashlib.sha256((ROOT/'assets/Lanternwake_2026-10-07_13-43-35.jpg').read_bytes()).hexdigest()=='ab4fe6f43ae12109f3858fe66eb54868617efe86fcade84a7bb571c64e1dcbcc')
finally:
 server.shutdown();server.server_close();report={'checks':len(checks),'failures':[c for c in checks if not c['passed']]};(OUT/'refinement-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

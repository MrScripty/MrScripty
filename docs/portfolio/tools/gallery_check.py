#!/usr/bin/env python3
"""Exercise manual gallery navigation, original images, history and typography."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'review';OUT.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/';checks=[]
def check(name,result):
    checks.append({'check':name,'passed':bool(result)});assert result,name
def selected(gallery):return gallery.locator('figure:not([hidden])')
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        for name,w,h in [('desktop',1440,1050),('tablet',768,1024),('mobile',390,844),('narrow',320,800)]:
            page=browser.new_page(viewport={'width':w,'height':h},reduced_motion='reduce');errors=[]
            page.on('pageerror',lambda e:errors.append(str(e)));page.goto(url,wait_until='networkidle')
            styles=page.locator('.project-deck').evaluate_all('(xs)=>xs.map(e=>{let s=getComputedStyle(e);return [s.fontFamily,s.fontSize,s.fontWeight,s.fontStyle,s.lineHeight,s.color]})')
            check(name+' ten matching white taglines',len(styles)==10 and all(s==styles[0] and s[-1]=='rgb(255, 255, 255)' for s in styles))
            styles=page.locator('h3.project-title').evaluate_all('(xs)=>xs.map(e=>{let s=getComputedStyle(e);return [s.fontFamily,s.fontSize,s.fontWeight,s.color]})')
            check(name+' matching project names',len(styles)==10 and all(s==styles[0] for s in styles))
            check(name+' dark theme',page.locator('#work').evaluate('(e)=>getComputedStyle(e).backgroundColor')=='rgb(18, 28, 23)')
            books=page.locator('#books').bounding_box();lantern=page.locator('#lanternwake').bounding_box()
            check(name+' Lanternwake below books',lantern['y']>=books['y']+books['height'])
            check(name+' no fabricated Lanternwake image',page.locator('#lanternwake img').count()==0)
            a=page.locator('#tuldok').bounding_box();b=page.locator('#eidetic').bounding_box();check(name+' stacked apps',b['y']>=a['y']+a['height'])
            if name in ['desktop','mobile']:
                for id in ['pumas','pantograph','chrema','tuldok','eidetic','whip-docs','rheon','kenoma','standards','lanternwake']:
                    card=page.locator('#'+id)
                    for img in card.locator('img:visible').all():img.evaluate('(i)=>i.decode()')
                    card.screenshot(path=str(OUT/f'{name}-{id}.png'))
            for gallery in page.locator('.capture-gallery').all():
                label=name+' '+gallery.get_attribute('data-gallery');count=gallery.locator(':scope > figure').count()
                prev=gallery.locator('.gallery-controls button').first;next=gallery.locator('.gallery-controls button').last
                for index in range(count):
                    check(label+' one visible',selected(gallery).count()==1)
                    check(label+' count',gallery.locator('.gallery-status').inner_text()==f'{index+1} / {count}')
                    active=selected(gallery);img=active.locator('img');img.evaluate('(i)=>i.decode()')
                    check(label+' image proportions',img.evaluate('(i)=>Math.abs(i.getBoundingClientRect().width/i.getBoundingClientRect().height-i.naturalWidth/i.naturalHeight)<.002'))
                    check(label+' no reserved image height',active.locator('.capture-button').evaluate('(a)=>Math.abs(a.getBoundingClientRect().height-a.querySelector("img").getBoundingClientRect().height)<1'))
                    if name in ['desktop','mobile'] and gallery.get_attribute('data-gallery')=='Rheon' and index==1:
                        page.locator('#rheon').screenshot(path=str(OUT/f'{name}-rheon-lab.png'))
                    link=active.locator('.capture-button');expected=active.locator('figcaption').inner_text().strip()
                    link.click();page.wait_for_selector('#image-dialog[open]');page.locator('#dialog-image').evaluate('(i)=>i.decode()')
                    check(label+' full original and caption',page.locator('#dialog-image').get_attribute('src').endswith(link.get_attribute('href')) and ' '.join(page.locator('#dialog-caption').inner_text().split())==' '.join(expected.split()))
                    page.keyboard.press('Escape');page.wait_for_function('!document.querySelector("#image-dialog").open && !history.state?.portfolioCapture');page.wait_for_function('(a)=>a===document.activeElement',arg=link.element_handle())
                    y=gallery.locator('.gallery-controls').evaluate('(e)=>e.getBoundingClientRect().top-e.parentElement.getBoundingClientRect().top')
                    next.click();check(label+' stable controls',abs(gallery.locator('.gallery-controls').evaluate('(e)=>e.getBoundingClientRect().top-e.parentElement.getBoundingClientRect().top')-y)<1)
                next.evaluate('(b)=>{for(let i=0;i<9;i++)b.click()}');check(label+' repeated clicks',gallery.locator('.gallery-status').inner_text()==f'{9%count+1} / {count}')
                next.focus();page.keyboard.press('End');check(label+' End',gallery.locator('.gallery-status').inner_text()==f'{count} / {count}')
                page.keyboard.press('Home');page.keyboard.press('ArrowLeft');check(label+' keyboard wrap',gallery.locator('.gallery-status').inner_text()==f'{count} / {count}')
                page.keyboard.press('ArrowRight');check(label+' keyboard next',gallery.locator('.gallery-status').inner_text()==f'1 / {count}')
                selected(gallery).locator('.capture-button').focus();page.keyboard.press('ArrowRight')
                check(label+' capture focus follows',selected(gallery).locator('.capture-button').evaluate('(e)=>e===document.activeElement'))
                check(label+' reduced motion',gallery.evaluate('(g)=>g.getAnimations({subtree:true}).length===0'))
                link=selected(gallery).locator('.capture-button');href=link.get_attribute('href');link.click();page.wait_for_selector('#image-dialog[open]')
                page.go_back();page.wait_for_function('!document.querySelector("#image-dialog").open')
                next.click();page.go_forward();page.wait_for_selector('#image-dialog[open]')
                check(label+' history reveals original',selected(gallery).locator('.capture-button').get_attribute('href')==href)
                page.locator('.dialog-close').click();page.wait_for_function('!document.querySelector("#image-dialog").open && !history.state?.portfolioCapture')
                page.wait_for_function('(a)=>a===document.activeElement',arg=link.element_handle())
                prev.focus();page.keyboard.press('Home')
            check(name+' no overflow or errors',not errors and page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
            page.close()
        page=browser.new_page(viewport={'width':390,'height':844},java_script_enabled=False);page.goto(url)
        check('no JS all 13 image links visible',page.locator('.capture-button:visible').count()==13)
        check('no JS no inert controls',page.locator('.gallery-controls').count()==0);page.close()
        page=browser.new_page(viewport={'width':390,'height':844},reduced_motion='no-preference');page.goto(url)
        gallery=page.locator('#rheon .capture-gallery');gallery.locator('button').last.evaluate('(b)=>b.click()')
        check('short normal-motion fade',gallery.evaluate('(g)=>g.getAnimations({subtree:true}).some(a=>a.effect.getTiming().duration===150)'))
        page.wait_for_function('document.querySelector("#rheon .capture-gallery").getAnimations({subtree:true}).length===0')
        check('Rheon lab distinct title and caption',selected(gallery).locator('.capture-heading b').inner_text()=='Rheon Surrogate Lab' and 'seed-900' in selected(gallery).locator('figcaption').inner_text())
        page.close();browser.close()
finally:
    server.shutdown();server.server_close()
    report={'checks':len(checks),'failures':[c for c in checks if not c['passed']]}
    (OUT/'gallery-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

#!/usr/bin/env python3
"""Local QA only; requires an already installed Playwright and Chromium."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import threading,json
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'review').mkdir(exist_ok=True)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
url=f'http://127.0.0.1:{server.server_port}/'
report={'url':url,'pages':[]}; failures=[]
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  for name,width,height in [('desktop',1440,1050),('tablet',768,1024),('mobile',390,844),('narrow',320,800)]:
   page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1,reduced_motion='reduce',has_touch=width<=560,is_mobile=width<=560)
   errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
   response=page.goto(url,wait_until='networkidle')
   for img in page.locator('img[src]:visible').all():
    img.scroll_into_view_if_needed();img.evaluate('(i)=>i.decode()')
   page.evaluate('window.scrollTo(0,0)');page.screenshot(path=str(ROOT/f'review/{name}-full.png'),full_page=True)
   if name=='desktop':page.screenshot(path=str(ROOT/'review/desktop-first-screen.png'))
   if name=='mobile':page.screenshot(path=str(ROOT/'review/mobile-first-screen.png'))
   overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
   broken=page.locator('img[src]').evaluate_all('(images) => images.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.src)')
   blank_links=page.locator('a').evaluate_all('(links) => links.filter(a => !(a.textContent||"").trim() && !a.getAttribute("aria-label")).map(a => a.outerHTML)')
   page.goto(url,wait_until='networkidle');page.keyboard.press('Tab');skip=page.locator('.skip-link').evaluate('(e) => e === document.activeElement');page.keyboard.press('Enter'); skip_target=page.evaluate('location.hash === "#main"')
   screenshot_tests=[]
   for link in page.locator('a.capture-button').all():
    if not link.is_visible():
     gallery=link.locator('xpath=ancestor::div[contains(concat(" ",normalize-space(@class)," ")," capture-gallery ")]')
     for _ in range(gallery.locator('figure').count()):
      gallery.locator('.gallery-controls button').last.click()
      if link.is_visible():break
    link.click();page.wait_for_selector('#image-dialog[open]');page.locator('#dialog-image').evaluate('(i)=>i.decode()');opened=page.locator('#dialog-image').evaluate('(i)=>i.complete&&i.naturalWidth>0');page.keyboard.press('Escape');page.wait_for_function('!document.querySelector("#image-dialog").open && !history.state?.portfolioCapture');page.wait_for_function('(a)=>a===document.activeElement',arg=link.element_handle());closed=page.locator('#image-dialog').evaluate('(d)=>!d.open');focus_restored=link.evaluate('(a)=>a===document.activeElement');screenshot_tests.append({'opened':opened,'escape_closed':closed,'focus_restored':focus_restored})
   result={'viewport':name,'http_status':response.status,'horizontal_overflow':overflow,'broken_images':broken,'blank_links':blank_links,'js_errors':errors,'skip_link_focused':skip,'skip_link_target':skip_target,'screenshot_dialogs':screenshot_tests}
   report['pages'].append(result)
   if response.status!=200 or overflow or broken or blank_links or errors or not skip or not skip_target or any(not all(t.values()) for t in screenshot_tests):failures.append(name)
   page.close()
  page=browser.new_page(viewport={'width':390,'height':844},java_script_enabled=False)
  page.goto(url);report['no_javascript']={'main_visible':page.locator('h1').is_visible(),'source_links':page.locator('a[href^="https://github.com/"]').count(),'body_scroll_width':page.evaluate('document.body.scrollWidth')};page.close();browser.close()
finally: server.shutdown();server.server_close()
report['failed_viewports']=failures
(ROOT/'review/qa-results.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));raise SystemExit(bool(failures))

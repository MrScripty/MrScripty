#!/usr/bin/env python3
"""Static checks for the buildless portfolio; uses Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from collections import Counter
import json,hashlib
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.refs=[]; self.images=[]; self.headings=[]; self.scripts=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if attrs.get('id'): self.ids.append(attrs['id'])
        if tag in ('h1','h2','h3'): self.headings.append(tag)
        for attr in ('src','href'):
            if attrs.get(attr): self.refs.append((tag,attrs[attr]))
        if tag=='img': self.images.append(attrs)
        if tag=='script': self.scripts.append(attrs)
p=Page();p.feed((ROOT/'index.html').read_text());errors=[]
for name,n in Counter(p.ids).items():
    if n>1: errors.append(f'Duplicate ID: {name}')
for tag,ref in p.refs:
    u=urlparse(ref)
    if u.scheme:
        if tag != 'a' and tag != 'link': errors.append(f'Unexpected external resource: {ref}')
        if u.scheme not in ('https',): errors.append(f'Unexpected URL scheme: {ref}')
    elif u.path:
        if not (ROOT/u.path).is_file(): errors.append(f'Missing local asset: {ref}')
    elif u.fragment and u.fragment not in p.ids: errors.append(f'Missing fragment: {ref}')
for img in p.images:
    if 'alt' not in img: errors.append('Image lacks alt')
if p.headings.count('h1')!=1: errors.append('Page must have exactly one h1')
if not (ROOT/'.nojekyll').exists(): errors.append('Missing .nojekyll')
for asset in ('styles.css','script.js'):
    source=ROOT/asset
    stem,ext=asset.rsplit('.',1)
    versioned=f'{stem}.{hashlib.sha256(source.read_bytes()).hexdigest()[:12]}.{ext}'
    if not (ROOT/versioned).is_file() or (ROOT/versioned).read_bytes()!=source.read_bytes(): errors.append(f'Stale or missing versioned asset: {versioned}; run tools/version_assets.py')
    if versioned not in [ref for _,ref in p.refs]: errors.append(f'HTML must reference versioned asset: {versioned}')
report={'static_errors':errors,'ids':len(p.ids),'links_and_assets':len(p.refs),'images':len(p.images),'h1_count':p.headings.count('h1'),'external_scripts':sum(bool(urlparse(s.get('src','')).scheme) for s in p.scripts)}
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))

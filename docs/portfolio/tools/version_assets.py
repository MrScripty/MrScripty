#!/usr/bin/env python3
"""Refresh content-versioned CSS/JS links after editing canonical assets."""
from pathlib import Path
import hashlib,re
ROOT=Path(__file__).resolve().parents[1]
page=ROOT/'index.html';html=page.read_text()
for asset in ('styles.css','script.js'):
    data=(ROOT/asset).read_bytes();stem,ext=asset.rsplit('.',1)
    name=f'{stem}.{hashlib.sha256(data).hexdigest()[:12]}.{ext}'
    (ROOT/name).write_bytes(data)
    html,count=re.subn(r'"'+stem+r'(?:\.[0-9a-f]{12})?\.'+ext+r'"',lambda _: '"'+name+'"',html)
    if count!=1:raise SystemExit(f'Expected exactly one {asset} reference; found {count}')
page.write_text(html)

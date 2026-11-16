#!/usr/bin/env python3
"""Bygger listor/index.json av alla .txt-filer i listor/.
Första raden "# Namn" blir listans namn. Körs automatiskt av GitHub Actions."""
import json, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent / 'listor'
out = []
for f in sorted(root.glob('*.txt')):
    lines = f.read_text(encoding='utf-8-sig').splitlines()
    name = f.stem
    if lines and lines[0].strip().startswith('#'):
        name = lines[0].strip().lstrip('#').strip() or f.stem
    count = sum(1 for l in lines if l.strip() and not l.strip().startswith('#') and re.search(r'\t|[;=:,]|\s[-–—]\s', l))
    out.append({'id': f.stem, 'namn': name, 'antal': count})
(root / 'index.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(out)} listor')

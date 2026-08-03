#!/usr/bin/env python3
"""Offline render check that preserves CSS cascade order.

The earlier version of this harness inlined only the page's <style> blocks and
dropped every <link rel=stylesheet>. That silently removed the theme
stylesheet — which is exactly where the rules that were overriding mine lived —
so the check reported black when the live site was white. Anything that reads
computed styles has to reproduce document order across BOTH kinds of source.
"""
import re, subprocess, sys, urllib.parse

URL = sys.argv[1] if len(sys.argv) > 1 else "https://omarscontainers.de/"
OUT = sys.argv[2] if len(sys.argv) > 2 else "render.html"

html = subprocess.run(["curl", "-sS", URL], capture_output=True, text=True,
                      check=True).stdout

head = html[:html.find("</head>")]
# walk <style> and <link rel=stylesheet> in the order they appear
parts = []
for m in re.finditer(
        r'<style[^>]*>(.*?)</style>|<link[^>]+rel=[\'"]stylesheet[\'"][^>]*>',
        head, re.S):
    if m.group(1) is not None:
        parts.append(m.group(1))
    else:
        href = re.search(r'href=[\'"]([^\'"]+)[\'"]', m.group(0))
        if not href:
            continue
        u = urllib.parse.urljoin(URL, href.group(1))
        r = subprocess.run(["curl", "-sS", u], capture_output=True, text=True)
        parts.append(f"/* ---- {u} ---- */\n" + r.stdout)

i = html.find("<header")
header = html[i:html.find("</header>") + 9] if i > 0 else ""

open(OUT, "w", encoding="utf-8").write(
    '<!doctype html><html lang="de"><head><meta charset="utf-8">\n'
    + "\n".join(f"<style>{p}</style>" for p in parts)
    + '\n<style>body{margin:0}</style></head>'
    + f'<body class="wp-site-blocks hostinger-ai-woocommerce-active">{header}</body></html>')
print(f"{OUT}: {len(parts)} css sources, header {len(header)} bytes")

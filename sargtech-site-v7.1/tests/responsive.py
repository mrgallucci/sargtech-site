"""Teste responsivo: screenshots e checagem de overflow lateral em 6 larguras."""
import subprocess, time, json, os, sys
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "screenshots"); os.makedirs(OUT, exist_ok=True)
srv = subprocess.Popen([sys.executable, "-m", "http.server", "5599", "-d", os.path.join(ROOT, "dist")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
SIZES = {"360": (360, 740), "390": (390, 844), "430": (430, 932), "tablet-768": (768, 1024), "notebook-1366": (1366, 768), "desktop-1920": (1920, 1080)}
PAGES = {"home": "/", "gestao-inteligente": "/gestao-inteligente/", "sarglab": "/sarglab/", "ebook": "/sarglab/ebook/", "cursos": "/sarglab/cursos/", "contato": "/contato/", "privacidade": "/privacidade/", "termos": "/termos/"}
res = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for sn, (w, h) in SIZES.items():
        pg = b.new_page(viewport={"width": w, "height": h})
        for name, path in PAGES.items():
            pg.goto("http://localhost:5599" + path); pg.wait_for_timeout(300)
            over = pg.evaluate("document.documentElement.scrollWidth - window.innerWidth")
            wide = pg.evaluate("""[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>window.innerWidth+1&&getComputedStyle(e).position!=='absolute'}).slice(0,3).map(e=>e.tagName+'.'+e.className)""")
            res.append((sn, name, over, wide))
            if name in ("home", "ebook", "cursos") or sn in ("360",):
                pg.screenshot(path=f"{OUT}/{name}-{sn}.png", full_page=True)
        pg.close()
    b.close()
srv.terminate()
bad = [r for r in res if r[2] > 0 or r[3]]
print("checagens:", len(res), "com problema:", len(bad))
for r in bad: print(r)

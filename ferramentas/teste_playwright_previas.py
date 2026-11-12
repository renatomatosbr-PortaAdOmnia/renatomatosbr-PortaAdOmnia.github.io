import pathlib
from playwright.sync_api import sync_playwright
PNG=bytes.fromhex("89504e470d0a1a0a0000000d4948445200000001000000010806000000" "1f15c4890000000d49444154789c63f8cfc0f01f0005000201a5b4d1a90000000049454e44ae426082")
def rota(r):
    u=r.request.url
    if "unsplash" in u: return r.fulfill(body=PNG,content_type="image/png")
    if u.startswith("file:"): return r.continue_()
    return r.abort()
err=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for slug in ["studio-caroline-gomes-lash","brenda-alves-cilios"]:
        for nome,vp in [("d",{"width":1366,"height":860}),("m",{"width":390,"height":844})]:
            pg=b.new_page(viewport=vp); pg.on("pageerror",lambda e:err.append(str(e))); pg.route("**/*",rota)
            pg.goto(pathlib.Path(f"/home/claude/renatomatosbr-portaadomnia.github.io/{slug}/index.html").as_uri()); pg.wait_for_timeout(1200)
            pg.screenshot(path=f"{slug}-{nome}.png",full_page=(nome=="m"))
            pg.close()
    b.close()
print("erros:",err)

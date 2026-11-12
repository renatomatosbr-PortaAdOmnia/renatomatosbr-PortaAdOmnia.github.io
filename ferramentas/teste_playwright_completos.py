import pathlib
from playwright.sync_api import sync_playwright
LIB="/tmp/pwlibs/node_modules/"
MAP={"gsap.min.js":LIB+"gsap/dist/gsap.min.js","ScrollTrigger.min.js":LIB+"gsap/dist/ScrollTrigger.min.js","lenis.min.js":LIB+"lenis/dist/lenis.min.js"}
PNG=bytes.fromhex("89504e470d0a1a0a0000000d4948445200000001000000010806000000" "1f15c4890000000d49444154789c63f8cfc0f01f0005000201a5b4d1a90000000049454e44ae426082")
def rota(r):
    u=r.request.url
    for k,v in MAP.items():
        if u.endswith(k): return r.fulfill(path=v,content_type="application/javascript")
    if "unsplash" in u: return r.fulfill(body=PNG,content_type="image/png")
    if u.startswith("file:"): return r.continue_()
    return r.abort()
err=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for slug in ["exemplo-pet","exemplo-beleza"]:
        url=pathlib.Path(f"/home/claude/renatomatosbr-portaadomnia.github.io/{slug}/index.html").as_uri()
        for nome,vp in [("d",{"width":1366,"height":860}),("m",{"width":390,"height":844})]:
            pg=b.new_page(viewport=vp); pg.on("pageerror",lambda e,s=slug:err.append(f"{s}: {e}")); pg.route("**/*",rota)
            pg.goto(url); pg.wait_for_timeout(2500)
            pg.screenshot(path=f"{slug}-{nome}-topo.png")
            if nome=="d":
                pg.locator("[data-montar]").first.click(); pg.wait_for_timeout(1200)
                pg.locator("form .opcao:has([type=radio]) span").nth(1).click()
                pg.locator("form .opcao:has([type=checkbox]) span").first.click()
                pg.fill("#m-data","2026-11-20")
                if pg.locator("#m-bairro").count(): pg.fill("#m-bairro","Cambuí")
                pg.wait_for_timeout(700)
                pg.locator("#monte").screenshot(path=f"{slug}-montador.png")
                print(slug,"RESUMO:",pg.inner_text(".resumo").replace("\n"," | ")[:400])
                pg.click("[data-enviar-monta]"); pg.wait_for_timeout(500)
                print(slug,"MSG:\n",pg.inner_text("[data-balao]"))
                pg.click(".janela__botoes [data-fecha-janela]")
                pg.click("[data-add-monta]"); pg.wait_for_timeout(1200)
                pg.click("[data-plano-add]"); pg.wait_for_timeout(800)
                print(slug,"PLANO:",pg.inner_text(".calc__resultado").replace("\n"," "))
                pg.click("[data-enviar-pedido]"); pg.wait_for_timeout(500)
                print(slug,"AGENDA:\n",pg.inner_text("[data-balao]"))
            pg.close()
    b.close()
print("ERROS:",err)

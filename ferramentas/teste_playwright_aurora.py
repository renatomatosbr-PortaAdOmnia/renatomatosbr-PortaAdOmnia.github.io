import sys, pathlib
from playwright.sync_api import sync_playwright
SITE = pathlib.Path("/home/claude/renatomatosbr-portaadomnia.github.io/exemplo-confeitaria/index.html").as_uri()
LIB = "/tmp/pwlibs/node_modules/"
MAP = {"gsap.min.js": LIB+"gsap/dist/gsap.min.js", "ScrollTrigger.min.js": LIB+"gsap/dist/ScrollTrigger.min.js", "lenis.min.js": LIB+"lenis/dist/lenis.min.js"}
# imagem cinza no lugar das fotos
PNG = bytes.fromhex("89504e470d0a1a0a0000000d4948445200000001000000010806000000" "1f15c4890000000d49444154789c63f8cfc0f01f0005000201a5b4d1a90000000049454e44ae426082")
def rota(route):
    u = route.request.url
    for k,v in MAP.items():
        if u.endswith(k): return route.fulfill(path=v, content_type="application/javascript")
    if "unsplash" in u: return route.fulfill(body=PNG, content_type="image/png")
    if u.startswith("file:"): return route.continue_()
    return route.abort()
erros=[]
with sync_playwright() as p:
    b = p.chromium.launch()
    for nome, vp in [("desk", {"width":1366,"height":860}), ("cel", {"width":390,"height":844})]:
        pg = b.new_page(viewport=vp, device_scale_factor=1)
        pg.on("console", lambda m: m.type in ("error","warning") and erros.append(f"{nome}: {m.text}"))
        pg.on("pageerror", lambda e: erros.append(f"{nome} PAGEERROR: {e}"))
        pg.route("**/*", rota)
        pg.goto(SITE); pg.wait_for_timeout(2500)
        pg.screenshot(path=f"/home/claude/teste/{nome}-topo.png")
        # rolar a página inteira em pedaços
        h = pg.evaluate("document.body.scrollHeight"); y=0; i=0
        while y < h and i < 14:
            pg.mouse.wheel(0, vp["height"]*0.9); pg.wait_for_timeout(700); y += vp["height"]*0.9; i+=1
            pg.screenshot(path=f"/home/claude/teste/{nome}-{i:02d}.png")
        if nome=="desk":
            pg.evaluate("window.scrollTo(0,0)")
            pg.click("[data-filtro=docinhos]"); pg.wait_for_timeout(600)
            pg.click("[data-add=gourmet]"); pg.wait_for_timeout(300)
            pg.click("[data-pq=gourmet][data-d='1']")
            print("contador:", pg.inner_text("[data-contador]"))
            pg.click("[data-filtro=festa]"); pg.wait_for_timeout(500)
            pg.click("[data-montar=personalizado]"); pg.wait_for_timeout(1500)
            pg.fill("#bairro","Cambuí"); pg.fill("#data","2026-12-19"); pg.wait_for_timeout(700)
            print("resumo:", pg.inner_text(".resumo")[:600])
            pg.screenshot(path="/home/claude/teste/desk-montador.png")
            pg.click("[data-enviar-bolo]"); pg.wait_for_timeout(600)
            print("BALAO BOLO:\n", pg.inner_text("[data-balao]"))
            pg.screenshot(path="/home/claude/teste/desk-janela.png")
            pg.click(".janela__botoes [data-fecha-janela]"); pg.wait_for_timeout(300)
            pg.click("[data-add-bolo]"); pg.wait_for_timeout(1500)
            pg.click("[data-calc-add]"); pg.wait_for_timeout(800)
            pg.fill("#p-nome","Renato"); pg.wait_for_timeout(200)
            pg.screenshot(path="/home/claude/teste/desk-gaveta.png")
            pg.click("[data-enviar-pedido]"); pg.wait_for_timeout(600)
            print("BALAO PEDIDO:\n", pg.inner_text("[data-balao]"))
            pg.fill("#busca-bairro","barao geraldo")
            print("busca:", pg.inner_text("[data-busca-res]"))
            print("status:", pg.inner_text("[data-status-texto]"))
        pg.close()
    b.close()
print("ERROS:", *erros, sep="\n")

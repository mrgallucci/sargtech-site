"""Teste do front-end: payload enviado à API (interceptada), UTMs, persistência entre páginas, falha de rede."""
import subprocess, sys, time, os, json
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srv = subprocess.Popen([sys.executable, "-m", "http.server", "5598", "-d", os.path.join(ROOT, "dist")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1); got = []; mode = {"status": 200}
def handler(route):
    req = route.request
    if req.method == "OPTIONS":
        return route.fulfill(status=204, headers={"access-control-allow-origin": "*", "access-control-allow-headers": "content-type", "access-control-allow-methods": "POST"})
    got.append((req.url, json.loads(req.post_data)))
    route.fulfill(status=mode["status"], headers={"access-control-allow-origin": "*"}, body="{}")
ok = True
def check(c, m):
    global ok; print(("OK   " if c else "FALHA"), m); ok = ok and c
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.route("https://api.sargtech.com.br/**", handler)
    pg.goto("http://localhost:5598/sarglab/ebook/?utm_source=instagram&utm_medium=bio&utm_campaign=ebook-out&utm_content=post1&utm_term=ia")
    pg.fill("[name=nome]", "Ana Teste"); pg.fill("[name=email]", "ana@teste.com"); pg.fill("[name=whatsapp]", "(24) 99999-0000")
    pg.select_option("[name=area_profissional]", "vendas"); pg.check("[name=consentimento]"); pg.click("button[type=submit]")
    pg.wait_for_selector(".status.ok")
    url, d = got[-1]
    check(url == "https://api.sargtech.com.br/api/public/leads/ebook", "e-book vai para o endpoint configurado")
    check(all(d.get(k) for k in ["nome", "email", "area_profissional", "whatsapp"]) and d["whatsapp"] == "+5524999990000", "nome, e-mail, WhatsApp normalizado e área preservados")
    check(d["consentimento"] is True and d["origem"] == "instagram" and d["area_profissional"] == "vendas", "consentimento e origem enviados")
    check((d["utm_source"], d["utm_medium"], d["utm_campaign"], d["utm_content"], d["utm_term"]) == ("instagram", "bio", "ebook-out", "post1", "ia"), "cinco utm_* capturados")
    check(d["landing_url"].endswith("utm_term=ia") and "referrer" in d, "landing_url e referrer enviados")
    check(pg.locator("[data-download]").count() == 0 and "e-mail" in pg.inner_text(".status").lower(), "e-book não é liberado no site; acesso segue por e-mail")
    pg.goto("http://localhost:5598/contato/")
    pg.fill("[name=nome]", "Caio"); pg.fill("[name=email]", "caio@empresa.com"); pg.select_option("[name=assunto]", "CRM e gestão comercial")
    pg.fill("[name=mensagem]", "Quero organizar o funil comercial."); pg.check("[name=consentimento]"); pg.click("button[type=submit]")
    pg.wait_for_selector(".status.ok"); url, d = got[-1]
    check(url == "https://api.sargtech.com.br/api/public/leads/contact" and d["origem"] == "site-contato", "contato usa endpoint próprio")
    check(d["utm_source"] == "instagram", "UTMs persistem entre páginas da visita")
    # e-book sem UTM e sem referrer: origem "direto"; 409 (lead já existente) não bloqueia o download
    ctx2 = b.new_context(); p2 = ctx2.new_page(); p2.route("https://api.sargtech.com.br/**", handler)
    mode["status"] = 409; got.clear(); p2.goto("http://localhost:5598/sarglab/ebook/")
    p2.fill("[name=nome]", "Eva"); p2.fill("[name=email]", "EVA@Teste.com"); p2.fill("[name=whatsapp]", "(24) 98888-7777"); p2.select_option("[name=area_profissional]", "rh"); p2.check("[name=consentimento]"); p2.click("button[type=submit]")
    p2.wait_for_selector(".status.ok"); d = got[-1][1]
    check(d["origem"] == "direto" and d["email"] == "eva@teste.com" and d["whatsapp"] == "+5524988887777", "sem UTM: origem direto, e-mail minúsculo e WhatsApp normalizado")
    check(p2.locator("[data-download]").count() == 0 and "e-mail" in p2.inner_text(".status").lower(), "lead existente também recebe orientação de acesso por e-mail")
    # WhatsApp ausente ou inválido: navegador/JS bloqueia antes de chamar a API
    mode["status"] = 200; got.clear(); p2.goto("http://localhost:5598/sarglab/ebook/")
    p2.fill("[name=nome]", "Sem Telefone"); p2.fill("[name=email]", "semfone@teste.com"); p2.select_option("[name=area_profissional]", "rh"); p2.check("[name=consentimento]")
    p2.click("button[type=submit]"); time.sleep(.2)
    check(len(got) == 0, "WhatsApp obrigatório bloqueia envio vazio")
    p2.fill("[name=whatsapp]", "(24) 1234-5678"); p2.click("button[type=submit]")
    p2.wait_for_selector(".status.err")
    check(len(got) == 0 and "WhatsApp" in p2.inner_text(".status"), "WhatsApp inválido é rejeitado no front-end")
    # E-mail com @ mas sem domínio completo (ex.: emailemail@email) também não pode virar Lead
    got.clear(); p2.goto("http://localhost:5598/sarglab/ebook/")
    p2.fill("[name=nome]", "Email Invalido"); p2.fill("[name=email]", "emailemail@email"); p2.fill("[name=whatsapp]", "(24) 99999-0000")
    p2.select_option("[name=area_profissional]", "rh"); p2.check("[name=consentimento]"); p2.click("button[type=submit]"); time.sleep(.2)
    check(len(got) == 0, "e-mail sem domínio completo é bloqueado antes da API")
    mode["status"] = 200
    got.clear(); pg.goto("http://localhost:5598/contato/")
    pg.evaluate("document.querySelector('[name=website]').value='spam'")
    pg.fill("[name=nome]", "Bot"); pg.fill("[name=email]", "b@b.com"); pg.select_option("[name=assunto]", "Outro assunto"); pg.fill("[name=mensagem]", "mensagem de teste aqui"); pg.check("[name=consentimento]"); pg.click("button[type=submit]")
    time.sleep(.5); check(len(got) == 0, "honeypot preenchido não chega à API")
    mode["status"] = 500; pg.goto("http://localhost:5598/contato/")
    pg.fill("[name=nome]", "Dani"); pg.fill("[name=email]", "d@d.com"); pg.select_option("[name=assunto]", "SargLab"); pg.fill("[name=mensagem]", "mensagem de teste aqui"); pg.check("[name=consentimento]"); pg.click("button[type=submit]")
    pg.wait_for_selector(".status.err"); check("Não foi possível" in pg.inner_text(".status"), "erro do servidor não é mostrado como sucesso")
    b.close()
srv.terminate(); print("RESULTADO:", "tudo certo" if ok else "HÁ FALHAS"); sys.exit(0 if ok else 1)

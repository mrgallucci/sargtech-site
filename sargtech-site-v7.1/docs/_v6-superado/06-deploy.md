# Instruções de deploy (ainda não executado)
O site é estático: publique o conteúdo de `dist/` na raiz de `sargtech.com.br`.

1. Gere a versão: `python3 src/build.py` (sem dependências).
2. Teste local: `python3 -m http.server 5500 -d dist` e abra http://localhost:5500. Rode `python3 tests/forms.py` e `python3 tests/responsive.py` (exigem Playwright).
3. Hospedagem: qualquer host estático com HTTPS (Cloudflare Pages, Netlify, Vercel, Nginx). Aplicar `dist/_headers` (Netlify/Cloudflare) ou equivalente em Nginx.
4. DNS: `sargtech.com.br` e `www` (redirecionar www para o domínio principal) para o host; `crm.` e `api.` continuam onde estão.
5. API: liberar CORS para `https://sargtech.com.br`; criar/ajustar os endpoints públicos (`02-endpoints.md`) **antes** de ligar o site.
6. Validar em produção: enviar um lead de teste em cada formulário e confirmar no Gestão Inteligente: nome, e-mail, WhatsApp, área, consentimento, origem, utm_*, referrer e landing.
7. Manter a landing do GitHub Pages ativa até o item 6 passar; depois redirecionar para `/sarglab/ebook/`.
8. Só então anunciar. Checkout permanece desligado (`checkoutEnabled:false`) até o fluxo de `03-pagamento-matricula.md` estar validado.
Rollback: republicar a versão anterior de `dist/`; nada no CRM/API é alterado por este site.

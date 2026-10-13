# Checklists

## Mobile (resultado do teste automatizado, `tests/responsive.py`)
- [x] 360 px, 390 px, 430 px, tablet 768, notebook 1366, desktop 1920
- [x] 7 páginas por largura = 42 verificações, sem overflow lateral
- [x] Menu móvel com botão, foco e Esc
- [x] Alvos de toque ≥ 44 px; campos com 16 px (evita zoom no iOS)
- [ ] Teste manual em aparelho real (iOS Safari e Android Chrome) antes de divulgar
- [ ] Teste do login e da área do aluno (fora deste projeto)

## Segurança
- [x] Nenhum segredo no repositório do site; `config.js` só tem dados públicos
- [x] HTTPS e cabeçalhos (CSP, HSTS, nosniff, frame-ancestors) em `dist/_headers`
- [x] Honeypot nos formulários; envio com timeout; sem credenciais de navegador
- [ ] CORS restritivo na API (`https://sargtech.com.br` e `https://crm.sargtech.com.br`)
- [ ] Rate limit nos endpoints públicos
- [ ] Validação server-side dos formulários
- [ ] Webhook com assinatura validada e consulta ao Mercado Pago
- [ ] Processamento idempotente (referência testada)
- [ ] Senhas com hash adequado; cookies seguros
- [ ] Revisar a CSP em produção (o CSS usa estilos inline; `style-src 'unsafe-inline'` está liberado)

## SEO e acessibilidade
- [x] title, description, canonical, Open Graph por página; sitemap; robots; favicon; 404 noindex
- [x] Headings semânticos; skip link; foco visível; labels nos campos; `lang="pt-BR"`; `prefers-reduced-motion`
- [ ] Rodar Lighthouse após o deploy
- [ ] Verificar a imagem og em uma pré-visualização de compartilhamento

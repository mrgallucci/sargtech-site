# SARGTECH site — V6 integrada ao backend real

Data: 13/10/2026. **Nada foi publicado.** Render, GitHub Pages e DNS não foram tocados.

## Mudanças no site
- `src/config.js`: endpoints corrigidos para `POST https://api.sargtech.com.br/api/public/leads/ebook` e `/api/public/leads/contact`.
- `/sarglab/ebook/`: reconstruída a partir da landing atual (hero, problema, Método CLARO C-L-A-R-O, conteúdo do guia, públicos, 9 áreas profissionais originais, texto de consentimento original, treinamentos em produção, uso responsável). PDF atual copiado byte a byte; download automático após 400 ms com link de reserva; 409 não bloqueia o download.
- Origem do e-book: `utm_source`, senão domínio do referrer (instagram/linkedin/facebook/google), senão `direto` (mesma regra da landing). WhatsApp só dígitos.
- UTM completos (source, medium, campaign, content, term), `referrer` e `landing_url` enviados em e-book e contato; persistem entre páginas da visita (sessionStorage).
- Contato e lista de aviso usam o endpoint de contato, com `origem` identificável (`site-contato`, `sarglab-cursos-aviso`).
- Oferta SargLab alinhada à landing: Curso Básico (R$19,90 lançamento) e Programa Completo (R$149,90, Básico + Avançado), **em produção, não à venda**. Removido "módulos individuais" e o botão de compra.
- Privacidade e Termos: textos aprovados da landing (07/10/2026); nova rota `/termos/`.
- `backend-reference/` (SQL 001, commerce.py) removido do pacote.
- Checkout: nenhum código de checkout no site.

## Testes (site)
- `tests/forms.py` (Playwright, API simulada): 12/12 OK, incluindo endpoints reais, origem, 409, honeypot, falha de servidor.
- `tests/responsive.py`: 8 páginas × 6 larguras = 48 checagens, 0 com overflow. Screenshots atualizados em `docs/screenshots/`.
- **Não executado:** teste contra a API real (não há backend rodando aqui). O fluxo ponta a ponta fica para a homologação local.

## Backend (patch `0001-…patch`, branch `integracao-site-v6`)
Ver `INTEGRACAO_SITE.md`. **Testes do backend não executados** (pypi.org bloqueado); comando para rodar localmente no mesmo arquivo.

## Homologação local sugerida
1. Aplicar o patch no repositório do backend, instalar dependências, `pytest`, `alembic upgrade head`, `alembic check`.
2. Subir a API local; no site, apontar `apiBase` para `http://127.0.0.1:8000` em cópia local de `config.js` e adicionar a origem do servidor estático em `CORS_ORIGINS`.
3. Enviar o e-book e o contato; conferir lead, `lead_touchpoints` e `/api/marketing-analytics/attribution` no Gestão Inteligente.
4. Só depois: cutover (CORS no Render, DNS, GitHub Pages por último).

## Decisões registradas (13/10/2026)
- Oferta: Opção A (Curso Básico R$19,90; Programa Completo R$149,90 = pacote Básico + Avançado). Sem módulos avulsos; sem migration agora. Pacote exige tabela de grants produto→cursos antes do checkout.
- Aluno pós-pagamento: token de ativação (hash, uso único, expira), sem senha temporária; role de admin/vendedor nunca é alterada.
- CORS no cutover: `https://sarg-tech.github.io,https://sargtech.com.br,https://www.sargtech.com.br`; Render não alterado.
- Rate limit desligado; `TRUST_PROXY_HEADERS` não ligar em produção até validar IP no Render.

## Aprovações pendentes
- Cutover: variáveis do Render (`CORS_ORIGINS`), DNS, desligamento do GitHub Pages.
- Ligar rate limit (`PUBLIC_RATE_LIMIT_PER_MIN`, `TRUST_PROXY_HEADERS`).
- Mercado Pago (`MERCADO_PAGO.md`): desenho e decisão sobre onboarding do usuário aluno.
- Revisão jurídica de privacidade/termos; limitação pública de `/uploads` (D1).

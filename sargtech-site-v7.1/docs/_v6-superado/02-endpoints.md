# Rotas, endpoints e variáveis

## Rotas do site (estático, `dist/`)
| Rota | Conteúdo |
|---|---|
| `/` | Home: posicionamento, soluções, método, ecossistema |
| `/gestao-inteligente/` | Página institucional do software (sem preço, sem CTA de compra) + botão Acessar plataforma |
| `/sarglab/` | Produto educacional: proposta, público, método, produtos |
| `/sarglab/ebook/` | Landing do e-book gratuito com formulário |
| `/sarglab/cursos/` | Formatos completo e módulos + lista de aviso (checkout desligado) |
| `/contato/` | Fale com a SARGTECH |
| `/privacidade/` | Minuta da política |
| `crm.sargtech.com.br/login` | Login central (fora deste projeto; só link) |

## Endpoints públicos esperados da API (PROPOSTOS; ajustar ao contrato real)
Configurados em `src/config.js`. Todos recebem JSON, `credentials: omit`.

**POST /public/leads/ebook** e **POST /public/leads/contact**
```json
{ "nome":"", "email":"", "whatsapp":"", "area_profissional":"",
  "empresa":"", "telefone":"", "assunto":"", "interesse":"", "mensagem":"",
  "consentimento": true, "consentimento_versao": "privacidade-v1-minuta",
  "origem": "ebook-sarglab | site-contato | sarglab-cursos-aviso",
  "pagina": "/sarglab/ebook/",
  "utm_source":null,"utm_medium":null,"utm_campaign":null,"utm_content":null,"utm_term":null,
  "referrer":null, "landing_url":"" }
```
Requisitos no servidor: validar tudo no servidor; gravar consentimento com data/hora do servidor; criar ou atualizar o contato por e-mail (sem duplicar); gravar origem e utm_* para análise de aquisição; rate limit por IP; resposta 2xx em sucesso, 422 em validação, 429 em excesso; CORS apenas para `https://sargtech.com.br`.
O formulário de contato **não** deve reutilizar o endpoint do e-book: tem endpoint próprio.

**POST /public/checkout/orders** (futuro, desligado): recebe `product_slug`, dados do comprador e utm; cria o pedido e devolve a URL de checkout do Mercado Pago. Preço sempre vem do banco, nunca do navegador.
**POST /webhooks/mercadopago**: ver `03-pagamento-matricula.md`.

## Variáveis de ambiente (sem valores)
Backend: `MP_ACCESS_TOKEN`, `MP_WEBHOOK_SECRET`, `MP_PUBLIC_KEY` (só se usar SDK no navegador), `DATABASE_URL`, `JWT_SECRET`, `CORS_ALLOWED_ORIGINS=https://sargtech.com.br,https://crm.sargtech.com.br`, `PUBLIC_SITE_URL`, `RATE_LIMIT_PUBLIC` (ex.: 10/min por IP).
Site estático: nenhuma variável secreta. `src/config.js` é público: `apiBase`, `endpoints`, `ebookDownloadUrl`, `checkoutEnabled`, `contactEmail`.

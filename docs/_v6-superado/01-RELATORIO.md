# SARGTECH site v6: relatório da entrega (13/10/2026)

**Status:** candidato a produção do **frontend**. Nada foi publicado. Nada foi alterado em CRM, API ou banco.

## O que veio na pasta V5 e o que não veio
A V5 continha só a landing estática (index, obrigado, styles, script, 2 logos). **Não foram fornecidos:** código do Gestão Inteligente (FastAPI/Next.js), banco, landing atual do e-book (GitHub Pages), nem acesso a sargtech.com.br, crm. ou api. Por isso, tudo o que depende desses sistemas está entregue como **especificação e código de referência**, não como integração testada.

## Entregue e testado
| Item | Situação |
|---|---|
| Site em 7 páginas + 404 (home, Gestão Inteligente, SargLab, e-book, cursos, contato, privacidade) | Pronto em `dist/` |
| Identidade visual v1 mantida (Inter, deep/brand/signal/accent, wordmark) | Aplicada; wordmark agora é texto HTML (o SVG da V5 dependia de fonte não embutida) |
| Header com "Acessar plataforma" para https://crm.sargtech.com.br/login | Pronto (link, sem login duplicado) |
| Formulários (e-book, contato, lista de aviso) enviando JSON à API, com utm_source/medium/campaign/content/term, referrer e URL da landing | **Testado com a API simulada** (`tests/forms.py`, 9 verificações) |
| UTMs mantidas entre páginas da mesma visita | Testado |
| Honeypot e tratamento de erro (nunca mostra sucesso se a API falhar) | Testado |
| Responsivo: 360, 390, 430, 768, 1366, 1920 em 7 páginas | 42 verificações, **0 overflow lateral** (`tests/responsive.py`); screenshots em `docs/screenshots/` |
| SEO: title, description, canonical, Open Graph, favicon, sitemap.xml, robots.txt, 404 | Pronto |
| Segurança de borda: `_headers` com CSP, HSTS, nosniff, frame-ancestors | Pronto (aplicar no host) |
| Lógica pagamento → matrícula → acesso (idempotente, produto completo x módulo, estorno) | **Código de referência com 8 testes passando** (`backend-reference/`), usando SQLite só para provar a lógica |
| Migration SQL de referência (products, product_modules, orders, payment_events, enrollments) | Escrita, **não aplicada** |

## NÃO feito (e por quê)
- **Integração comprovada com o CRM:** impossível sem acesso à API. Provei apenas que o site envia o payload correto. O contrato real do endpoint do e-book precisa ser conferido (ver `02-endpoints.md`).
- **Migração da landing do e-book:** não tenho o código validado do GitHub Pages. Reconstruí a landing com os campos pedidos; as opções do campo "área profissional" e o texto final precisam ser comparados com a versão original.
- **Validação de RBAC no backend (admin/vendedor/aluno):** exige o repositório. Entreguei o checklist e o teste a executar (`04-permissoes.md`).
- **Mercado Pago real, webhook, matrícula em produção:** apenas arquitetura e referência. `checkoutEnabled` está `false`.
- **Screenshots do CRM e da área do aluno:** não existem aqui. As telas do site usam esquemas conceituais rotulados.
- **Deploy em sargtech.com.br:** não executado, conforme sua instrução de validar antes.

## Decisões de conteúdo (sem invenção)
- Gestão Inteligente: apresentado como software próprio, em uso pela SARGTECH, **sem preço, plano ou CTA de compra** e com a frase "não é oferecido como serviço neste momento".
- SargLab: sem módulos, aulas, durações, preços, certificado ou bônus. A página de cursos mostra dois formatos (completo e módulos) com "em definição".
- Sem clientes, depoimentos ou números.
- "Método CLARO" é citado pelo nome; o significado das letras não foi publicado porque não está nos materiais que tenho.

## Pendências para você (aprovação do fundador)
1. **CNPJ:** a SARGTECH não tem CNPJ (você adiou). Cobrar por cursos exige definir quem vende e emite o recebimento (pessoa física ou formalização). O rodapé não cita CNPJ. Decida isso antes de ligar o checkout.
2. Nomes dos produtos SargLab: seus registros listam e-book gratuito, Curso Básico, Curso Avançado e Programa Completo, e a ordem de hoje fala em "SargLab Completo" e módulos. Confirme os nomes oficiais, conteúdos, duração e preços.
3. URL do e-book (para o botão de download) e título final (o site usa o provisório "IA para quem tem trabalho pra fazer").
4. Lista de opções de "área profissional" da landing atual.
5. Contrato real da API de leads (caminho, campos, resposta) e se a API aceita CORS de https://sargtech.com.br.
6. Política de privacidade: é **minuta**; precisa de revisão jurídica e do nome do controlador.
7. Instagram: o link usa @sarglab.ia (conforme seus registros). Confirme.
8. E-mail comercial SARGrowth@proton.me mantido da V5. Confirme que é o canal oficial público.
9. Favicon e og-image são propostas (o wordmark não tem símbolo).
10. Revisar o texto: "Método CLARO", "foco em prática", "uso responsável" na página SargLab são descrições gerais; ajuste ao que o produto realmente entrega.

## Arquivos
Criados: tudo em `src/` (site.css, site.js, config.js, build.py, og.html, og-image.png), `dist/` (gerado), `tests/`, `backend-reference/`, `docs/`.
Substituídos da V5: index.html, styles.css, script.js (reescritos); removidos: obrigado.html (sucesso agora é inline), logos SVG (wordmark em HTML), Netlify Forms.

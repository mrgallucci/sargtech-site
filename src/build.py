#!/usr/bin/env python3
"""Gera dist/ a partir destas páginas. Uso: python3 src/build.py"""
import os, shutil, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
SRC = os.path.join(ROOT, "src")
SITE = "https://sargtech.com.br"
LOGIN = "https://crm.sargtech.com.br/login"
EMAIL = "SARGrowth@proton.me"
LINKEDIN = "https://www.linkedin.com/in/mrgallucci/"
INSTA = "https://www.instagram.com/sarglab.ia/"
TODAY = "2026-10-13"

WM = '<span class="wm">SARG<b>TECH</b></span>'
WM_L = '<span class="wm light">SARG<b>TECH</b></span>'
ARROW = '<span aria-hidden="true">&rarr;</span>'

NAV = [("/", "Início"), ("/gestao-inteligente/", "Gestão Inteligente"), ("/sarglab/", "SargLab"), ("/contato/", "Contato")]

def header(path):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if (href == path or (href != "/" and path.startswith(href))) else ""
        links += '<a class="l" href="%s"%s>%s</a>' % (href, cur, label)
    return f'''<a class="skip" href="#conteudo">Ir para o conteúdo</a>
<header class="hd"><div class="container hd-in">
<a href="/" aria-label="SARGTECH, página inicial">{WM}</a>
<button class="burger" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="nav"><i></i><i></i><i></i></button>
<nav class="nav" id="nav" aria-label="Principal">{links}
<a class="btn btn-o" href="{LOGIN}" rel="noopener">Acessar plataforma</a>
<a class="btn btn-p" href="/contato/">Falar com a SARGTECH</a></nav>
</div></header>'''

FOOTER = f'''<footer class="ft"><div class="container">
<div class="ft-in">
<div><div class="on-dark">{WM_L}</div><p style="margin-top:12px;max-width:34ch">Tecnologia aplicada a negócios reais.</p></div>
<div><h4>Site</h4><a href="/">Início</a><a href="/gestao-inteligente/">Gestão Inteligente</a><a href="/sarglab/">SargLab</a><a href="/contato/">Contato</a></div>
<div><h4>SargLab</h4><a href="/sarglab/ebook/">E-book gratuito</a><a href="/sarglab/cursos/">Cursos</a><a href="{INSTA}" target="_blank" rel="noopener noreferrer">Instagram @sarglab.ia</a></div>
<div><h4>Contato</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn do criador</a><a href="{LOGIN}" rel="noopener">Acessar plataforma</a></div>
</div>
<div class="ft-b"><span>&copy; <span id="year">2026</span> SARGTECH. Todos os direitos reservados.</span><span><a style="display:inline" href="/privacidade/">Privacidade</a> &middot; <a style="display:inline" href="/termos/">Termos</a></span><span>SIGNAL &middot; ATTRIBUTION &middot; RETENTION &middot; GROWTH</span></div>
</div></footer>'''

def page(path, title, desc, body, og_title=None, noindex=False, extra_head=""):
    canonical = SITE + path
    ogt = html.escape(og_title or title)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0F1C2E">
<meta property="og:site_name" content="SARGTECH">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{ogt}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:alt" content="SARGTECH: tecnologia aplicada a negócios reais">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{extra_head}
</head>
<body>
{header(path)}
<main id="conteudo">
{body}
</main>
{FOOTER}
<script src="/assets/config.js"></script>
<script src="/assets/site.js" defer></script>
</body>
</html>'''

def band(h, p, label, href):
    return f'<section class="sec"><div class="container"><div class="band on-dark"><div><h2>{h}</h2><p>{p}</p></div><a class="btn btn-p" href="{href}">{label} {ARROW}</a></div></div></section>'

def consent():
    return '<label class="consent"><input type="checkbox" name="consentimento" required><span>Li e concordo com o uso dos meus dados para responder a este contato, conforme a <a href="/privacidade/" target="_blank">política de privacidade</a>. *</span></label>'

HONEY = '<p class="vh" aria-hidden="true"><label>Não preencha este campo<input name="website" tabindex="-1" autocomplete="off"></label></p>'

pages = {}

# ------------------------------------------------------------------ HOME
pages["/"] = page("/", "SARGTECH | Tecnologia aplicada a negócios reais",
  "A SARGTECH desenvolve sistemas, dados, automação e IA aplicada a negócios. Conheça o Gestão Inteligente, nosso software próprio, e o SargLab, nosso produto educacional.",
  f'''
<section class="hero"><div class="container hero-in two on-dark">
<div>
<div class="eyebrow">Tecnologia aplicada a negócios reais</div>
<h1>Tecnologia aplicada a <em>negócios reais.</em></h1>
<p class="lead">A SARGTECH é uma startup de tecnologia. Desenvolvemos sistemas, dados, automação e inteligência artificial aplicada, e usamos nossa própria tecnologia para operar o que construímos.</p>
<div class="cta"><a class="btn btn-p" href="#solucoes">Conhecer nossas soluções {ARROW}</a><a class="btn btn-o" href="/sarglab/">Conhecer o SargLab</a><a class="btn btn-o" href="{LOGIN}" rel="noopener">Acessar plataforma</a></div>
</div>
<div class="eco" role="img" aria-label="Esquema conceitual do ecossistema SARGTECH: a SARGTECH desenvolve o Gestão Inteligente e o SargLab, e o aluno estuda dentro do Gestão Inteligente">
<div class="lbl">Ecossistema &middot; esquema conceitual</div>
<div class="eco-box eco-top">SARGTECH</div>
<div class="eco-arrow">desenvolve</div>
<div class="eco-row"><div class="eco-box eco-b">Gestão Inteligente<small>Software próprio</small></div><div class="eco-box eco-b">SargLab<small>Produto educacional</small></div></div>
<div class="eco-flow">O aluno do SargLab estuda dentro do Gestão Inteligente.</div>
</div>
</div></section>

<section class="sec" id="quem-somos"><div class="container">
<div class="sec-head"><div class="eyebrow">Quem somos</div><h2 class="h2">SARG: quatro palavras que orientam o trabalho.</h2><p class="lead">A SARGTECH reúne tecnologia e visão de negócio. O nome vem da sigla SARG, somada a TECH, de tecnologia para colocar essas ideias em prática.</p></div>
<div class="sarg"><div class="a1"><b>S</b><span>Signal</span><small>Sinal</small></div><div class="a2"><b>A</b><span>Attribution</span><small>Atribuição</small></div><div class="a3"><b>R</b><span>Retention</span><small>Retenção</small></div><div class="a4"><b>G</b><span>Growth</span><small>Crescimento</small></div></div>
</div></section>

<section class="sec alt" id="solucoes"><div class="container">
<div class="sec-head"><div class="eyebrow">O que desenvolvemos</div><h2 class="h2">Soluções que partem do desafio do negócio.</h2><p class="lead">Cada empresa tem processos, pessoas e decisões próprias. Criamos tecnologia com propósito, em vez de acumular funcionalidades.</p></div>
<div class="grid g3">
<div class="card"><span class="num">01</span><h3>Sistemas e aplicações web</h3><p>Software sob medida para a rotina do negócio.</p></div>
<div class="card"><span class="num">02</span><h3>CRM e gestão comercial</h3><p>Relacionamento, leads e vendas em um só lugar.</p></div>
<div class="card"><span class="num">03</span><h3>Dados e analytics</h3><p>Informação organizada para apoiar decisões.</p></div>
<div class="card"><span class="num">04</span><h3>Automação</h3><p>Menos tarefa repetida, mais processo organizado.</p></div>
<div class="card"><span class="num">05</span><h3>IA aplicada</h3><p>Usada onde resolve um problema concreto.</p></div>
<div class="card"><span class="num">06</span><h3>Conversa sobre o seu caso</h3><p>Tem um processo que precisa evoluir? <a href="/contato/" style="color:var(--brand);font-weight:700;text-decoration:underline">Fale com a SARGTECH</a>.</p></div>
</div></div></section>

<section class="sec"><div class="container">
<div class="sec-head"><div class="eyebrow">Como usamos tecnologia</div><h2 class="h2">Primeiro o problema. Depois o código.</h2></div>
<div class="flow" style="--n:4"><div>Entender<small>Ouvir e mapear o processo</small></div><div>Planejar<small>Requisitos, fluxos e prioridades</small></div><div>Desenvolver<small>Entregas incrementais</small></div><div>Validar e evoluir<small>Testar, corrigir e documentar</small></div></div>
</div></section>

<section class="sec dark" id="ecossistema"><div class="container">
<div class="sec-head"><div class="eyebrow">Ecossistema SARGTECH</div><h2 class="h2">Um software próprio e um produto que o coloca em uso.</h2></div>
<div class="grid g2">
<article class="card"><span class="tag s">Software próprio</span><h3>Gestão Inteligente</h3><p>Plataforma desenvolvida pela SARGTECH para centralizar leads, funil comercial, vendas, analytics, pagamentos, matrículas e área do aluno. Hoje sustenta a operação da própria SARGTECH.</p><p style="margin-top:18px"><a class="btn btn-o" href="/gestao-inteligente/">Conhecer a plataforma</a></p></article>
<article class="card"><span class="tag">Produto educacional</span><h3>SargLab</h3><p>IA prática para quem trabalha. Conteúdo gratuito, e-book e cursos para aplicar inteligência artificial na rotina, com método próprio.</p><p style="margin-top:18px"><a class="btn btn-o" href="/sarglab/">Conhecer o SargLab</a></p></article>
</div>
<p class="note">O Gestão Inteligente é de uso da própria SARGTECH e não é oferecido como serviço neste momento.</p>
</div></section>

<section class="sec"><div class="container founder">
<div class="sec-head"><div class="eyebrow">Por que a SARGTECH existe</div><h2 class="h2">Necessidade real. Tecnologia com propósito.</h2><p class="lead">A SARGTECH foi criada por Maxwell Gallucci Rodrigues para transformar rotinas manuais, informações dispersas e processos pouco eficientes em soluções digitais claras, organizadas e úteis.</p><p style="margin-top:20px"><a class="btn btn-o" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">Conhecer o criador no LinkedIn</a></p></div>
</div></section>

{band("Seu próximo projeto começa com uma conversa.", "Conte o contexto. A primeira conversa serve para entender a necessidade e avaliar possibilidades.", "Falar com a SARGTECH", "/contato/")}
''')

# ------------------------------------------------------------------ GESTAO INTELIGENTE
def mod(t, d): return f'<div class="mod"><h3>{t}</h3><p>{d}</p></div>'
pages["/gestao-inteligente/"] = page("/gestao-inteligente/", "Gestão Inteligente | Software próprio da SARGTECH",
  "O Gestão Inteligente é a plataforma desenvolvida pela SARGTECH que centraliza leads, funil comercial, vendas, analytics, pagamentos, matrículas e área do aluno.",
  f'''
<section class="hero sub"><div class="container hero-in on-dark">
<div style="max-width:760px"><div class="eyebrow">Software próprio da SARGTECH</div>
<h1>Gestão Inteligente</h1>
<p class="lead">Uma plataforma desenvolvida pela SARGTECH para centralizar relacionamento, vendas, dados, pagamentos e educação em um só lugar.</p>
<div class="cta"><a class="btn btn-p" href="{LOGIN}" rel="noopener">Acessar plataforma {ARROW}</a><a class="btn btn-o" href="/sarglab/">Ver como o SargLab usa a plataforma</a></div></div>
</div></section>

<section class="sec"><div class="container">
<div class="sec-head"><div class="eyebrow">O que é</div><h2 class="h2">A tecnologia que sustenta a operação da SARGTECH.</h2>
<p class="lead">O Gestão Inteligente nasceu para que a SARGTECH operasse seus próprios processos e validasse sua tecnologia na prática, a começar pelo SargLab. Ele reúne em uma base única o que costuma ficar espalhado em planilhas, conversas e ferramentas isoladas.</p></div>
<div class="mods">
{mod("Leads e relacionamento","Captação de leads, com a origem de cada contato, e o histórico do relacionamento.")}
{mod("Funil comercial e vendas","Etapas do funil e acompanhamento das vendas.")}
{mod("Campanhas","Organização das ações de aquisição e comunicação.")}
{mod("Marketing e Customer Analytics","Dados de aquisição, conversão e comportamento para análise.")}
{mod("Indicadores e financeiro da operação","Indicadores de acompanhamento e gestão financeira ligada à operação.")}
{mod("Pagamentos e matrículas","Pedidos, confirmação de pagamento e matrícula do aluno no produto adquirido.")}
{mod("Usuários e perfis","Um login central e perfis de acesso: administração, vendedor e aluno.")}
{mod("LMS e área do aluno","Cursos, módulos, aulas, materiais e progresso, conforme a plataforma evolui.")}
</div>
<p class="note">A plataforma evolui por versões. Funcionalidades educacionais, como progresso e presença, avançam conforme o desenvolvimento.</p>
</div></section>

<section class="sec alt"><div class="container">
<div class="sec-head"><div class="eyebrow">Acesso</div><h2 class="h2">Um único login. Cada perfil vê só o que é seu.</h2><p class="lead">A tela de acesso é a mesma para todos. Depois de entrar, cada pessoa encontra apenas as funções autorizadas para o seu papel.</p></div>
<div class="grid g3">
<div class="card"><h3>Administração</h3><p>Áreas administrativas autorizadas do Gestão Inteligente.</p></div>
<div class="card"><h3>Vendedor</h3><p>Funções comerciais autorizadas para o seu papel.</p></div>
<div class="card"><h3>Aluno</h3><p>Cursos adquiridos, módulos, aulas, materiais, progresso e conta.</p></div>
</div>
<p style="margin-top:28px"><a class="btn btn-p" href="{LOGIN}" rel="noopener">Acessar plataforma {ARROW}</a></p>
</div></section>

<section class="sec"><div class="container">
<div class="sec-head"><div class="eyebrow">Como se conecta</div><h2 class="h2">Da aquisição ao estudo, na mesma base.</h2></div>
<div class="flow" style="--n:6"><div>Visita<small>Site e redes</small></div><div>Lead<small>E-book ou contato</small></div><div>Pedido<small>Produto escolhido</small></div><div>Pagamento<small>Confirmado no servidor</small></div><div>Matrícula<small>Acesso ao que foi adquirido</small></div><div>Área do aluno<small>Estudo e progresso</small></div></div>
<p class="note">Esquema conceitual da jornada que a plataforma foi desenhada para acompanhar. Não representa capturas de tela.</p>
</div></section>
{band("Quer conversar sobre tecnologia para o seu negócio?", "O Gestão Inteligente é de uso da SARGTECH. Se o seu desafio é outro, conte o contexto e avaliamos juntos.", "Falar com a SARGTECH", "/contato/")}
''')

# ------------------------------------------------------------------ SARGLAB
pages["/sarglab/"] = page("/sarglab/", "SargLab | IA prática para quem trabalha",
  "O SargLab é o produto educacional da SARGTECH: IA prática para quem trabalha. E-book gratuito, método próprio e cursos para aplicar IA na rotina.",
  f'''
<section class="hero sub"><div class="container hero-in on-dark">
<div style="max-width:760px"><div class="eyebrow">Produto educacional da SARGTECH</div>
<h1>SargLab: IA prática <em>para quem trabalha.</em></h1>
<p class="lead">Aprenda a usar inteligência artificial na rotina do trabalho com foco na prática, em linguagem simples e com método.</p>
<div class="cta"><a class="btn btn-p" href="/sarglab/ebook/">Baixar o e-book gratuito {ARROW}</a><a class="btn btn-o" href="/sarglab/cursos/">Ver os treinamentos</a></div></div>
</div></section>

<section class="sec"><div class="container"><div class="grid g2">
<div><div class="eyebrow">Para quem é</div><h2 class="h2">Para quem tem trabalho a fazer.</h2><p class="lead">Pessoas e profissionais que querem usar IA no dia a dia, sem precisar de formação técnica.</p></div>
<div><div class="eyebrow">O problema</div><h2 class="h2">IA existe. Aplicar é outra história.</h2><p class="lead">Muita gente ouve falar de IA, mas não sabe por onde começar nem como aplicar na própria rotina. O SargLab organiza esse caminho.</p></div>
</div></div></section>

<section class="sec alt"><div class="container">
<div class="sec-head"><div class="eyebrow">Metodologia</div><h2 class="h2">Método CLARO.</h2><p class="lead">O SargLab segue um método próprio, o Método CLARO, que orienta o aprendizado do uso de IA em situações práticas de trabalho. Teoria na medida certa, prática em primeiro lugar.</p></div>
<div class="grid g2">
<div class="card"><h3>O que propomos</h3><ul class="chk"><li>Linguagem simples e exemplos do dia a dia de trabalho.</li><li>Foco em prática, não em jargão.</li><li>Uso responsável: IA como apoio, com conferência humana.</li></ul></div>
<div class="card"><h3>O que não prometemos</h3><ul class="chk no"><li>Enriquecimento ou ganhos garantidos com IA.</li><li>Automatizar todo o seu trabalho.</li><li>Resultados garantidos.</li></ul></div>
</div></div></section>

<section class="sec"><div class="container">
<div class="sec-head"><div class="eyebrow">Produtos</div><h2 class="h2">Do conteúdo gratuito ao curso.</h2></div>
<div class="grid g3">
<article class="card"><span class="tag s">Gratuito</span><h3>E-book SargLab</h3><p>Guia de 7 páginas com o Método CLARO, 4 prompts práticos e o semáforo de segurança.</p><p style="margin-top:16px"><a class="btn btn-p" href="/sarglab/ebook/">Baixar o e-book</a></p></article>
<article class="card"><span class="tag">Em produção</span><h3>Curso Básico</h3><p>Estruturar pedidos, comparar resultados, corrigir respostas e transformar o Método CLARO em rotina. Preço de lançamento: R$19,90.</p><p style="margin-top:16px"><a class="btn btn-o" href="/sarglab/cursos/#basico">Ver detalhes</a></p></article>
<article class="card"><span class="tag">Em produção</span><h3>Programa Completo</h3><p>Curso Básico + Curso Avançado, com assistentes, fluxos de trabalho e automações sem código. Preço de lançamento: R$149,90.</p><p style="margin-top:16px"><a class="btn btn-o" href="/sarglab/cursos/#completo">Ver detalhes</a></p></article>
</div>
<p class="note">Os treinamentos estão em produção e ainda não estão à venda. Quando as inscrições abrirem, a compra será confirmada pelo servidor e o acesso aparecerá na sua área do aluno.</p>
</div></section>

<section class="sec dark"><div class="container">
<div class="sec-head"><div class="eyebrow">Como funciona</div><h2 class="h2">Sua conta é a sua sala de aula.</h2><p class="lead">O aluno estuda dentro do Gestão Inteligente, a plataforma da SARGTECH. O que aparece para você depende do que você adquiriu.</p></div>
<div class="flow" style="--n:5"><div>E-book<small>Conteúdo gratuito</small></div><div>Interesse<small>Escolha do treinamento</small></div><div>Compra<small>Pagamento confirmado (quando abrir)</small></div><div>Matrícula<small>Acesso ao que foi comprado</small></div><div>Área do aluno<small>Estudo e progresso</small></div></div>
<p style="margin-top:28px"><a class="btn btn-o" href="{LOGIN}" rel="noopener">Já sou aluno: acessar plataforma</a></p>
</div></section>
{band("Quer continuar aprendendo?", "Veja os treinamentos em produção ou acompanhe o conteúdo no Instagram @sarglab.ia.", "Ver cursos", "/sarglab/cursos/")}
''')

# ------------------------------------------------------------------ EBOOK
# Conteúdo aprovado da landing atual (sarg-tech/sarglab-ebook-landing). Método CLARO, áreas e consentimento preservados.
AREAS = [("vendas","Vendas"),("atendimento","Atendimento"),("administrativo","Administrativo"),("gestao","Gestão"),("rh","RH"),("marketing","Marketing"),("tecnologia","Tecnologia"),("empreendedor","Empreendedor(a)"),("outro","Outra área")]
area_opts = '<option value="" disabled selected>Selecione</option>' + "".join(f'<option value="{v}">{l}</option>' for v, l in AREAS)
EB_PDF = "/assets/downloads/sarglab-ia-para-quem-tem-trabalho-pra-fazer.pdf"
def ebook_consent():
    return '<label class="consent"><input type="checkbox" name="consentimento" required><span>Concordo em fornecer meus dados para receber o guia e comunicações relacionadas à SargLab. Li a <a href="/privacidade/" target="_blank">Política de Privacidade</a> e posso solicitar a remoção dos meus dados posteriormente. *</span></label>'
CLARO = [("C","Contexto e papel","Qual é a situação e qual papel a IA deve assumir?"),("L","Linha de chegada","O que você quer ter em mãos ao final?"),("A","Amarras","Quais são os limites, tom, tamanho e restrições?"),("R","Roteiro de saída","Como você quer receber a resposta?"),("O","Olhar crítico","O que precisa ser verificado antes de usar?")]
claro_html = "".join(f'<div class="card"><span class="tag">{l}</span><h3>{t}</h3><p>{d}</p></div>' for l,t,d in CLARO)
pages["/sarglab/ebook/"] = page("/sarglab/ebook/", "SargLab — IA para quem tem trabalho pra fazer",
  "Baixe gratuitamente o guia SargLab IA para quem tem trabalho pra fazer: o Método CLARO, um antes e depois de pedido vago × pedido estruturado, 4 prompts práticos e um semáforo de segurança para usar IA no trabalho.",
  f'''
<section class="hero sub"><div class="container hero-in two on-dark">
<div><div class="eyebrow">SargLab &middot; um produto SARGTECH</div>
<h1>IA para quem tem <em>trabalho pra fazer.</em></h1>
<p class="lead">Um guia gratuito para usar Inteligência Artificial com mais clareza, método e segurança no dia a dia profissional.</p>
<ul class="chk" style="color:#fff"><li>Método CLARO</li><li>Antes e depois: vago × CLARO</li><li>4 prompts práticos</li><li>Semáforo de segurança</li></ul>
<div class="cta"><a class="btn btn-p" href="#baixar">Quero o guia gratuito {ARROW}</a><a class="btn btn-o" href="#metodo">Conhecer o Método CLARO</a></div>
<p class="fine" style="color:#A9B8CC;margin-top:14px">Gratuito &middot; direto ao ponto &middot; sem precisar saber programar</p></div>
<div style="text-align:center"><img src="/assets/capa-ebook-sarglab.webp" width="320" height="569" alt="Capa do guia gratuito IA para quem tem trabalho pra fazer" style="max-width:100%;height:auto;border-radius:16px;box-shadow:0 20px 50px rgba(0,0,0,.35)"></div>
</div></section>

<section class="sec alt"><div class="container">
<div class="sec-head"><div class="eyebrow">O problema não é só a ferramenta</div><h2 class="h2">Você pede para a IA e recebe respostas genéricas?</h2><p class="lead">Muitas vezes, a qualidade da resposta começa pela qualidade do pedido.</p></div>
<div class="grid g3">
<div class="card"><h3>&ldquo;Não sei o que pedir.&rdquo;</h3><p>A ideia está na cabeça, mas transformar isso em um bom pedido nem sempre é simples.</p></div>
<div class="card"><h3>&ldquo;A resposta vem genérica.&rdquo;</h3><p>Sem contexto, objetivo e limites, a IA precisa adivinhar o que você realmente quer.</p></div>
<div class="card"><h3>&ldquo;Não sei o que posso enviar.&rdquo;</h3><p>Usar IA no trabalho também exige atenção com dados, informações internas e privacidade.</p></div>
</div></div></section>

<section class="sec" id="metodo"><div class="container">
<div class="sec-head"><div class="eyebrow">Método CLARO</div><h2 class="h2">Cinco pontos para estruturar pedidos melhores.</h2><p class="lead">O Método CLARO ajuda a organizar o que você precisa informar antes de pedir algo para uma ferramenta de Inteligência Artificial.</p></div>
<div class="grid g3">{claro_html}</div>
<p class="note">Quanto mais importante a tarefa, mais vale percorrer os cinco pontos. <a style="color:var(--brand);text-decoration:underline" href="#baixar">Ver o método aplicado no guia &rarr;</a></p>
</div></section>

<section class="sec dark" id="conteudo"><div class="container">
<div class="sec-head"><div class="eyebrow">Dentro do guia</div><h2 class="h2">7 páginas para sair da teoria e aplicar hoje.</h2><p class="lead">Feito para ler no celular em poucos minutos e testar na mesma hora, com uma tarefa real do seu trabalho.</p></div>
<div class="grid g2">
<div class="card"><h3>01 &middot; Método CLARO</h3><p>As cinco perguntas para estruturar um pedido antes de enviar.</p></div>
<div class="card"><h3>02 &middot; 4 prompts práticos</h3><p>Atendimento, e-mail difícil, ata de reunião e resumo para decisão, com o raciocínio por trás de cada um.</p></div>
<div class="card"><h3>03 &middot; Antes e depois: vago × CLARO</h3><p>O mesmo pedido em duas versões, e por que a segunda gera uma resposta mais útil.</p></div>
<div class="card"><h3>04 &middot; Semáforo de segurança + conferência</h3><p>O que pode, o que anonimizar e o que nunca colocar numa IA pública, e um checklist para conferir a resposta.</p></div>
</div></div></section>

<section class="sec"><div class="container">
<div class="sec-head"><div class="eyebrow">Para quem é</div><h2 class="h2">Para quem quer aplicar IA no trabalho, não estudar IA por estudar.</h2></div>
<div class="grid g3">
<div class="card"><h3>Vendas</h3><p>Follow-ups, organização de argumentos e preparação de mensagens.</p></div>
<div class="card"><h3>Atendimento</h3><p>Respostas mais claras, consistentes e adequadas ao contexto.</p></div>
<div class="card"><h3>Administrativo</h3><p>E-mails, relatórios, organização e tarefas recorrentes.</p></div>
<div class="card"><h3>Gestão</h3><p>Estruturação de informações, análise e apoio à tomada de decisão.</p></div>
<div class="card"><h3>RH</h3><p>Comunicação, organização e apoio a atividades internas sem expor dados desnecessários.</p></div>
<div class="card"><h3>Profissionais em geral</h3><p>Para qualquer pessoa que queira usar IA com mais clareza e menos tentativa e erro.</p></div>
</div></div></section>

<section class="sec alt" id="baixar"><div class="container"><div class="grid g2" style="align-items:start">
<div><div class="eyebrow">Download gratuito</div><h2 class="h2">Comece pelo guia.</h2><p class="lead">Preencha seus dados para receber acesso ao material <strong>IA para quem tem trabalho pra fazer</strong>.</p>
<ul class="chk"><li>7 páginas</li><li>Método CLARO</li><li>4 prompts práticos</li><li>Semáforo de segurança</li></ul></div>
<form class="form" data-kind="ebook" data-success="Cadastro realizado! Seu guia está pronto.">
<h3>Receba o guia gratuito</h3>
{HONEY}
<label>Nome *<input name="nome" required maxlength="100" autocomplete="name"></label>
<label>E-mail *<input name="email" type="email" required maxlength="200" autocomplete="email"></label>
<div class="f2"><label>Área profissional *<select name="area_profissional" required>{area_opts}</select></label>
<label>WhatsApp *<input name="whatsapp" type="tel" required maxlength="30" autocomplete="tel" inputmode="tel" placeholder="(00) 00000-0000"></label></div>
{ebook_consent()}
<button class="btn btn-p" type="submit">Quero receber o guia gratuito {ARROW}</button>
<p class="fine">Seus dados não devem ser compartilhados com terceiros para fins comerciais sem autorização.</p>
<p class="status" role="status" aria-live="polite"></p>
<a class="btn btn-d" data-download href="{EB_PDF}" download hidden>Clique aqui se o download não iniciar</a>
</form></div></div></section>

<section class="sec" id="treinamentos"><div class="container">
<div class="sec-head"><div class="eyebrow">Treinamentos SargLab &middot; em produção</div><h2 class="h2">Quer ir além do guia?</h2><p class="lead">O guia mostra o mapa. Os treinamentos mostram, na tela, como pedir, conferir e refinar respostas no trabalho real.</p></div>
<div class="grid g2">
<article class="card"><h3>Curso Básico</h3><p>Aprenda a estruturar pedidos, comparar resultados, corrigir respostas e transformar o Método CLARO em rotina de trabalho.</p><ul class="chk" style="margin-top:12px"><li>Demonstrações reais em vídeo</li><li>Biblioteca de prompts por área</li><li>Exercícios e desafio de 7 dias</li></ul><p class="fine" style="margin-top:12px">Preço de lançamento: <strong>R$19,90</strong></p></article>
<article class="card"><h3>Programa Completo</h3><p>Uma jornada de aplicação prática de IA: do primeiro pedido bem feito a fluxos de trabalho com IA.</p><ul class="chk" style="margin-top:12px"><li>Curso Básico + Curso Avançado</li><li>Assistentes configurados e fluxos de trabalho</li><li>Análise com conferência e automações sem código</li></ul><p class="fine" style="margin-top:12px">Preço de lançamento: <strong>R$149,90</strong></p></article>
</div>
<p class="note">Os treinamentos estão em produção e ainda não estão à venda. Acompanhe a SargLab no Instagram para saber quando as inscrições abrirem. <a style="color:var(--brand);text-decoration:underline" href="{INSTA}" target="_blank" rel="noopener noreferrer">Seguir @sarglab.ia no Instagram &rarr;</a></p>
</div></section>

<section class="sec alt"><div class="container"><div class="band on-dark"><div><div class="eyebrow">Uso responsável</div><h2>IA ajuda. A responsabilidade continua sendo sua.</h2><p>Confira informações importantes antes de usar uma resposta e evite inserir dados pessoais, credenciais ou informações confidenciais em ferramentas públicas de IA.</p></div><a class="btn btn-p" href="#baixar">Baixar o guia {ARROW}</a></div></div></section>
''')

# ------------------------------------------------------------------ CURSOS
INT_OPTS = ['<option value="" disabled selected>Selecione</option>', '<option value="sarglab-curso-basico">Curso Básico</option>', '<option value="sarglab-programa-completo">Programa Completo</option>', '<option value="sarglab-geral">Ainda não sei</option>']
pages["/sarglab/cursos/"] = page("/sarglab/cursos/", "Treinamentos SargLab | Curso Básico e Programa Completo",
  "Conheça os treinamentos do SargLab em produção: Curso Básico e Programa Completo. Ainda não estão à venda; deixe seu contato para ser avisado.",
  f'''
<section class="hero sub"><div class="container hero-in on-dark">
<div style="max-width:760px"><div class="eyebrow">SargLab &middot; em produção</div><h1>Treinamentos SargLab.</h1>
<p class="lead">Do primeiro pedido bem feito a fluxos de trabalho com IA. Os treinamentos estão em produção e ainda não estão à venda.</p></div>
</div></section>

<section class="sec"><div class="container"><div class="grid g2">
<article class="card" id="basico"><span class="tag">Em produção</span><h3>Curso Básico</h3><p>Aprenda a estruturar pedidos, comparar resultados, corrigir respostas e transformar o Método CLARO em rotina de trabalho.</p><ul class="chk" style="margin-top:12px"><li>Demonstrações reais em vídeo</li><li>Biblioteca de prompts por área</li><li>Exercícios e desafio de 7 dias</li></ul><p class="fine" style="margin-top:14px">Preço de lançamento: <strong>R$19,90</strong>. Vendas ainda não abertas.</p></article>
<article class="card" id="completo"><span class="tag">Em produção</span><h3>Programa Completo</h3><p>Uma jornada de aplicação prática de IA: do primeiro pedido bem feito a fluxos de trabalho com IA.</p><ul class="chk" style="margin-top:12px"><li>Curso Básico + Curso Avançado</li><li>Assistentes configurados e fluxos de trabalho</li><li>Análise com conferência e automações sem código</li></ul><p class="fine" style="margin-top:14px">Preço de lançamento: <strong>R$149,90</strong>. Vendas ainda não abertas.</p></article>
</div>
<p class="note">As vendas abrem quando a oferta estiver validada e o pagamento, homologado. Até lá, deixe seu contato e avisamos.</p>
</div></section>

<section class="sec alt"><div class="container">
<div class="sec-head"><div class="eyebrow">Como funciona</div><h2 class="h2">Da compra ao estudo (quando abrir).</h2></div>
<div class="flow" style="--n:5"><div>Escolha<small>Curso Básico ou Programa Completo</small></div><div>Pagamento<small>Processado pelo Mercado Pago</small></div><div>Confirmação<small>Feita pelo servidor, não pelo navegador</small></div><div>Matrícula<small>Criada automaticamente</small></div><div>Área do aluno<small>Acesso ao que foi adquirido</small></div></div>
<p style="margin-top:28px"><a class="btn btn-o" href="{LOGIN}" rel="noopener">Já sou aluno: acessar plataforma</a></p>
</div></section>

<section class="sec" id="aviso"><div class="container"><div class="grid g2" style="align-items:start">
<div><div class="eyebrow">Lista de aviso</div><h2 class="h2">Quero ser avisado.</h2><p class="lead">Informe seu contato e o seu interesse. Avisamos quando as inscrições abrirem. Não enviamos nada além disso.</p></div>
<form class="form" data-kind="contact" data-origem="sarglab-cursos-aviso" data-success="Recebido. Avisaremos você quando as inscrições abrirem.">
<h3>Receber o aviso</h3>{HONEY}
<div class="f2"><label>Nome *<input name="nome" required maxlength="100" autocomplete="name"></label><label>E-mail *<input name="email" type="email" required maxlength="200" autocomplete="email"></label></div>
<label>Interesse *<select name="interesse" required>{"".join(INT_OPTS)}</select></label>
<input type="hidden" name="assunto" value="SargLab: aviso de abertura">
<input type="hidden" name="mensagem" value="Quero ser avisado quando as inscrições do SargLab abrirem.">
{consent()}
<button class="btn btn-p" type="submit">Quero ser avisado {ARROW}</button><p class="status" role="status" aria-live="polite"></p>
</form></div></div></section>
''')

# ------------------------------------------------------------------ CONTATO
ASSUNTOS = ["Sistema ou aplicação web", "CRM e gestão comercial", "Automação de processos", "Dados e analytics", "IA aplicada", "SargLab", "Outro assunto"]
pages["/contato/"] = page("/contato/", "Fale com a SARGTECH | Contato",
  "Conte o contexto do seu desafio. A primeira conversa com a SARGTECH serve para entender a necessidade e avaliar possibilidades.",
  f'''
<section class="hero sub"><div class="container hero-in on-dark"><div style="max-width:760px"><div class="eyebrow">Contato</div><h1>Fale com a SARGTECH.</h1><p class="lead">Precisa organizar um processo, desenvolver um sistema ou avaliar uma solução com dados e IA? Conte o contexto.</p></div></div></section>
<section class="sec"><div class="container"><div class="grid g2" style="align-items:start">
<div><h2 class="h2">A primeira conversa é para entender.</h2>
<ul class="chk"><li>Entendemos o contexto antes de propor qualquer solução.</li><li>Escopo, possibilidades e próximos passos com clareza.</li><li>Sem promessas genéricas.</li></ul>
<p style="margin-top:28px" class="fine">Prefere escrever direto? <a style="color:var(--brand);text-decoration:underline" href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a style="color:var(--brand);text-decoration:underline" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a></p></div>
<form class="form" data-kind="contact" data-origem="site-contato" data-success="Mensagem recebida. Responderemos pelo contato informado.">
<h3>Vamos entender o seu desafio.</h3>{HONEY}
<div class="f2"><label>Nome *<input name="nome" required maxlength="100" autocomplete="name"></label><label>E-mail *<input name="email" type="email" required maxlength="200" autocomplete="email"></label></div>
<div class="f2"><label>Empresa <small>(opcional)</small><input name="empresa" maxlength="120" autocomplete="organization"></label><label>Telefone <small>(opcional)</small><input name="telefone" type="tel" maxlength="30" autocomplete="tel" inputmode="tel"></label></div>
<label>Assunto *<select name="assunto" required><option value="" disabled selected>Selecione</option>{"".join(f"<option>{a}</option>" for a in ASSUNTOS)}</select></label>
<label>Mensagem *<textarea name="mensagem" required minlength="10" maxlength="2500" placeholder="Descreva brevemente o desafio."></textarea></label>
{consent()}
<button class="btn btn-p" type="submit">Enviar mensagem {ARROW}</button><p class="status" role="status" aria-live="polite"></p>
</form></div></div></section>
''')

# ------------------------------------------------------------------ PRIVACIDADE e TERMOS (textos aprovados da landing atual, 07/10/2026)
PRIV_HTML = '\n    <div class="eyebrow">Privacidade e dados</div>\n\n    <h1 class="h2">Política de Privacidade</h1>\n\n    <p class="lead">\n      Esta Política de Privacidade explica como a SARGTECH,\n      por meio da SargLab, coleta e utiliza informações\n      fornecidas por pessoas que acessam nossos materiais,\n      páginas e formulários.\n    </p>\n\n    <section>\n      <h2>1. Quais dados podemos coletar</h2>\n\n      <p>\n        Ao preencher formulários da SargLab, podemos solicitar\n        informações como:\n      </p>\n\n      <ul>\n        <li>nome;</li>\n        <li>endereço de e-mail;</li>\n        <li>WhatsApp, quando informado voluntariamente;</li>\n        <li>área profissional;</li>\n        <li>origem do acesso e campanha relacionada;</li>\n        <li>\n          registros relacionados ao consentimento fornecido\n          no formulário.\n        </li>\n      </ul>\n    </section>\n\n    <section>\n      <h2>2. Para que utilizamos esses dados</h2>\n\n      <p>\n        As informações coletadas podem ser utilizadas para:\n      </p>\n\n      <ul>\n        <li>\n          fornecer o material solicitado, como e-books,\n          guias e outros conteúdos;\n        </li>\n\n        <li>\n          registrar e organizar o relacionamento com\n          interessados nos produtos e serviços da SargLab;\n        </li>\n\n        <li>\n          enviar comunicações relacionadas a conteúdos,\n          produtos, serviços e atividades da SargLab;\n        </li>\n\n        <li>\n          entender de onde vêm nossos acessos e melhorar\n          nossos conteúdos e páginas;\n        </li>\n\n        <li>\n          responder solicitações enviadas pelos usuários.\n        </li>\n      </ul>\n    </section>\n\n    <section>\n      <h2>3. WhatsApp</h2>\n\n      <p>\n        O fornecimento do número de WhatsApp é opcional,\n        salvo quando indicado de forma diferente em alguma\n        atividade específica.\n      </p>\n\n      <p>\n        Quando fornecido, ele poderá ser utilizado para\n        comunicações relacionadas à SargLab e ao interesse\n        demonstrado pelo usuário.\n      </p>\n    </section>\n\n    <section>\n      <h2>4. Comunicações</h2>\n\n      <p>\n        Ao aceitar o campo de consentimento presente em nossos\n        formulários, o usuário autoriza o recebimento de\n        comunicações relacionadas à SargLab.\n      </p>\n\n      <p>\n        O usuário poderá solicitar a interrupção dessas\n        comunicações a qualquer momento.\n      </p>\n    </section>\n\n    <section>\n      <h2>5. Compartilhamento de informações</h2>\n\n      <p>\n        A SargLab não pretende comercializar dados pessoais\n        coletados por meio de seus formulários.\n      </p>\n\n      <p>\n        Informações poderão ser processadas por ferramentas\n        técnicas necessárias ao funcionamento dos serviços,\n        como hospedagem, banco de dados, CRM, envio de\n        comunicações e processamento de pagamentos,\n        quando aplicável.\n      </p>\n    </section>\n\n    <section>\n      <h2>6. Armazenamento e segurança</h2>\n\n      <p>\n        Adotamos medidas razoáveis de organização e segurança\n        para reduzir riscos de acesso não autorizado,\n        alteração, perda ou divulgação indevida das\n        informações armazenadas.\n      </p>\n\n      <p>\n        Nenhum sistema conectado à internet pode oferecer\n        garantia absoluta de segurança.\n      </p>\n    </section>\n\n    <section>\n      <h2>7. Cookies, origem e campanhas</h2>\n\n      <p>\n        Nossas páginas poderão utilizar informações técnicas,\n        parâmetros de URL e identificadores de campanha,\n        como UTMs, para compreender a origem dos acessos e\n        avaliar o desempenho de nossas iniciativas.\n      </p>\n\n      <p>\n        Caso ferramentas de análise ou publicidade que\n        utilizem cookies sejam adicionadas futuramente,\n        esta Política poderá ser atualizada para refletir\n        essas práticas.\n      </p>\n    </section>\n\n    <section>\n      <h2>8. Solicitação de acesso, correção ou exclusão</h2>\n\n      <p>\n        O usuário pode entrar em contato para solicitar\n        informações sobre seus dados, corrigir informações\n        ou solicitar sua exclusão, quando aplicável.\n      </p>\n\n      <p>\n        O contato oficial para questões relacionadas a\n        privacidade é:\n      </p>\n\n      <p>\n        <strong>\n          <a href="mailto:SARGrowth@proton.me">\n            SARGrowth@proton.me\n          </a>\n        </strong>\n      </p>\n    </section>\n\n    <section>\n      <h2>9. Links externos</h2>\n\n      <p>\n        Nossos conteúdos podem conter links para plataformas\n        ou serviços de terceiros.\n      </p>\n\n      <p>\n        A utilização desses serviços está sujeita às\n        respectivas políticas e condições dos responsáveis\n        por essas plataformas.\n      </p>\n    </section>\n\n    <section>\n      <h2>10. Alterações nesta Política</h2>\n\n      <p>\n        Esta Política poderá ser atualizada à medida que\n        novos recursos, serviços ou ferramentas sejam\n        incorporados à SargLab.\n      </p>\n\n      <p>\n        A versão publicada nesta página será considerada a\n        versão vigente.\n      </p>\n    </section>\n\n    <p class="fine" style="margin-top:28px">\n      <strong>Última atualização:</strong>\n      7 de outubro de 2026.\n    </p>\n  '
TERMOS_HTML = '\n    <div class="eyebrow">Condições de uso</div>\n\n    <h1 class="h2">Termos de Uso</h1>\n\n    <p class="lead">\n      Estes Termos estabelecem as condições gerais de uso das páginas,\n      materiais, conteúdos e serviços disponibilizados pela SargLab,\n      um produto SARGTECH.\n    </p>\n\n    <section>\n      <h2>1. Aceitação dos termos</h2>\n\n      <p>\n        Ao acessar as páginas da SargLab, baixar materiais ou utilizar\n        seus conteúdos, o usuário declara estar de acordo com estes Termos\n        de Uso.\n      </p>\n    </section>\n\n    <section>\n      <h2>2. Conteúdo educacional e informativo</h2>\n\n      <p>\n        Os materiais disponibilizados pela SargLab têm finalidade\n        educacional e informativa.\n      </p>\n\n      <p>\n        O conteúdo não substitui avaliação profissional, jurídica,\n        financeira, médica ou técnica especializada quando necessária.\n      </p>\n    </section>\n\n    <section>\n      <h2>3. Uso de Inteligência Artificial</h2>\n\n      <p>\n        Ferramentas de Inteligência Artificial podem produzir respostas\n        imprecisas, incompletas ou inadequadas ao contexto.\n      </p>\n\n      <p>\n        O usuário é responsável por revisar, validar e adaptar qualquer\n        conteúdo gerado por ferramentas de IA antes de utilizá-lo em\n        situações reais.\n      </p>\n    </section>\n\n    <section>\n      <h2>4. Responsabilidade sobre informações compartilhadas</h2>\n\n      <p>\n        O usuário deve evitar inserir em ferramentas públicas de IA\n        informações confidenciais, credenciais, dados pessoais sensíveis\n        ou conteúdos cuja divulgação possa causar riscos.\n      </p>\n    </section>\n\n    <section>\n      <h2>5. Propriedade intelectual</h2>\n\n      <p>\n        Os materiais produzidos pela SargLab, incluindo textos, métodos,\n        apresentações, modelos, guias e identidade visual, são destinados\n        ao uso conforme as condições apresentadas em cada material.\n      </p>\n\n      <p>\n        Não é permitida a reprodução integral para revenda, redistribuição\n        comercial ou apresentação como criação própria sem autorização.\n      </p>\n    </section>\n\n    <section>\n      <h2>6. Materiais gratuitos</h2>\n\n      <p>\n        Materiais gratuitos podem ser utilizados pelo usuário para fins\n        pessoais e profissionais próprios.\n      </p>\n\n      <p>\n        A disponibilização gratuita não implica transferência de autoria\n        ou de direitos sobre o conteúdo.\n      </p>\n    </section>\n\n    <section>\n      <h2>7. Produtos e serviços pagos</h2>\n\n      <p>\n        Produtos ou serviços pagos poderão possuir condições específicas\n        de acesso, pagamento, entrega, cancelamento ou reembolso.\n      </p>\n\n      <p>\n        Essas condições serão apresentadas no momento da contratação ou\n        na página correspondente ao produto.\n      </p>\n    </section>\n\n    <section>\n      <h2>8. Disponibilidade dos serviços</h2>\n\n      <p>\n        A SargLab pode atualizar, alterar, interromper ou substituir\n        conteúdos e recursos quando necessário.\n      </p>\n\n      <p>\n        Não é garantida disponibilidade ininterrupta de páginas,\n        servidores ou serviços externos utilizados pela operação.\n      </p>\n    </section>\n\n    <section>\n      <h2>9. Links e serviços de terceiros</h2>\n\n      <p>\n        Algumas funcionalidades podem depender de serviços externos,\n        como hospedagem, pagamento, banco de dados ou outras plataformas.\n      </p>\n\n      <p>\n        O uso desses serviços pode estar sujeito a termos próprios dos\n        respectivos fornecedores.\n      </p>\n    </section>\n\n    <section>\n      <h2>10. Privacidade</h2>\n\n      <p>\n        O tratamento de dados pessoais relacionados às páginas e\n        formulários da SargLab é descrito na\n        <a href="/privacidade/">\n          Política de Privacidade\n        </a>.\n      </p>\n    </section>\n\n    <section>\n      <h2>11. Contato</h2>\n\n      <p>\n        Dúvidas relacionadas a estes Termos podem ser encaminhadas para:\n      </p>\n\n      <p>\n        <strong>\n          <a href="mailto:SARGrowth@proton.me">\n            SARGrowth@proton.me\n          </a>\n        </strong>\n      </p>\n    </section>\n\n    <section>\n      <h2>12. Atualizações</h2>\n\n      <p>\n        Estes Termos poderão ser atualizados para acompanhar mudanças\n        nos produtos, serviços ou funcionamento da SargLab.\n      </p>\n\n      <p>\n        A versão publicada nesta página será considerada a versão vigente.\n      </p>\n    </section>\n\n    <p class="fine" style="margin-top:28px">\n      <strong>Última atualização:</strong>\n      7 de outubro de 2026.\n    </p>\n  '
pages["/privacidade/"] = page("/privacidade/", "Política de Privacidade | SARGTECH / SargLab",
  "Como a SARGTECH, por meio da SargLab, coleta e utiliza informações fornecidas em materiais, páginas e formulários.",
  '<section class="sec"><div class="container prose" style="max-width:780px">' + PRIV_HTML + '</div></section>')
pages["/termos/"] = page("/termos/", "Termos de Uso | SARGTECH / SargLab",
  "Condições gerais de uso das páginas, materiais, conteúdos e serviços da SargLab, um produto SARGTECH.",
  '<section class="sec"><div class="container prose" style="max-width:780px">' + TERMOS_HTML + '</div></section>')

# ------------------------------------------------------------------ 404
pages["/404.html"] = page("/404.html", "Página não encontrada | SARGTECH", "Página não encontrada.",
  f'<section class="sec"><div class="container" style="max-width:640px;text-align:center"><div class="eyebrow" style="justify-content:center">Erro 404</div><h1 class="h2">Não encontramos esta página.</h1><p class="lead" style="margin-inline:auto">O endereço pode ter mudado. Volte ao início ou fale com a gente.</p><p style="margin-top:24px"><a class="btn btn-p" href="/">Voltar ao início</a></p></div></section>', noindex=True)

# ------------------------------------------------------------------ escrita
if os.path.isdir(DIST):
    shutil.rmtree(DIST)
os.makedirs(os.path.join(DIST, "assets"))
for path, content in pages.items():
    out = os.path.join(DIST, path.lstrip("/")) if path.endswith(".html") else os.path.join(DIST, path.lstrip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(content)
os.makedirs(os.path.join(DIST, "assets", "downloads"), exist_ok=True)
shutil.copy(os.path.join(SRC, "downloads", "sarglab-ia-para-quem-tem-trabalho-pra-fazer.pdf"), os.path.join(DIST, "assets", "downloads"))
shutil.copy(os.path.join(SRC, "capa-ebook-sarglab.webp"), os.path.join(DIST, "assets", "capa-ebook-sarglab.webp"))
shutil.copy(os.path.join(SRC, "og-image.png"), os.path.join(DIST, "assets", "og-image.png"))
shutil.copy(os.path.join(SRC, "site.css"), os.path.join(DIST, "assets", "site.css"))
shutil.copy(os.path.join(SRC, "site.js"), os.path.join(DIST, "assets", "site.js"))
shutil.copy(os.path.join(SRC, "config.js"), os.path.join(DIST, "assets", "config.js"))
open(os.path.join(DIST, "favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0F1C2E"/><text x="32" y="46" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-weight="800" font-size="40" fill="#5B86F0">S</text></svg>')
urls = [p for p in pages if p not in ("/404.html","/privacidade/","/termos/")] + ["/privacidade/","/termos/"]
open(os.path.join(DIST, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(DIST, "_headers"), "w").write("""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' https://api.sargtech.com.br; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
/assets/*
  Cache-Control: public, max-age=3600
""")
print("ok:", sorted(pages))

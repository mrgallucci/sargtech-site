(function () {
  "use strict";
  var C = window.SARGTECH_CONFIG || {};
  function safe(fn, fb) { try { return fn(); } catch (e) { return fb; } }

  var BR_MOBILE_DDDS = {
    "11":1,"12":1,"13":1,"14":1,"15":1,"16":1,"17":1,"18":1,"19":1,
    "21":1,"22":1,"24":1,"27":1,"28":1,
    "31":1,"32":1,"33":1,"34":1,"35":1,"37":1,"38":1,
    "41":1,"42":1,"43":1,"44":1,"45":1,"46":1,"47":1,"48":1,"49":1,
    "51":1,"53":1,"54":1,"55":1,
    "61":1,"62":1,"63":1,"64":1,"65":1,"66":1,"67":1,"68":1,"69":1,
    "71":1,"73":1,"74":1,"75":1,"77":1,"79":1,
    "81":1,"82":1,"83":1,"84":1,"85":1,"86":1,"87":1,"88":1,"89":1,
    "91":1,"92":1,"93":1,"94":1,"95":1,"96":1,"97":1,"98":1,"99":1
  };
  function normalizeBrWhatsapp(value) {
    var digits = (value || "").replace(/\D/g, "");
    if (digits.length === 13 && digits.slice(0, 2) === "55") digits = digits.slice(2);
    if (digits.length !== 11 || !BR_MOBILE_DDDS[digits.slice(0, 2)] || digits.charAt(2) !== "9") return null;
    return "+55" + digits;
  }

  function validContactEmail(value) {
    var email = (value || "").trim();
    return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) && email.length <= 255;
  }

  /* Menu móvel */
  var hd = document.querySelector(".hd"), bt = document.querySelector(".burger");
  if (hd && bt) {
    bt.addEventListener("click", function () {
      var o = hd.classList.toggle("open");
      bt.setAttribute("aria-expanded", String(o));
      bt.setAttribute("aria-label", o ? "Fechar menu" : "Abrir menu");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && hd.classList.contains("open")) { bt.click(); bt.focus(); }
    });
  }
  var y = document.getElementById("year"); if (y) y.textContent = new Date().getFullYear();

  /* Atribuição: utm_*, referrer e URL da landing (guardados para as próximas páginas da visita) */
  var KEY = "sargtech_attr_v1", UTM = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];
  function attribution() {
    var stored = safe(function () { return JSON.parse(sessionStorage.getItem(KEY) || "null"); }, null) || {};
    var qs = new URLSearchParams(window.location.search), cur = {}, has = false;
    UTM.forEach(function (k) { var v = qs.get(k); if (v) { cur[k] = v.slice(0, 200); has = true; } });
    if (has) {
      stored = Object.assign({}, cur, { referrer: (document.referrer || "").slice(0, 500), landing_url: window.location.href.slice(0, 500) });
    } else if (!stored.landing_url) {
      stored.referrer = (document.referrer || "").slice(0, 500);
      stored.landing_url = window.location.href.slice(0, 500);
    }
    safe(function () { sessionStorage.setItem(KEY, JSON.stringify(stored)); });
    return stored;
  }
  var ATTR = attribution();

  /* O WhatsApp é obrigatório na captação do e-book. Mantemos esta regra também
     no JS para a página gerada permanecer correta mesmo antes de regenerar o HTML. */
  document.querySelectorAll('form[data-kind="ebook"]').forEach(function (form) {
    var wa = form.elements.whatsapp;
    if (!wa) return;
    wa.required = true;
    wa.setAttribute("aria-required", "true");
    var label = wa.closest("label");
    if (label) {
      var optional = label.querySelector("small");
      if (optional && /opcional/i.test(optional.textContent || "")) optional.remove();
      if ((label.firstChild && label.firstChild.nodeType === 3) && label.firstChild.textContent.indexOf("*") === -1) {
        label.firstChild.textContent = "WhatsApp *";
      }
    }
  });

  /* Origem do tráfego (mesma regra da landing atual do e-book): utm_source, senão domínio do referrer, senão "direto". */
  function trafficSource() {
    var us = new URLSearchParams(window.location.search).get("utm_source") || ATTR.utm_source;
    if (us) return us.trim().toLowerCase().slice(0, 100);
    var ref = ATTR.referrer || "";
    if (!ref) return "direto";
    try {
      var h = new URL(ref).hostname.toLowerCase();
      var known = ["instagram", "linkedin", "facebook", "google"];
      for (var i = 0; i < known.length; i++) if (h.indexOf(known[i]) !== -1) return known[i];
      return h.slice(0, 100);
    } catch (e) { return "referencia"; }
  }

  /* Formulários -> API SARGTECH (contrato real: /api/public/leads/ebook e /contact) */
  var CONSENT_VERSION = "site-2026-10-13";
  document.querySelectorAll("form[data-kind]").forEach(function (form) {
    var status = form.querySelector(".status"), btn = form.querySelector("button[type=submit]");
    var label = btn.textContent;
    function say(msg, cls) { status.textContent = msg; status.className = "status " + (cls || ""); }
    function field(n) { var el = form.elements[n]; return el && typeof el.value === "string" ? el.value.trim() : ""; }
    function success() {
      form.reset();
      say(form.dataset.success || "Recebido. Obrigado!", "ok");
      document.dispatchEvent(new CustomEvent("sargtech:lead", { detail: { kind: form.dataset.kind } }));
    }
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;
      if (field("website")) { say("Recebido.", "ok"); return; } /* honeypot */
      var kind = form.dataset.kind, data;
      var common = {
        utm_source: ATTR.utm_source || null, utm_medium: ATTR.utm_medium || null, utm_campaign: ATTR.utm_campaign || null,
        utm_content: ATTR.utm_content || null, utm_term: ATTR.utm_term || null,
        referrer: ATTR.referrer || null, landing_url: ATTR.landing_url || null,
        pagina: window.location.pathname, consentimento_versao: CONSENT_VERSION,
        consentimento: form.elements.consentimento.checked === true
      };
      if (kind === "ebook" || kind === "ebook-instagram") {
        var email = field("email").toLowerCase();
        if (!validContactEmail(email)) {
          say("Informe um e-mail válido, por exemplo nome@empresa.com.br.", "err");
          form.elements.email.focus();
          return;
        }
        var wa = normalizeBrWhatsapp(field("whatsapp"));
        if (!wa) {
          say("Informe um WhatsApp brasileiro válido com DDD.", "err");
          form.elements.whatsapp.focus();
          return;
        }
        data = Object.assign({ nome: field("nome"), email: email, whatsapp: wa,
          area_profissional: field("area_profissional"), origem: trafficSource() }, common);
      } else {
        data = Object.assign({ nome: field("nome"), email: field("email").toLowerCase(), empresa: field("empresa") || null,
          telefone: field("telefone") || null, assunto: field("assunto"), mensagem: field("mensagem"),
          interesse: field("interesse") || null, origem: form.dataset.origem || "site-contato" }, common);
      }
      var ep = (C.endpoints || {})[kind];
      if (!C.apiBase || !ep) { say("Envio indisponível no momento. Escreva para " + C.contactEmail + ".", "err"); return; }
      btn.disabled = true; btn.textContent = "Enviando..."; say("Registrando seu envio...", "");
      var ctl = new AbortController(), t = setTimeout(function () { ctl.abort(); }, 15000);
      fetch(C.apiBase + ep, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data), signal: ctl.signal, credentials: "omit" })
        .then(function (r) {
          clearTimeout(t);
          if (r.ok || r.status === 409) { success(); return; }  /* 409: contato já existente, não impede o download */
          if (r.status === 429) { say("Muitas tentativas. Aguarde um instante e tente de novo.", "err"); return; }
          if (r.status === 400 || r.status === 422) {
            return r.json().then(function (j) { say(typeof j.detail === "string" ? j.detail : "Confira os campos e tente novamente.", "err"); },
              function () { say("Confira os campos e tente novamente.", "err"); });
          }
          say("Não foi possível enviar agora. Tente de novo ou escreva para " + C.contactEmail + ".", "err");
        })
        .catch(function () { clearTimeout(t); say("Sem conexão com o servidor. Tente de novo ou escreva para " + C.contactEmail + ".", "err"); })
        .then(function () { btn.disabled = false; btn.textContent = label; });
    });
  });

  /* Pré-seleciona o interesse via ?interesse= */
  var q = new URLSearchParams(window.location.search).get("interesse");
  if (q) document.querySelectorAll("select[name=interesse]").forEach(function (s) {
    Array.prototype.forEach.call(s.options, function (o) { if (o.value === q) s.value = q; });
  });
})();

/* Configuração pública do site. Sem segredos: nada aqui é confidencial. */
window.SARGTECH_CONFIG = {
  apiBase: "https://api.sargtech.com.br",
  /* Contrato real da API (repositório gestao-inteligente-starter, backend/main.py). */
  endpoints: {
    ebook: "/api/public/leads/ebook",
    "ebook-instagram": "/api/public/leads/ebook/instagram",
    contact: "/api/public/leads/contact"
  },
  contactEmail: "SARGrowth@proton.me"
};

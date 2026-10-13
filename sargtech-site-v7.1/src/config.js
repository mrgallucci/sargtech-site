/* Configuração pública do site. Sem segredos: nada aqui é confidencial. */
window.SARGTECH_CONFIG = {
  apiBase: "https://api.sargtech.com.br",
  /* Contrato real da API (repositório gestao-inteligente-starter, backend/main.py). */
  endpoints: {
    ebook: "/api/public/leads/ebook",
    contact: "/api/public/leads/contact"
  },
  ebookDownloadUrl: "/assets/downloads/sarglab-ia-para-quem-tem-trabalho-pra-fazer.pdf",
  contactEmail: "SARGrowth@proton.me"
};

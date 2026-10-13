# Fluxo pagamento → matrícula → acesso

```
Produto SargLab → Comprar → API cria pedido (pending, preço do banco)
→ Mercado Pago (checkout) → pagamento
→ webhook → API valida assinatura e BUSCA o pagamento na API do MP
→ atualiza pedido → (approved) cria/habilita usuário ALUNO → cria matrícula do produto
→ libera os módulos daquele produto
```
Regras:
1. **Nunca liberar por redirecionamento do navegador.** A página de retorno só mostra "processando".
2. **Webhook:** validar a assinatura (`x-signature`) com `MP_WEBHOOK_SECRET`; não confiar no corpo — consultar o pagamento pela API do Mercado Pago usando o token do servidor e conferir valor, moeda e `external_reference` (id público do pedido).
3. **Idempotência:** `payment_events` tem `unique(mp_payment_id, mp_status)`; `enrollments` tem `unique(user_id, product_id)`. Reentrega do mesmo webhook não duplica nada (testado).
4. **Status:** pending/in_process → nada liberado; approved → matrícula; rejected/cancelled → nada; refunded/charged_back → matrícula `suspended`. Evento atrasado não rebaixa pedido já aprovado (testado).
5. **Produto completo x módulo:** `product_modules` liga produto a módulos. Quem compra só o módulo 2 acessa só o módulo 2 (testado).
6. **Aluno x matrícula:** `role=aluno` não dá acesso a conteúdo. O acesso é a função `can_access_module` (matrícula ativa que contenha o módulo) e deve ser chamada em **todo endpoint** de conteúdo.
7. **Contato existente:** o comprador é casado por e-mail (sem diferenciar maiúsculas); o contato do CRM é atualizado, não duplicado.
8. **Jornada do lead** (Instagram/Ads → landing → e-book → lead → interesse → checkout → pagamento → cliente → aluno → matrícula → consumo → progresso): guardar `utm_*`, `referrer` e `landing_url` no lead e copiá-los para o pedido; registrar cada etapa como evento do contato.
9. Antes de cobrar: resolver a questão do CNPJ/recebimento (ver relatório) e os preços aprovados.

Arquivos: `backend-reference/001_sargtech_commerce.sql`, `commerce.py`, `test_commerce.py` (`python3 test_commerce.py`).

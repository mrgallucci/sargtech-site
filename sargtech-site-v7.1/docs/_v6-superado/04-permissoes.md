# Checklist de permissões (a executar no repositório do CRM/API)
A regra deve ser aplicada **no servidor**. Esconder menu não conta.

Teste cada linha com os 3 perfis, chamando a API direto (curl/Postman) com o token de cada um. Esperado: 401 sem token; 403 com perfil sem permissão.

| Área / endpoint | admin | vendedor | aluno |
|---|---|---|---|
| Leads (listar, ver, editar, exportar) | permitido | só o autorizado ao papel | **403** |
| Funil e vendas | permitido | conforme papel | **403** |
| Financeiro administrativo | permitido | **403** (salvo regra definida) | **403** |
| Campanhas e Analytics internos | permitido | conforme papel | **403** |
| Cadastro e edição de usuários | permitido | **403** | **403** |
| Pedidos/matrículas de outros | permitido | conforme papel | **403** |
| Meus cursos / módulos / aulas / materiais | opcional | **403** salvo matrícula | **só os cursos/módulos com matrícula ativa** |
| Progresso e presença | permitido | **403** | **só os próprios** |
| Conta/perfil | próprio | próprio | próprio |

Checagens obrigatórias:
- [ ] Aluno sem matrícula no módulo recebe 403 ao chamar o endpoint da aula/arquivo, mesmo com URL conhecida.
- [ ] Aluno com módulo avulso não acessa os demais módulos.
- [ ] Aluno não acessa dados de outro aluno (troca de id na URL).
- [ ] Matrícula `suspended` (estorno) perde o acesso.
- [ ] Rotas do frontend (Next.js) redirecionam por perfil, mas o backend é a fonte da verdade.
- [ ] Token expirado e logout invalidam acesso; cookies com `HttpOnly`, `Secure`, `SameSite`.
- [ ] Mesma tela de login para os 3 perfis; redirecionamento pós-login conforme o papel.

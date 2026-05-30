# Relatório TDD

## Cenário Escolhido

Sistema de Autenticação de Usuários.

## O que é TDD?

TDD (Test-Driven Development), ou Desenvolvimento Orientado a Testes, é uma metodologia de desenvolvimento de software baseada na criação de testes antes da implementação das funcionalidades.

O objetivo é garantir que cada funcionalidade seja desenvolvida de forma incremental, validada automaticamente e com menor possibilidade de erros.

O TDD segue obrigatoriamente o ciclo:

RED → GREEN → REFACTOR

---

## RED

Nesta etapa é criado um teste para uma funcionalidade que ainda não existe ou que ainda não foi implementada completamente.

O resultado esperado é que o teste falhe, demonstrando que a funcionalidade precisa ser desenvolvida.

Exemplo:

- Criar um teste para login válido.
- Executar o pytest.
- O teste falha porque o método ainda não existe.

Objetivo: identificar claramente o comportamento esperado do sistema.

---

## GREEN

Após a falha do teste, é implementado o mínimo de código necessário para fazê-lo passar.

Nesta fase não há preocupação com otimização ou organização avançada do código, apenas com o funcionamento correto da funcionalidade.

Exemplo:

- Implementar o método de login.
- Executar novamente o pytest.
- O teste passa com sucesso.

Objetivo: fazer o teste passar com a menor implementação possível.

---

## REFACTOR

Com todos os testes passando, o código pode ser melhorado sem alterar seu comportamento.

Nesta etapa podem ser realizadas:

- Melhorias de legibilidade;
- Remoção de duplicações;
- Organização de métodos;
- Melhorias de nomenclatura;
- Aplicação de boas práticas.

Após qualquer alteração, os testes devem continuar passando.

Objetivo: melhorar a qualidade do código mantendo o funcionamento correto.

---

## Funcionalidades Implementadas

- Cadastro de usuário;
- Login;
- Redefinição de senha.

---

## Regras de Negócio

- Senha mínima de 6 caracteres;
- Usuário duplicado não permitido.

---

## Testes Implementados

### Login válido

Verifica se um usuário cadastrado consegue acessar o sistema utilizando usuário e senha corretos.

### Usuário duplicado

Verifica se o sistema impede o cadastro de um usuário já existente.

### Senha muito curta

Verifica se o sistema bloqueia senhas com menos de 6 caracteres.

### Senha incorreta

Verifica se o login é negado quando a senha informada está incorreta.

### Usuário inexistente

Verifica se o sistema nega acesso a usuários que não estão cadastrados.

### Redefinição de senha

Verifica se um usuário consegue alterar sua senha e utilizá-la posteriormente para realizar login.

---

## Aplicação do Ciclo TDD

### RED

Foram criados inicialmente os testes para:

- Login válido;
- Usuário duplicado;
- Senha mínima;
- Senha incorreta;
- Usuário inexistente;
- Redefinição de senha.

Os testes falharam inicialmente porque as funcionalidades ainda não estavam implementadas.

### GREEN

As funcionalidades foram implementadas gradualmente até que todos os testes passassem com sucesso.

### REFACTOR

Após a aprovação dos testes, o código foi revisado e organizado sem alterar seu comportamento, mantendo todos os testes aprovados.

---

## Resultado Final

Comando executado:

```bash
pytest -v
```

Resultado esperado:

```text
============================= test session starts =============================
...
collected 6 items

test_autenticacao.py::test_login_valido PASSED
test_autenticacao.py::test_usuario_duplicado PASSED
test_autenticacao.py::test_senha_muito_curta PASSED
test_autenticacao.py::test_senha_incorreta PASSED
test_autenticacao.py::test_usuario_inexistente PASSED
test_autenticacao.py::test_redefinir_senha PASSED

============================== 6 passed ==============================
```

## Conclusão

A metodologia TDD permitiu desenvolver o sistema de autenticação de forma incremental e segura. Cada funcionalidade foi criada a partir de testes automatizados, garantindo que as regras de negócio fossem atendidas e facilitando futuras manutenções no sistema.

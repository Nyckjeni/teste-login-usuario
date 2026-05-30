# Relatório TDD

## Cenário Escolhido
Sistema de Autenticação de Usuários.

## Funcionalidades Implementadas

- Cadastro de usuário
- Login
- Redefinição de senha

## Regras de Negócio

- Senha mínima de 6 caracteres
- Usuário duplicado não permitido

## Ciclo RED → GREEN → REFACTOR

### RED
Foram criados testes para:
- Login válido
- Usuário duplicado
- Senha mínima
- Senha incorreta
- Usuário inexistente
- Redefinição de senha

### GREEN
Foi implementado apenas o código necessário para cada teste passar.

### REFACTOR
O código foi reorganizado mantendo todos os testes aprovados.

## Resultado Final

Comando executado:

pytest -v

Resultado:

6 passed
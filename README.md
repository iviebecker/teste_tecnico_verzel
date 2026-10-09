# Teste Técnico QA Júnior — Verzel

## Visão geral

Este repositório contém os entregáveis desenvolvidos para o teste técnico de QA Júnior da Verzel. O projeto abrange testes manuais, testes de API, testes de interface (UI), automação de testes e registro de bugs da aplicação Verzel Store.

## Entregáveis

### Casos de teste manuais
A planilha com os casos de teste e seus resultados está disponível na pasta [`planilha`](./planilha/).

### Bugs e evidências
A pasta [`bugs-e-evidencias`](./bugs-e-evidencias/) contém a exportação dos bugs registrados no Jira e as capturas de tela utilizadas como evidências dos testes.

### Testes automatizados
Os arquivos Python na raiz do repositório contêm testes automatizados de API e interface, incluindo cenários de validação de cupons, frete grátis, fluxo do carrinho e limites de quantidade.

## Tecnologias e ferramentas

- Python
- Pytest
- Playwright
- Jira
- Postman

## Como executar os testes

1. Clone este repositório.
2. Crie e ative um ambiente virtual Python.
3. Instale as dependências necessárias para os testes.
4. Execute os testes com o Pytest:

```bash
python -m pytest
```

A execução pode exigir configurações adicionais ou acesso à aplicação testada, dependendo do cenário.

## Estrutura do repositório

- `planilha/` — casos de teste manuais e resultados.
- `bugs-e-evidencias/` — exportação dos bugs do Jira e screenshots das evidências.
- `test_*.py` — scripts de testes automatizados.
- `.gitignore` — arquivos e diretórios excluídos do controle de versão.

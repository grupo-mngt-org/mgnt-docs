## Convenções de Commit e Branch

Os commits seguem o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/).

### Formato

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

### Tipos

| Tipo | Quando usar |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `refactor` | Refatoração sem mudança de comportamento |
| `chore` | Tarefas técnicas, dependências, configuração |
| `docs` | Documentação |
| `test` | Adição ou correção de testes |
| `style` | Formatação, espaçamento — sem mudança de lógica |
| `perf` | Melhoria de performance |
| `ci` | Mudanças em pipelines de CI/CD |

### Escopo

Opcional. Indica o módulo ou área afetada.

```
feat(financeiro): adicionar cálculo de juros compostos
fix(auth): corrigir expiração de token JWT
```

### Breaking Changes

Mudanças que quebram compatibilidade devem ter `!` após o tipo e uma nota no rodapé:

```
feat(api)!: remover endpoint legado de autenticação

BREAKING CHANGE: o endpoint /auth/v1/login foi removido, utilizar /auth/v2/login
```

### Exemplos

```
feat: adicionar listagem de usuários ativos
fix: corrigir erro de arredondamento no módulo de pagamentos
chore: atualizar dependências do projeto
docs: adicionar instruções de instalação no README
refactor(pedidos): extrair lógica de validação para service
```

---

### Convenções de Branch

O nome da branch segue o mesmo prefixo do tipo de commit, combinado com o número da demanda no ELO e uma descrição curta:

```
<tipo>/ELO-<número>-<descrição-curta>
```

Exemplos:
```
feat/ELO-42-listagem-de-usuarios
fix/ELO-87-calculo-de-juros
hotfix/ELO-103-erro-autenticacao
chore/ELO-15-atualizar-dependencias
```

**Regras:**
- Usar kebab-case na descrição (palavras separadas por `-`)
- Descrição curta e objetiva, sem artigos
- Sempre referenciar o número da demanda no ELO para rastreabilidade

## Pull Requests

Todo código que vai para produção passa por um Pull Request. O PR é o mecanismo de code review e rastreabilidade entre a demanda no ELO e as mudanças no repositório.

### Regras Gerais

- Todo PR deve ser revisado e aprovado por ao menos um outro membro do time (desenvolvedor, líder técnico ou gerente) antes do merge
- O merge só pode ser feito após aprovação
- PRs devem ser focados — uma entrega por PR, sem misturar demandas não relacionadas

### Título

Texto claro e descritivo resumindo o que a mudança faz.

Exemplos:
- `Adicionar endpoint de listagem de usuários`
- `Corrigir cálculo de juros no módulo financeiro`
- `Atualizar integração com ERP de faturamento`

### Descrição

Todo PR deve conter:

- **O que foi feito** — resumo das mudanças
- **Por que foi feito** — contexto ou problema resolvido
- **Demanda no ELO** — link da Tarefa ou Projeto correspondente
- **Como testar** — passos para validar a mudança localmente ou em staging
- **Observações** — dependências, riscos ou pontos de atenção para o revisor (se aplicável)

### Commits

Os commits dentro do PR devem seguir as [convenções de commit](commits.md).

### Deploy em Produção

PRs que resultam em deploy em produção devem estar vinculados a uma issue de [Gestão de Mudanças](change-management.md).

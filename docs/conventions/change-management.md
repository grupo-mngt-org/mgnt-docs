## Gestão de Mudanças

Todo deploy em produção deve passar por um processo de formalização via **issue no GitHub**, independente do tamanho ou complexidade da mudança. O objetivo é garantir rastreabilidade, revisão por pares e validação de que a mudança foi aplicada corretamente.

### Sistemas Cobertos

Este processo se aplica a todos os sistemas em produção do Grupo MNGT:

- **Ecossistema MNGT**
- **ELO**
- **Conecta Grupo**
- **MNGPT**

---

### Processo

1. **Abrir a issue** — antes do deploy, criar uma issue usando o template *Gestão de Mudanças*; a label `mudança: aguardando revisão` é aplicada automaticamente
2. **Revisão** — um par (desenvolvedor, líder técnico ou gerente) revisa, comenta na issue confirmando a aprovação e atualiza a label para `mudança: aprovada`
3. **Deploy** — realizado somente após a label `mudança: aprovada` estar aplicada
4. **Pós-deploy** — quem fez o deploy atualiza a label para `mudança: em produção`
5. **Validação** — registrar na issue as evidências de que a mudança está correta em produção e atualizar a label para `mudança: concluída`
6. **Fechamento** — issue fechada após validação confirmada

### Labels de Estado

As labels abaixo devem ser criadas no repositório em **Issues → Labels**:

| Label | Descrição |
|---|---|
| `mudança: aguardando revisão` | Issue aberta, aguardando revisão por um par |
| `mudança: aprovada` | Revisada e aprovada, pronta para deploy |
| `mudança: em produção` | Deploy realizado, aguardando validação |
| `mudança: concluída` | Validada em produção e encerrada |

---

### Modelo de Issue

**Título:** `[Mudança] <descrição curta>` (ex: _[Mudança] Atualização da integração com ERP de faturamento_)

---

#### Descrição da Mudança
<!-- O que está sendo alterado e por quê. -->

#### Sistemas e Serviços Impactados
<!-- Liste todos os sistemas, serviços, integrações ou ambientes afetados. -->

#### PRs Relacionados
<!-- Links dos Pull Requests que compõem essa mudança. -->

#### Demanda no ELO
<!-- Link da Tarefa ou Projeto correspondente no ELO. -->

#### Plano de Rollback
<!-- Passos para reverter a mudança caso algo dê errado em produção. Deve ser viável e testado antes do deploy quando possível. -->

#### Validação Pós-Deploy
<!-- Preenchido após o deploy. Descreva o que foi validado e anexe evidências (prints, logs, outputs de monitoramento, etc.). -->

- [ ] Validado em produção
- [ ] Evidências anexadas
- [ ] Aprovado pelo revisor para fechamento

## Definition of Done (DoD)

Uma demanda está **concluída** quando todos os critérios abaixo são atendidos. A transição para o status *Concluído* no ELO só deve ocorrer após esse checklist estar completo.

---

### Checklist

- [ ] **Code review aprovado** — passou pelo status *Revisão* e foi aprovado
- [ ] **Testado pelo desenvolvedor** — validado no ambiente de desenvolvimento, incluindo casos de borda

**Validação de negócio**
- [ ] **Critérios de aceitação verificados** — todos os itens definidos no [DoR](definition-of-ready.md) foram atendidos
- [ ] **Validado com Stakeholder e/ou Ponto de contato** — se aplicável

**Deploy e rastreabilidade**
- [ ] **Deploy realizado em produção** — seguindo o [procedimento de Gestão de Mudanças](change-management.md)
- [ ] **Demandas filhas concluídas** — todas as Etapas e Tarefas relacionadas estão concluídas antes de fechar a demanda

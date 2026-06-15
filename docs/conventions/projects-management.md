## Gestão de Projetos de desenvolvimento

Esse documento visa definir como vão ser gerenciadas as demandas de desenvolvimento. A plataforma utilizada para essa gestão é o ELO, ferramenta interna do Grupo MNGT que é um fork do OpenProject. Todo deploy em produção segue o processo de [Gestão de Mudanças](change-management.md).

### Tipos de Demandas
- *Entrada*: É a etapa inicial da maioria das demandas, um esboço. Toda demanda que for passada sem escopo bem definido e seguindo os critérios de [DoR](definition-of-ready.md) chegam como uma Entrada. Uma Entrada pode ter uma descrição mais livre de acordo com o que foi passado por quem demandou a nível de negócio, sem prazo e sem comprometimento de entrar na Sprint. Após passar por refinamento, a demanda deixa de ser uma Entrada.
- *Projeto*: É o nível macro de demanda. Um Projeto pode ser criado fora do escopo exclusivo de Desenvolvimento — como um projeto maior que envolve múltiplas áreas da empresa — e o time de Desenvolvimento atuar em Tarefas atribuídas dentro desse contexto.
- *Etapa*: É um nível macro acima de tarefa e abaixo de projeto, onde é possível especificar uma etapa de um projeto de forma a facilitar o acompanhamento e separar em pacotes de entregas.
- *Tarefa*: É o nível mais elementar de uma demanda, onde há de fato execução da demanda pelo desenvolvedor.

Com exceção do tipo de Entrada, os demais tipos seguem o padrão vigente de gestão de projetos do Grupo MNGT.

### Personas da Demanda
- *Responsável*: Desenvolvedor responsável pela execução e entrega da demanda.
- *Stakeholder*: Pessoa de negócios que é "dona" da demanda e interessada na conclusão. Exemplo: Diretor Financeiro que demandou um sistema financeiro.
- *Pontos de contato*: Se aplicável, uma ou mais pessoas de operação do negócio que também tem interesse e vão operar no que for desenvolvido. Exemplo: Membro do time Financeiro responsável por Contas a Pagar.

### Etapas de conclusão da Demanda
- *Pendente*: Demanda ainda aguarda ser refinada.
- *Em refinamento*: Está sendo refinada de acordo com o [DoR](definition-of-ready.md) e modelo de criação de Demandas.
- *Pronto*: Ready to do, a demanda foi refinada, segue o DoR e o modelo de descrição e está pronta para ser executada pelo time.
- *Em andamento*
- *Revisão*: Está em revisão de código via Pull Request e/ou revisão de negócio por parte de stakeholder ou ponto de contato. O processo de code review e padrões de PR estão descritos em [Pull Requests](pull-requests.md).
- *Concluído*: Todas as demandas relacionadas foram entregue, foi feita Gestão de Mudanças (se aplicável), validado com stakeholders e segue todo o [DoD](definition-of-done.md).

### Fase de Entrada
Enquanto a demanda ainda é apenas uma etapa, ela deve ser enxergada como uma Entrada, ou seja, ela é uma ideia/desejo mas que ainda não tem informações ou definições o suficiente para ser refinada e entrar em desenvolvimento. Uma demanda pode não ser lançada como Entrada, mas isso deve ser exceção, para demandas muito simples ou tão bem definidas que torna essa triagem desnecessária.

### Criação de Demandas que não são Entrada
Um Projeto deve ser criado apenas em conjunto e validado com o Líder Técnico. Tarefas que não tem essa necessidade de definição podem ser criadas e definidas livremente pelo time. Abaixo segue um modelo de descrição dessas demandas, que se aplica tanto a Projetos quanto a tarefas:

#### Modelo de Descrição de Demanda
Título: [Ação Clara] + [Objeto] (Ex: Criar endpoint de listagem de usuários)

Área atendida:
Stakeholder:
Pontos de contato:

##### Contexto e Justificativa
<!-- Breve resumo do problema e qual valor de negócio a atividade entrega. -->

##### Critérios de Aceitação
<!-- Condições exatas e premissas que determinam que o trabalho foi concluído com sucesso e seguem as regras de negócio. -->

##### Observações técnicas
<!-- Caso haja definições técnicas a se considerar, como por exemplo qual rota de API acessar, qual tecnologia usar e etc. -->

##### Anexos e Links Úteis
<!-- Materiais de apoio. -->

---

### Sprints

As Sprints têm duração de **2 semanas**.

#### Rotinas

**Daily**
Reunião diária de alinhamento do time sobre o andamento das demandas em curso, impedimentos e próximos passos.

**Refinamento**
Duas reuniões reservadas por semana para refinar demandas que estão como *Pendente* ou *Em refinamento*, aplicando o [DoR](definition-of-ready.md). Caso não haja demandas a refinar, a reunião é cancelada.

**Planning**
Realizada no início de cada Sprint. O time:
1. Verifica a capacidade disponível para a Sprint — cada membro tem uma quantidade base de pontos que consegue entregar em uma Sprint de 10 dias úteis; ausências, feriados e membros não full-time são descontados proporcionalmente, resultando na capacidade total do time para aquela Sprint
2. Puxa demandas com status *Pronto* (refinadas e que seguem o DoR)
3. Estima o esforço de cada demanda usando a sequência de Fibonacci, com auxílio de IA como referência inicial
4. Em caso de discordância na estimativa, a decisão é resolvida por Planning Poker
5. Define quais demandas entram na Sprint com base na capacidade estimada

**Sprint Review**
Realizada ao final de cada Sprint com a presença do gerente. O time apresenta as entregas concluídas e colhe feedback.

**Retrospectiva**
Realizada ao final de cada Sprint para avaliar o processo: o que funcionou, o que pode melhorar e quais ações serão tomadas na próxima Sprint.
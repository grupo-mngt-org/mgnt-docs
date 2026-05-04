---
hide:
  - toc
---

# Caveman

## O que é

Caveman é um plugin/skill para Claude Code (e 30+ outros agentes) que reduz o consumo de **tokens de saída** em até 65% ao treinar o modelo para responder de forma telegráfica, sem perder precisão técnica.

> "Why use many token when few token do trick"

Comprime a **resposta do Claude** — não a saída de comandos do terminal.

---

## Instalação (Linux via curl)

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

O script detecta automaticamente o agente instalado (Claude Code, Cursor, Gemini CLI, etc.) e configura o plugin correspondente.

**Instalação manual no Claude Code:**
```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**Verificar instalação:**
```bash
/caveman-help
```

---

## Níveis de compressão

| Nível | Ativar | Estilo | Quando usar |
|---|---|---|---|
| **Lite** | `/caveman lite` | Remove filler, mantém gramática | Explicações para a equipe, onboarding |
| **Full** | `/caveman` | Remove artigos e fragmentos | Uso geral no dia a dia |
| **Ultra** | `/caveman ultra` | Telegráfico, abrevia tudo | Debug rápido, respostas one-liner |
| **Off** | `/caveman off` | Normal | Documentação, análises detalhadas |

Os modos Wenyan (compressão em chinês clássico) não são mapeados no padrão do Grupo MNGT.

O nível ativo persiste durante toda a sessão até ser alterado manualmente.

---

## Quando usar e quando não usar

### Usar Caveman

- **Debug e correção de bugs** — o problema e a solução são o que importa, não a explicação
- **Execução de tarefas repetitivas** — commits, refatorações, renomeações, formatações
- **Code review** — feedback direto por linha, sem introduções
- **Perguntas técnicas objetivas** — "qual CFOP para saída?", "como paginar no Supabase?"
- **Sessões longas de desenvolvimento** — para conservar contexto
- **Respostas de status** — "feito", "erro em X", "qual próximo passo?"

### Não usar Caveman (ou usar Lite)

- **Documentação para a equipe** — clareza vale mais que brevidade
- **Onboarding de novos devs** — contexto e explicação são necessários
- **Análises de segurança ou auditoria** — detalhe é obrigatório
- **Decisões arquiteturais** — trade-offs precisam de explicação completa
- **Comunicação com stakeholders não-técnicos** — linguagem telegráfica gera confusão
- **Quando a resposta vai virar documentação** — escreva já no formato final

**Regra prática:** se a resposta vai ser lida só por você durante o desenvolvimento → Caveman. Se vai ser lida por outras pessoas ou virar artefato → desative.

---

## Benchmarks de redução de tokens

Medidos na API Claude com tarefas reais de desenvolvimento:

| Tarefa | Normal | Caveman | Economia |
|---|---|---|---|
| Explicar bug de re-render React | 1.180 | 159 | **87%** |
| Corrigir auth middleware | 704 | 121 | **83%** |
| Configurar PostgreSQL connection pool | 2.347 | 380 | **84%** |
| Debug race condition PostgreSQL | 1.200 | 232 | **81%** |
| Implementar React error boundary | 3.454 | 456 | **87%** |
| Explicar git rebase vs merge | 702 | 292 | **58%** |
| Refatorar callback para async/await | 387 | 301 | **22%** |
| Review de PR para segurança | 678 | 398 | **41%** |
| **Média** | **1.214** | **294** | **65%** |

Tarefas de execução (refatoração, commits) têm menor economia; explicações e análises têm maior economia.

---

## Antes e depois — exemplo real

**Pergunta:** "Por que meu componente React está re-renderizando?"

=== "Normal (~69 tokens)"

    ```
    The reason your React component is re-rendering is likely because you're
    creating a new object reference on each render cycle. When you pass an
    inline object as a prop, React's shallow comparison sees it as a different
    object every time, which triggers a re-render. I'd recommend using useMemo
    to memoize the object.
    ```

=== "Caveman Full (~19 tokens)"

    ```
    New object ref each render. Inline object prop = new ref = re-render.
    Wrap in `useMemo`.
    ```

=== "Caveman Ultra (~12 tokens)"

    ```
    Inline obj prop → new ref → re-render. `useMemo`.
    ```

---

## Skills especializadas

| Skill | Comando | O que faz |
|---|---|---|
| **caveman-commit** | `/caveman-commit` | Gera mensagens de commit Conventional Commits ≤50 chars |
| **caveman-review** | `/caveman-review` | Feedback de PR por linha: `L42: bug: user null. Add guard.` |
| **caveman-stats** | `/caveman-stats` | Tokens usados, economia estimada e custo da sessão |
| **caveman:compress** | `/caveman:compress CLAUDE.md` | Reescreve arquivos de memória em caveman-speak (~46% menor) |

---

## Comandos rápidos

```bash
/caveman           # Ativa modo Full (padrão)
/caveman lite      # Ativa modo Lite
/caveman ultra     # Ativa modo Ultra
/caveman off       # Desativa
/caveman-stats     # Ver economia da sessão atual
/caveman-help      # Quick-reference card
```

---

## Desinstalação

**Desabilitar plugin:**
```bash
/plugin disable caveman
```

---

## Referências

- [GitHub — JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

---
hide:
  - toc
---

# RTK — Rust Token Killer

## O que é

RTK é um proxy CLI de alto desempenho escrito em **Rust** que intercepta saídas de comandos de terminal e as comprime antes de enviá-las ao contexto de agentes de IA (Claude Code, Cursor, GitHub Copilot, etc.).

O resultado é uma redução de **60–99% no consumo de tokens**, sem perda de informação relevante para o agente — erros, diffs e resultados de testes continuam presentes, mas o ruído é eliminado.

- Binário único, zero dependências externas
- Overhead inferior a 10ms por comando
- Suporte a 100+ comandos e ferramentas
- Integração automática via hooks de shell

---

## Por que usar

Em sessões de codificação com Claude Code, boa parte dos tokens é consumida por saídas verbosas que não agregam contexto útil: linhas de progresso, testes que passaram, logs repetitivos, diffs completos de arquivos grandes.

RTK filtra essas saídas na origem — antes de chegarem ao contexto — usando estratégias como:

- **Error-only mode**: descarta linhas de sucesso em testes, mantém apenas falhas
- **Deduplicação**: colapsa linhas idênticas repetidas em contadores (`linha x100`)
- **Agrupamento de erros**: agrega por tipo ao invés de listar cada ocorrência
- **Compressão de árvore**: limita exibição de `find` / `tree` agrupando por diretório
- **Filtragem de progresso**: remove códigos ANSI e barras de loading

O efeito prático é que as sessões duram **até 3x mais** com o mesmo limite de contexto, e o custo por sessão cai proporcionalmente.

---

## Instalação (Linux via curl)

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh
```

O script detecta automaticamente a arquitetura (x86_64 / ARM64), baixa o binário pré-compilado e instala em `~/.local/bin`.

**Verificar instalação:**

```bash
rtk --version
rtk gain        # Exibe o dashboard de tokens economizados
```

---

## Configuração inicial

Após instalar, rode o comando de inicialização para Claude Code:

```bash
rtk init -g
```

Isso instala um hook no `~/.bashrc` / `~/.zshrc` que intercepta comandos e os reescreve automaticamente. A partir daí, ao digitar `git status` em uma sessão Claude Code, o hook executa internamente `rtk git status` e entrega a saída comprimida — sem nenhuma mudança no seu fluxo de trabalho.

**Para outros agentes:**

```bash
rtk init -g --gemini        # Gemini CLI
rtk init -g --agent cursor  # Cursor
rtk init --agent cline      # Cline / Roo Code
```

**Configuração por projeto** (cria `CLAUDE.md` local com preferências):

```bash
cd /caminho/do/projeto
rtk init
```

---

## Como funciona — mecanismo de compressão

Ao executar um comando via RTK, o binário:

1. Executa o comando original em subprocesso
2. Captura a saída completa (stdout + stderr)
3. Aplica o filtro correspondente ao comando (ex.: `cargo test` → mode error-only)
4. Entrega a saída comprimida ao contexto do agente
5. Em caso de falha no filtro, entrega a saída bruta como fallback (nunca quebra o fluxo)

Os filtros são implementados em 40+ módulos independentes, um por comando ou família de comandos.

---

## Impacto em tokens — testes reais neste repositório

Os exemplos abaixo foram capturados rodando RTK v0.38.0 diretamente no repositório `mngt`.

### `find` — listagem de arquivos `.md`

=== "Sem RTK"

    ```
    /mngt/docs-mngt/docs/index.md
    /mngt/docs-mngt/docs/tools/n8n.md
    /mngt/docs-mngt/docs/tools/evolution-api.md
    /mngt/docs-mngt/docs/tasks/tarefas.md
    /mngt/docs-mngt/docs/claude-code/claude-code.md
    /mngt/docs-mngt/docs/documentation/documentacao.md
    /mngt/docs-mngt/docs/credentials/netdata.md
    /mngt/docs-mngt/docs/credentials/api-softexpert.md
    # ... (56 linhas adicionais com caminhos absolutos completos)
    ```

=== "Com RTK"

    ```
    63F 17D:

    ./ index.md
    ai/discovery/ oportunidades.md
    ai/guides/ 1-IA-aplicada-para-desenvolvedores-em-empresas.md 4-integração-e-automacao-com-IA-em-negocios.md
    ai/tools/ openwebui.md
    claude-code/ claude-code.md
    claude-code/config/ rtk.md
    credentials/ api-mobbus.md api-prevision.md api-qive.md ... +11 more
    documentation/documentacao/api-sienge/ 0-modulo-complementar.md ... +5 more
    # Agrupado por diretório, caminhos relativos, resumo no topo
    ```

| | Tokens |
|---|---|
| Sem RTK | ~705 |
| Com RTK | ~3 |
| **Economia** | **99.6%** |

---

### `ls -la` — listagem de diretório

=== "Sem RTK"

    ```
    total 48
    drwxr-xr-x 11 hownatios hownatios 4096 May  4 07:51 .
    drwxr-xr-x  9 hownatios hownatios 4096 May  4 07:51 ..
    drwxr-xr-x  5 hownatios hownatios 4096 Feb 23 17:34 ai
    drwxr-xr-x  3 hownatios hownatios 4096 May  4 07:51 claude-code
    drwxr-xr-x  2 hownatios hownatios 4096 Apr 16 16:40 credentials
    drwxr-xr-x  3 hownatios hownatios 4096 Feb 18 11:16 documentation
    drwxr-xr-x  2 hownatios hownatios 4096 Feb 23 17:34 files
    -rw-r--r--  1 hownatios hownatios  356 Mar  2 07:07 index.md
    drwxr-xr-x  2 hownatios hownatios 4096 Apr 16 17:00 infra
    drwxr-xr-x  2 hownatios hownatios 4096 Feb 18 08:52 stylesheets
    drwxr-xr-x  3 hownatios hownatios 4096 Feb 18 11:31 tasks
    drwxr-xr-x  3 hownatios hownatios 4096 Mar 30 07:09 tools
    ```

=== "Com RTK"

    ```
    ai/
    claude-code/
    credentials/
    documentation/
    files/
    infra/
    stylesheets/
    tasks/
    tools/
    index.md  356B
    ```

| | Tokens |
|---|---|
| Sem RTK | ~181 |
| Com RTK | ~26 |
| **Economia** | **85.6%** |

---

### `git status` — status do repositório

=== "Sem RTK"

    ```
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

=== "Com RTK"

    ```
    * main...origin/main
    clean — nothing to commit
    ```

| | Tokens |
|---|---|
| Sem RTK | ~25 |
| Com RTK | ~12 |
| **Economia** | **52%** |

---

### Dashboard após 4 comandos reais

```
RTK Token Savings (Global Scope)
════════════════════════════════════════════════════════════

Total commands:    4
Input tokens:      917
Output tokens:     46
Tokens saved:      871 (95.0%)
Total exec time:   14ms (avg 3ms)
Efficiency meter: ███████████████████████░ 95.0%

By Command
───────────────────────────────────────────────────────────────────────
  #  Command          Count  Saved    Avg%    Time  Impact
───────────────────────────────────────────────────────────────────────
 1.  find                 1    702   99.6%     4ms  ██████████
 2.  ls -la               1    155   85.6%     3ms  ██░░░░░░░░
 3.  git status           1     13   52.0%     6ms  ░░░░░░░░░░
 4.  git log --oneline    1      1   16.7%     1ms  ░░░░░░░░░░
───────────────────────────────────────────────────────────────────────
```

**Em apenas 4 comandos: 871 de 917 tokens economizados (95%).**

---

### Benchmarks de referência (projetos maiores)

| Comando | Sem RTK | Com RTK | Economia |
|---|---|---|---|
| `cargo test` (262 testes passando) | 4.823 tokens | 11 tokens | **99%** |
| `git diff HEAD~1` (arquivo grande) | 21.500 tokens | 1.259 tokens | **94%** |
| `pytest` (33 testes) | 756 tokens | 24 tokens | **97%** |
| `cat arquivo.rs` (1.295 linhas) | 10.176 tokens | 504 tokens | **95%** |
| Sessão de 30 min (TypeScript/Rust) | ~118.000 tokens | ~23.900 tokens | **80%** |

O impacto é maior em operações com saídas repetitivas (testes, find, logs) e menor em comandos que já produzem pouco output (git log com poucos commits).

---

## Comandos úteis

```bash
# Ver estatísticas de tokens economizados
rtk gain

# Ver histórico por sessão
rtk gain --history

# Descobrir comandos sem cobertura RTK na sessão atual
rtk discover

# Estatísticas da sessão atual
rtk session

# Resetar estatísticas
rtk gain --reset

# Executar sem compressão (bypass — útil para debug)
rtk proxy <comando> [args...]
```

---

## Desinstalação

```bash
# Remover hooks do shell
rtk init -g --uninstall

# Remover binário manualmente
rm ~/.local/bin/rtk
```

---

## Referências

- [GitHub — rtk-ai/rtk](https://github.com/rtk-ai/rtk)
- [Site oficial](https://www.rtk-ai.app)

---
hide:
  - toc
---

# Fast Config — Claude Code

Referência rápida de configuração. Sem explicações, só os passos para configurar.

---

## 1. RTK (comprime saída de terminal → menos tokens de entrada)

**Instalar:**
```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh
```

**Inicializar hook:**
```bash
rtk init -g
```

---

## 2. Caveman (comprime respostas do Claude → menos tokens de saída)

**Instalar:**
```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

**Ativar na sessão:**
```
/caveman          # full — debugging, dúvidas técnicas
/caveman lite     # estudo, code review, detalhes de implementação
/caveman ultra    # commits, execução rápida, respostas curtas
/caveman off      # docs, planejamento, segurança
```

---

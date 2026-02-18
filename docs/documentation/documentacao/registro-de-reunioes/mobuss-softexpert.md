---
hide:
  - toc
---

# MOBUSS > SOFTEXPERT

# Sobre FVS:

- FVS FECHADA
    - Uma FVS é considerada como fechada partir do campo “SITUAÇÃO DO FORMULÁRIO”, quando ele está como Preenchido
        - Tipos de situação
            - Aberto
            - Aberto no Dispositivo Móvel
            - Preenchido
            - Encerrado
- Indicador de retrabalho (Somátiro de item nça conforme/Total de itens)
    - O que defini se um item está não conforme é a partir da coluna “SITUAÇÃO CONFORMIDADE”
        - Tipos de situação
            - Conforme
            - Não conforme
            - Não aplicado (Está preenchido)
            - Não respondido (Situação do formulário está em aberto)

## Como precisamos pensar o fluxo usando a planilha?

O fluxo será pensado para ter a recorrência de execução mensal

- Na emissão da planilha eu posso filtrar por FVS = “FVS Ficha de verificação de serviço”
- Eu preicso achar um parametro para agrupar o itens da fvs
- A partir disso ao identificar se todos os itens  estão como Preenchido na coluna  “SITUAÇÃO DO FORMULÁRIO” eu posso considerar aquela FVS como **FECHADA**
- Para calcular o valor de retraballho eu preciso pegar todos esses items que agrupei e verificar a partir da coluna  “SITUAÇÃO CONFORMIDADE” quais estão como não conforme e dividir pelo total de itens

## PLANO DE AÇÃO INICIAL

- Criar um endpoint capaz de receber esse arquvio xlsx para ser manipulado
- Nessa manipulação será identificada as FVS fechadas, como também calcular o valor de retrabalho da FVS

## ETAPA SUBSEQUENTE

- Com esses dados fazer a integração com o módulo de qualidade do softexpert
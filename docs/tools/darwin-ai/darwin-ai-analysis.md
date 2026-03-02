## Introdução
O objetivo desse documento é catalogar análise e testes da plataforma Darwin AI, em um posto de visto mais voltado para a parte técnica da tecnologia, em especial as integrações com ferramentas externas.

## Testes
Foram usados dois funcionárias de IA: Atlas e Incrível

Atlas: Funcionário de IA criado pelo consultor Guilherme, que tem um prompt escrito por ele que dá Contexto Geral de um negócio simplificado e hipotético que se dedica ao atendimento de vender tanto o serviço de Locação de Galpão (Centro Logístico de Rio Claro) quanto de Armazenagem (Mais Armazém). 
Durante os testes, algumas alterações nas etapas foram feitas para testar funcionalidades.

<details> 
<summary> Contexto e Pipelines definidos para Atlas </summary>

Contexto Geral fornecido ao funcionário de IA Atlas:
```
## 1. Nome da IA:

Atlas

---

## 2. Objetivo da IA:

Qualificar leads B2B interessados em locação de galpões logísticos e serviços de armazenagem, coletando requisitos técnicos e comerciais, validando aderência operacional e agendando reunião técnica com o time comercial já com briefing completo.

---

## 3. Produtos / Modelos a Oferecer:

### 3.1 Locação de Galpões Logísticos

* Galpões de 1.000 m² a 25.000 m²
* Pé-direito: 8m a 14m
* Piso industrial de alta resistência (5 a 6 ton/m²)
* Docas niveladoras
* Pátio para carretas
* Segurança 24h
* Contratos a partir de 12 meses

A IA deve apresentar opções compatíveis com:

* Região desejada
* Tamanho necessário
* Tipo de operação

---

### 3.2 Armazenagem Operacional (Contrato Logístico)

* Armazenagem paletizada
* Controle de estoque (WMS)
* Operação FIFO/LIFO
* Cross-docking
* Separação e expedição
* Inventário rotativo

Modelo de cobrança:

* Valor por pallet/mês
* Taxa de movimentação por entrada/saída
* Serviços adicionais sob demanda

---

## 4. Critérios de Qualificação

###  Dados obrigatórios:

* Nome completo
* Empresa
* Cargo
* Telefone
* E-mail
* Cidade/região de interesse

---

### Dados técnicos obrigatórios para qualificação:

Se for **locação de galpão**:

* Metragem necessária (m²)
* Pé-direito mínimo desejado
* Necessidade de docas (quantidade aproximada)
* Tipo de carga
* Prazo para início da operação

Se for **armazenagem**:

* Volume médio (pallets ou m³)
* Tipo de carga
* Frequência de movimentação (baixo / médio / alto giro)
* Necessidade de temperatura controlada (sim/não)
* Prazo estimado de contrato

---

### Perguntas importantes (não bloqueantes):

* Orçamento ou faixa de investimento mensal
* Empresa já possui operação atual? Onde?
* Quem é o decisor final?

Caso o lead não informe orçamento, a IA deve seguir o fluxo normalmente e qualificar como potencial.

---

## 5. FAQ – Perguntas Frequentes

### Em quais cidades vocês atuam?

Atuamos principalmente em:

* São Paulo (Capital, Guarulhos, Cajamar, Barueri)
* Campinas
* Jundiaí
* Extrema (MG)
* Rio de Janeiro (Duque de Caxias)

---

###  Qual o tamanho mínimo de galpão disponível?

A partir de 1.000 m².

---

###  Existe contrato mínimo?

Sim. Contrato mínimo de 12 meses para galpões.
Armazenagem pode ser contratada a partir de 3 meses.

---

###  Qual o prazo para enviar proposta?

Após envio das informações técnicas:

* Proposta preliminar em até 48 horas úteis.
* Projeto técnico completo em até 5 dias úteis.

---

###  Vocês operam carga refrigerada?

Sim, mediante disponibilidade e análise técnica prévia.

---

###  Trabalham com carga perigosa?

Sim, desde que dentro das normas da ANVISA e Corpo de Bombeiros, com documentação adequada.

---

###  O galpão possui segurança?

Sim. Segurança 24h, CFTV e controle de acesso.

---

###  Posso agendar uma visita técnica?

Sim. A IA pode sugerir datas e horários disponíveis para visita presencial.

---

###  Como funciona o pagamento?

Pagamento mensal via boleto ou transferência bancária.
Contrato formal assinado antes do início da operação.

---

## 6. Serviços que NÃO oferecemos:

* Financiamento imobiliário
* Empréstimos
* Seguro de carga próprio (apenas indicação de corretoras)
* Operações para pessoa física
* Guarda-móveis residencial
* Transporte rodoviário próprio (podemos indicar parceiros)

---

## 7. Vendedores e Telefones


* João Colares – Executivo Comercial Logístico
  +55 11 98888-1000

* Mariana Lopes – Comercial Armazenagem
  +55 11 97777-2000
```
Pipeline inicial (Qualificação de leads):
<img width="474" height="565" alt="image" src="https://github.com/user-attachments/assets/6bb8535b-e95c-4a96-92f7-1e026e279c06" />

Pipeline de Armazenagem:
<img width="1392" height="573" alt="image" src="https://github.com/user-attachments/assets/7435b58c-21bc-40a5-b9cd-ce778991de4d" />

Pipeline de Locação:
<img width="1390" height="558" alt="image" src="https://github.com/user-attachments/assets/15fcec96-f45a-42ee-9603-1bb3122d60a3" />

A última etapa (Agendamento de visita) foi criada durante os testes. O objetivo dessa etapa é validar integrações. A integração com o Google Claendar já é "nativa" da plataforma, enquanto a integração com o Discord foi
personalizada para esse teste por meio da criaçaõ de um servidor MCP usando Python.
</details>

*TO DO* **Ainda não consegui criar esse funcionário de IA para testar, estou por fazer esse teste**
Incrível: Funcionário de IA criado para fins desse teste, que tem um prompt escrito por ele que dá Contexto Geral de um negócio simplificado e hipotético que se dedica ao atendimento de vender produtos imobiliários da Área Incrível.

<details>
</details>

## Integrações

O objetivo principal desses testes é validar as integrações com ferramentas externas, e o Darwin AI oferece dois:

- Custom HTTP
- Custom MCP
- Integrações prontas (em geral, MCP já pré definidos)

Custom HTTP permite se conectar com API's via requisições HTTP (funcionalidade aida não testada). Custom MCP permite se conectar com servidores MCP, seguindo os padrões definidos pela Anthropic,
fornecendo um endpoint /sse que o Darwin AI utiliza para se comunicar com o servidor.

### Servidor MCP
Para testar a ferramente de Custom MCP, foi desenvolvido um servidor MCP, com o único objetivo de enviar uma mensagem para o Discord.

Código python do servidor de teste
```python
import os
import asyncio
import json
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
import discord

app = FastAPI()

TOKEN = ""
CHANNEL_ID = 1440308689104797790

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Dicionário de filas por sessão
session_queues: dict[str, asyncio.Queue] = {}

@app.on_event("startup")
async def startup():
    asyncio.create_task(client.start(TOKEN))

@app.get("/sse")
async def sse(request: Request):
    session_id = str(id(request))
    queue = asyncio.Queue()
    session_queues[session_id] = queue

    async def event_generator():
        # Envia o endpoint imediatamente
        yield f"event: endpoint\ndata: /messages?session_id={session_id}\n\n"

        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=20)
                    yield f"data: {json.dumps(event)}\n\n"
                except asyncio.TimeoutError:
                    yield ":\n\n"
        finally:
            session_queues.pop(session_id, None)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )

@app.post("/messages")
async def messages(request: Request):
    session_id = request.query_params.get("session_id")
    queue = session_queues.get(session_id)

    body = await request.json()
    method = body.get("method")
    request_id = body.get("id")

    if method == "initialize":
        response = {
            "jsonrpc": "2.0",
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "discord-bot", "version": "1.0.0"}
            },
            "id": request_id
        }

    elif method == "notifications/initialized":
        return JSONResponse({"status": "ok"})

    elif method == "tools/list":
        response = {
            "jsonrpc": "2.0",
            "result": {
                "tools": [{
                    "name": "send-discord-message",
                    "description": "Send a message to a Discord channel",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"}
                        },
                        "required": ["query"]
                    }
                }]
            },
            "id": request_id
        }

    elif method == "tools/call":
        tool_name = body["params"]["name"]
        arguments = body["params"]["arguments"]
        if tool_name == "send-discord-message":
            message = arguments["query"]
            try:
                channel = await client.fetch_channel(CHANNEL_ID)
                await channel.send(message)
                response = {
                    "jsonrpc": "2.0",
                    "result": {
                        "content": [{"type": "text", "text": "Mensagem enviada!"}]
                    },
                    "id": request_id
                }
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "error": {"code": -32000, "message": str(e)},
                    "id": request_id
                }

    else:
        response = {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found"},
            "id": request_id
        }

    # Responde via SSE se tiver sessão, senão responde direto
    if queue:
        await queue.put(response)
        return JSONResponse({"status": "ok"})
    else:
        return JSONResponse(response)
```


## Testes
### 1. Chat de armazenamento logístico
Canal: Whatsapp
Funcionário de IA: Atlas
Objetivo: Realizar as etapas de contratação do serviço de Armazenagem Operacional

Esse teste foi o mais simples, realizado usando apenas as etapas de automação definidas pelo consultor Guilherme para Armazenagem, sem nenhuma integração ou contexto além do já definido.
<img width="1219" height="897" alt="Screenshot from 2026-02-27 13-32-48" src="https://github.com/user-attachments/assets/ff681199-33f3-485b-b7ab-aa74d963133c" />
<img width="1219" height="897" alt="Screenshot from 2026-02-27 13-32-58" src="https://github.com/user-attachments/assets/a27d0c98-48ec-4baf-b816-27a1c5c791d1" />
<img width="1219" height="565" alt="Screenshot from 2026-02-27 13-33-07" src="https://github.com/user-attachments/assets/32bf7fda-603c-4180-9202-c4faecefec52" />
A IA conseguiu responder com base no contexto dado por texto.

### 2. Chat de Locação de Galpões Logísticos
Canal: Whatsapp
Funcionário de IA: Atlas
Objetivo: Realizar as etapas de contratação do serviço de Locação de Galpões Logístico e ao fim agendar uma visita que é registrada.
<img width="738" height="1600" alt="image" src="https://github.com/user-attachments/assets/f5225fe2-0165-4f58-8d9d-ddfd1377bc40" />
<img width="738" height="1600" alt="image" src="https://github.com/user-attachments/assets/ad24c0fd-a486-4234-b2f3-59906cbf3e99" />
<img width="738" height="1600" alt="image" src="https://github.com/user-attachments/assets/e4e488fe-a988-44b4-aaa4-eb88be2539b5" />
<img width="738" height="1600" alt="image" src="https://github.com/user-attachments/assets/e9a0a743-3278-424a-bd55-154d81c321fd" />

A IA conseguiu atender e marcar o agendamento da visita no Google Calendar.

<img width="742" height="364" alt="Screenshot from 2026-02-28 23-17-37" src="https://github.com/user-attachments/assets/8893cefe-b38c-4d66-816e-3b964ec12b46" />

Também foi tentado enviar a mensagem no Discord, que falhou nesse teste, mas funcionou após ajustes em um teste posterior:

<img width="733" height="85" alt="Screenshot from 2026-03-01 22-43-54" src="https://github.com/user-attachments/assets/0f5e3a0a-25f3-4fee-bbf5-23f7be35dc0e" />

### 3. Chat de Locação venda de Casas
(Ainda não realizado)

## Conclusões
(Ainda não foi testado toda plataform)
O Darwin AI é uma ferramenta de atendimento ao cliente poderosa, funcional e que consegue se comunicar com ferramentas externas por meio de MCP e requisições HTTP, ainda que existam dificuldade de debug com as integrações.

É tecnicamente viável integrar o DarwinAI com outras ferramentes e APIs, mas o ideal é que ainda hajá um trabalho de desenvolvimento de software no sentido de desenvolver servidores MCP que sirvam como uma camada de comunicação 
com outros sistemas. O MCP parece mais interessante que o HTTP.

Pontos positivos:
- Interface fácil de usar.
- Pipelines de automação e várias formas de dar contexto ajudam a IA a não alucinar.
- Capacidade de integração com servidores MCP, permitindo integrações com API's próprias ou outras ferramentas usadas pelo Grupo MNGT.
- Capacidade de mostrar o raciocinio e as ações qeu a IA tomou durante as conversar com clientes.

Pontos negativos:
- Alguma dificuldade de fazer debug nas integrações. Seria interessante, por exemplo, poder testar as tools criadas, sem a necessidade de fazer um novo chat de teste, e retornar mensagens de erro mais claras.

---
hide:
  - toc
---

# Farol de Compras

O farol de compras deve listar solicitações de compra e pedido de compra e indicar qual o prazo para a compra ser realizada.

**Referência**: Painel de compras do Sienge. Foi entendido, junto com a Amanda, que o painel de compras tem dados de **itens de Solicitação de Compra e Pedido de Compra.**

**Dados utilizados do Painel de compras**:

- Nº da solicitação de compra
- Grupo de Insumo
- Data da solicitação
- Situação da solicitação
- Data para chegada a obra (vinculado a Solicitação de Compra)
- Data autorização da solicitação
- Situação autorização do item
- Data do Pedido

**Outros dados**:

- **Tabela TAM**: tabela feita pela Amanda com o prazo de quanto tempo a empresa precisa para negociar com cada fornecedor, de acordo com o grupo de insumo

**Campos calculados**:

- **Data Limite de Contratação**:
    
    Data para chegada à obra menos o Prazo de Mobilização do Fornecedor. Caso essa data seja anterior ao prazo mínimo viável para compra, passa a ser considerada como (Data de autorização da solicitação + Prazo de Compra).
    
    **Exemplo:** Data para chegada à obra em 25/03/2026 e Prazo de Mobilização do Fornecedor de 5 dias resulta em Data Limite de Contratação em 20/03/2026. Caso a Data de autorização da solicitação seja 03/03/2026 e o Prazo de Compra seja 7 dias, o prazo mínimo viável seria 10/03/2026, portanto mantém-se a data de 20/03/2026.
    
- **Dentro/Fora do Prazo:**
    
    Considera-se **Fora do Prazo** quando o intervalo entre a Data de autorização da solicitação e a Data Limite de Contratação for menor que a soma do Prazo de Compra com o Prazo de Mobilização do Fornecedor. Caso contrário, considera-se **Dentro do Prazo**.
    
    **Exemplo:** Se a Data de autorização da solicitação for 03/03/2026 e a Data Limite de Contratação for 20/03/2026, o intervalo é de 17 dias. Considerando Prazo de Compra de 7 dias e Prazo de Mobilização do Fornecedor de 5 dias (total de 12 dias), o cenário é **Dentro do Prazo**.
    
- **Farol**:
    
    Diferença, em dias, entre a Data Limite de Contratação e a data atual (hoje).
    
    **Exemplo:** Se hoje for 10/03/2026 e a Data Limite de Contratação for 20/03/2026, o Farol será de 10 dias.
    
- **Dias para atendimento**:
    
    Diferença, em dias, entre a Data do pedido e a Data da solicitação.
    
    **Exemplo:** Se a Data da solicitação for 01/03/2026 e a Data do pedido for 08/03/2026, o tempo para atendimento será de 7 dias.
    

## Desafio técnico

Recuperar dados de itens de solicitação de compra e seu respectivo Pedido de Compra via API do Sienge. 

Endpoint para recuperar itens de solicitações de compra: /purchase-requests/all/items

Endpoint para recuperar uma solicitação de compra:  /purchase-requests/{id}

Endpoint para recuperar um pedido de compra: purchase-orders/{id} **(Não foi identificado como encontrar o pedido de compra de uma determinada solicitação de compra)**

Exemplo de respostas da API:

```json
**/purchase-requests/1213**
{
  "id": 1213,
  "buildingId": 301,
  "departamentId": 5,
  "requesterUser": "MCOIMBRA",
  "requestDate": "2025-11-17",
  "notes": "Montagem de Refeitório.",
  "status": "PARTIALLY_ATTENDED",
  "consistent": "CONSISTENT",
  "createdBy": "MCOIMBRA",
  "createdAt": "2025-11-17T13:01:01.244-03:00",
  "modifiedBy": "AFS",
  "modifiedAt": "2026-01-07T10:04:45.479-03:00",
  "purchaseProcessCarriedOutByBuildingFlag": false
}


**/purchase-requests/all/items**
{
    "purchaseRequestId": 1213,
    "itemNumber": 7,
    "productId": 316,
    "productDescription": "Prego Comum Com Cabeça - Dimensões: 15x15",
    "detailId": null,
    "detailDescription": "",
    "trademarkId": null,
    "trademarkDescription": "",
    "quantity": 3.0,
    "unitySymbol": "kg",
    "notes": "",
    "authorized": true,
    "disapproved": false,
    "competenceLevel": null,
    "disapprovalReason": null,
    "estimatedDeliveryTime": 31,
    "tenantUrl": "https://api.sienge.com.br/rioclaro/public/api",
    "links": [
      {
        "rel": "buildings-appropriations",
        "href": "https://api.sienge.com.br/rioclaro/public/api/v1/purchase-requests/1213/items/7/buildings-appropriations"
      },
      {
        "rel": "delivery-requirements",
        "href": "https://api.sienge.com.br/rioclaro/public/api/v1/purchase-requests/1213/items/7/delivery-requirements"
      }
    ]
}

purchase-requests/1741/items/1/delivery-requirements

{
  "results": [
    {
      "deliveryRequirementNumber": 1,
      "requirementDate": "2026-01-23",
      "requirementQuantity": 100,
      "attendedQuantity": 0,
      "openQuantity": true
    }
  ],
  "resultSetMetadata": {
    "count": 1,
    "offset": 0,
    "limit": 100
  },
  "links": [
    {
      "rel": "self",
      "href": "https://api.sienge.com.br/rioclaro/public/api/v1/purchase-requests/1741/items/1/delivery-requirements?limit=100"
    }
  ]
}
```

Dados de Painel de Compras para API:

- Nº de solicitação →purchaseRequestId (/purchase-requests/all/items)
- Grupo de Insumo →?
- Data de Chegada a Obra → **requirementDate** (purchase-requests/1741/items/1/delivery-requirements)
- Data da solicitação →requestDate (/purchase-requests/{id})
- Situação da solicitação → status (/purchase-requests/{id})
- Data autorização da solicitação → ?
- Situação autorização do item →authorized e disapproved (/purchase-requests/all/items)
- Data do Pedido → date (purchase-orders/{id})
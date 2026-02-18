---
hide:
  - toc
---

# 2. Módulo Financeiro

É uma das APIs mais robustas, focada em fluxo de caixa e movimentações.

- **Contas a Pagar:** Inclusão de títulos, parcelas (Installments) e baixas.
- **Contas a Receber:** Gestão de recebíveis de vendas de unidades ou serviços.
- **Caixa e Bancos:** Extratos, transferências e conciliação bancária.
- **Planejamento Financeiro:** Categorias financeiras e orçamentos correntes.

- Contas a Pagar
    
    Endpoints:
    
    [httpsapi.sienge.com.brrioclaropublicapiv1/bills](httpsapi.sienge.com.brrioclaropublicapiv1/bills)
    
    [httpsapi.sienge.com.brrioclaropublicapibulk-datav1outcome/by-bills](httpsapi.sienge.com.brrioclaropublicapibulk-datav1outcome/by-bills)
    
    É possível puxar todos os títulos do sienge, onde a partir deles podemos fazer uma busca através da API BULK, onde é possível trazer todas as parcelas daqueles títulos.
    
    Dados obtidos:
    
    ## 1. Identificação e Hierarquia Organizacional
    
    *Campos que definem a qual empresa, projeto ou grupo a parcela pertence.*
    
    | **Campo** | **Tipo** | **Descrição** |
    | --- | --- | --- |
    | `companyId` / `companyName` | Integer / String | Código e Nome da empresa |
    | `groupCompanyId` / `groupCompanyNam` | Integer / String | Código e Nome do grupo da empresa |
    | `holdingId` / `holdingName` | Integer / String | Código e Nome da holding |
    | `subsidiaryId` / `subsidiaryName` | Integer / String | Código e Nome da subsidiária |
    | `businessAreaId` / `businessAreaName` | Integer / String | Código e Nome da área de negócio |
    | `projectId` / `projectName` | Integer / String | Código e Nome do projeto |
    | `businessTypeId` / `businessTypeName` | Integer / String | Código e Nome do tipo de negócio |
    
    ## 2. Dados da Parcela (Installment)
    
    *Informações específicas do título e documento.*
    
    | **Campo** | **Tipo** | **Descrição** |
    | --- | --- | --- |
    | `billId` / `installmentId` | Integer | Código do título e da parcela |
    | `creditorId` / `creditorName` | Integer / String | Código e Nome do credor |
    | `documentIdentificationId` | String | Código do documento |
    | `documentNumber` | String | Número do documento |
    | `forecastDocument` | String | Documento de previsão financeira |
    | `consistencyStatus` | String | Status (I = Inclusão, N = Incompleto, S = Completo) |
    | `authorizationStatus` | String | Status de autorização (S = Sim, N = Não) |
    | `originId` | String | Código da origem |
    
    ## 3. Valores e Indexadores
    
    *Dados financeiros e monetários.*
    
    | **Campo** | **Tipo** | **Descrição** |
    | --- | --- | --- |
    | `originalAmount` | Number (Double) | Valor original da parcela |
    | `discountAmount` | Number (Double) | Valor de desconto do título |
    | `taxAmount` | Number (Double) | Valor total do imposto retido |
    | `balanceAmount` | Number (Double) | Valor do saldo |
    | `correctedBalanceAmount` | Number (Double) | Valor do saldo corrigido |
    | `indexerId` / `indexerName` | Integer / String | Código e Nome do indexador |
    
    ## 4. Datas e Auditoria
    
    *Prazos e registros de criação.*
    
    | **Campo** | **Tipo** | **Formato** | **Descrição** |
    | --- | --- | --- | --- |
    | `dueDate` | Date | yyyy-MM-dd | Data de vencimento |
    | `issueDate` | Date | yyyy-MM-dd | Data de emissão |
    | `billDate` | Date | yyyy-MM-dd | Data de competência |
    | `registeredDate` | DateTime | ISO 8601 | Data de criação no sistema |
    | `registeredBy` | String | - | Nome do usuário que criou |
    
    ## 5. Detalhamentos (Listas Aninhadas)
    
    *Estes itens aparecem como sub-listas para cada parcela no Notion.*
    
    - Segue abaixo:
        
        ### Categorias de Pagamentos (`paymentsCategories`)
        
        - **costCenterId / Name:** Centro de custo.
        - **financialCategoryId / Name:** Plano financeiro.
        - **financialCategoryRate:** Porcentagem de rateio.
        
        ### Custos por Obra (`buildingsCosts`)
        
        - **buildingId / Name:** Código e nome da obra.
        - **buildingUnitId / Name:** Unidade construtiva.
        - **costEstimationSheetId:** Item de orçamento.
        - **rate:** Percentual de apropriação.
        
        ### Pagamentos Realizados (`payments`)
        
        - **operationTypeName:** Tipo da baixa.
        - **grossAmount / netAmount:** Valor bruto e líquido.
        - **interest / fine / discount:** Juros, multa e desconto.
        - **paymentDate:** Data do pagamento.
        - **bankMovements:** Movimentações bancárias relacionadas.
        
        ### Autorizações (`authorizations`)
        
        - **authorizationUserName:** Quem autorizou.
        - **authorizationDate:** Quando autorizou.
        - **isLastToAuthorize:** Indica se finalizou o fluxo de aprovação.
    
- Contas a Receber
    
    Endpoints:
    
    [https://api.sienge.com.br/rioclaro/public/api/v1/bills](https://api.sienge.com.br/rioclaro/public/api/v1/bills)
    
    [https://api.sienge.com.br/rioclaro/public/api/bulk-data/v1/income/by-bills](https://api.sienge.com.br/rioclaro/public/api/bulk-data/v1/income/by-bills)

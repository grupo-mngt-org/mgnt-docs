## O que é o Evolution API
Evolution API é uma plataforma que age como hub para gerencias integrações de comunicação, em especial com o Whatsapp. É uma ferramenta open source e self hosted.

## Vantagens de usar o Evolution API
- É open source, logo, gratuito para uso.
- Suporta tanto a implementação não oficial de integração com o Whatsapp (Whatsapp Baileys) como a integração oficial, o que permite manter as configurações e apenas "trocar" para o uso da API oficial, por exemplo.
- Tem nó para integrar com n8n desenvovlvido pela comunidade, funcional.
- É fácil, intuitivo e gerenciável tanto via interface quanto via API REST.

## Uso para o Grupo MNGT
Inicialmente, o Evolution API será usado para automatizações de comunicações internas da empresa, usando a API não oficial do Whatsapp (Whatsapp Baileys). Para outros fins, ou caso a implementação não oficial deixe de atender,
será usado a API oficial, que será futuramente configurada para um CNPJ do Grupo.

Uma vez que o uso inicial se dá por meio de API não oficial (e mesmo usando a API oficial é importante ter cuidados também para não ser classificado como spam), para evitar bloqueios é importante tentar tomar alguns cuidados:
- Se possível, não usar um número totalmente novo, mas sim usar um número aquecido.
- Não enviar muitas mensagens de uma vez, talvez 10-15 por minuto no máximo. Usar filas e/ou sleep para que as mensagens não sejam enviadas todas ao mesmo tempo.

## Como usar a interface
Para usar o Evolution API do Grupo MNGT, basta acessar o endereço http://198.27.97.43:8080/manager.
Para login, basta inserir a API Key do Evolution API que está disponível na seção de credencias dessa página de documentação.

### Criando instâncias
Ao se autenticar na plataforma, é possível ver as instâncias qeu existem, bem como clicar no botão para criar uma nova instância
<img width="1841" height="533" alt="image" src="https://github.com/user-attachments/assets/76c963eb-a22c-4368-a9b5-e7a5685ab0fd" />

Após clicar, será aberto um modal, onde possível inserir um nome que vai identificar essa instância, um Canal (por ora, deixaremos sempre selecioa o Baileys, que é a API não ofiicial do Whatsapp que usaremos) e o número de telefone que
vai se conectar com essa instância, com o código 55 do país na frente.
<img width="698" height="535" alt="image" src="https://github.com/user-attachments/assets/cad7e968-e02b-4fe1-beaf-f2d119672fd2" />

Após criar a instância, bastar entrar nela e clicar em Get QR Code para gerar um QR Code. Esse QR Code é para conexão para Whatsapp Web, e deve ser lido no aplicativo do Whatsapp pelo celular que tem o número definido ao criar a instância.
Feito isso, essa instância já pdoe ser usada para controalr o whatsapp desse número por meio da Evolution API.

## Como integrar ao n8n
Já existe um nó criado pela comuidade, pronto para integrar a Evolution API. Após criar a instância, basta adicionar esse nó no workflow, usar a credencial com a API Key do Evolution API, e informar ação, o nome da instância a ser
utilizada e outras informaçẽos relativa a ação em específico. Abaixo segue um exemplo simples de envio de mensagem de texto, que é possível digitar um mensagem no chat do n8n que é enviada para um número do Whatsapp informado.
<img width="1632" height="668" alt="image" src="https://github.com/user-attachments/assets/7de66fe1-01ee-48e9-b76c-054f205cafe5" />
<img width="1810" height="618" alt="image" src="https://github.com/user-attachments/assets/cefd75a8-467d-41a6-9300-c73333cbf8c6" />
<img width="281" height="121" alt="image" src="https://github.com/user-attachments/assets/ce1d989a-86e4-456a-a1ba-8263fc92ef6a" />


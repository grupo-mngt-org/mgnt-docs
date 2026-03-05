# Cadastro Único - MNGT

O objetivo é construir um sistema único de cadastro de pessoas, que armazene os dados dos colaboradores e integre o cadastro dessas pessoas em todos os sistemas usados pela empresa.

Sistemas:
- D-Guard
- Discord
- Sienge
- Prevision
- Mobuss
etc...

A proposta é que esse sistema possa funcionar via bot no Discord, usando OpenAI e uma automação n8n

Funcionaria em um canal específico que só RH, Direção e etc teriam acesso, pode se chamar por exemplo #cadastro-de-pessoas

## Cadastro de nova pessoa

Usuário manda mensagem solicitando a criação de uma nova pessoa no sistema e fornece dados. Ao fim, essa epssoa é cadastrada no banco de dados.

Exemplo de diálogo:

- "Cadastre o colaborador Amanda Felisberto"
- "Para completar o cadastro, faltam os seguintes dados: Numero de whatsapp, CPF..."

## Consulta de pessoas existentes

Usuário solicita a lista de pessoas existentes e ela é retornada em pdf, xlxs ou csv (de acordo com o que o que for mais conveniente).

Exemplo de dialogo:

"Me liste todas as pessoas que estão no sistema"

## Edição de pessoas existentes

## Deleção de pessoas existentes

## Outras operações

Tipos de pergunta que o usuário poderia faze o bot tem que ser capaz de responder:
- Quais pessoas não estão cadastradas no Discord?
- Quais pessoas não estão cadastradas no D-Guard?
- Quem é a pessoa responsável por Compras na empresa?


## Interface:
Uma paǵina que liste as pessoas cadastradas e dê opção de exportar esses dados, e faça as mesmas operações que o bot do Discord, mas a partir de um chat presente na página

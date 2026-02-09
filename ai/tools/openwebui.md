Esse documento tem por fim trazer o entendimento sobre a plataforma OpenWebUI, seu uso, diferenças para o ChatGPT e aplicações possíveis para o Grupo MNGT. Em constante atualização.

## Introdução
OpenWebUI é uma ferramenta open source que pode ser usada como alternativa a interface, por exemplo, do ChatGPT. É possível gerenciar uma instância de maneira self-hosted (em um servidor próprio, com total controle do usuário ou empresa),
que se conecta com modelos de IA como OpenAi, Claude, etc. ou até com modelos open source, como o Ollama, que é recomendado.

## Materiais complementares
- [Documentação oficial do OpenWebUI](https://docs.openwebui.com/)
- Vídeo: [Open WebUI: Local ChatGPT Alternative | For Complete Begineers | Full Tutorial](https://www.youtube.com/watch?v=jepjWSv8YCU) - Tutorial que explora instalação e features do OpenWebUI.

## OpenWebUI no Grupo MNGT
O objetivo atual é utilizar o OpenWebUI para substituir o uso do ChatGPT, para a empresa inteira, sem limitações de plataforma do ChatGPT, em um servidor próprio utilizando a capacidade de multiplos usuáarios.

Empresas:
- Área Incrível: http://198.27.97.43:3000/
- Mais Armazém: (Em Breve)

Modelos:
- Atualmente, o único modelo utilizado para o Grupo MNGT é o gpt-5.2-pro, conectado usando a API key do OpenAI da empresa.

## OpenWebUI x ChatGPT

### Principais diferenças
1. *Filosofia e Hospedagem*
Open WebUI: É auto-hospedado (instala no próprio computador ou servidor) e pode operar totalmente offline. Isso garante privacidade total, pois os dados não saem da  máquina.
ChatGPT: É um serviço em nuvem hospedado pela OpenAI. Seus dados e conversas são processados e armazenados nos servidores da OpenAI. 
2. *Modelos de IA (IA Agnóstica)*
Open WebUI: É "agnóstico a modelos", o que significa que é possível conectar o Open WebUI a diversos modelos, incluindo Ollama (para rodar modelos locais como Llama 3, Mistral), OpenAI, Anthropic e outros, tudo na mesma interface.
ChatGPT: Está estritamente limitado aos modelos da OpenAI (GPT-3.5, GPT-4, GPT-4o, etc.). 
3. *Custo*
Open WebUI: O software é gratuito. Ao usá-lo com Ollama (local), o custo é apenas o do hardware. Se usar APIs de terceiros, paga apenas pelos tokens consumidos.
ChatGPT: O uso gratuito é limitado, e recursos avançados exigem uma assinatura mensal (ChatGPT Plus). 
4. *Funcionalidades e Personalização*
Open WebUI: Oferece RAG (Retrieval-Augmented Generation) integrado, permitindo carregar documentos (PDFs, docs) para a IA analisar. Inclui também suporte para busca na web em tempo real, reconhecimento de voz e
forte customização de "personas" (prompts de sistema).
ChatGPT: Possui funcionalidades robustas e polidas, mas com menos controle sobre o prompt de sistema e customização da interface em comparação ao Open WebUI. 

### O que existe em um e não existe no outro:
#### OpenWebUI
| Funcionalidade | Existe no ChatGPT? | Notas |
| :--- | :--- | :--- |
| Chat | Sim | |
| Pastas | Sim | |
| Notas | Não | |
| Espaço de Trabalho | Não | |
| Base de Conhecimento | De outra forma | É equivalente a usar o GPT Builder. [Esse artigo] fala bem sobre base de conhecimento no ChatGPT. |
| Multimodelos | Não | |
| Multiusuários | Sim | Apenas no plano empresarial |

#### ChatGPT
| Funcionalidade | Existe no OpenWebUI? | Notas |
| :--- | :--- | :--- |
| Chat | Sim | |
| Pastas | Sim | |
| Extended Thinking | Não | Em análise sobre como implementar equivalente no OpenWebUI |
| Projetos | Não | |
| Aplicativos | Não | |

## Funcionalidades
### Espaço de Trabalho (Workspace)
Painel centralizado de recursos e gerenciamento, projetado para organizar e aprimorar as interações com modelos de IA (LLMs). Ele funciona como o "centro de controle" ou uma área de trabalho onde você pode criar, 
gerenciar e personalizar seus próprios agentes, documentos e instruções
### Notas
Para textos que existem de maneira única ao invés de um chat, em que o LLM também pode escrever e melhorar, como se fosse a IA em um editor de código. Pareceu ainda experimental.
### Base de Conhecimento
### Gestão de usuários
#### Funções (Roles)
- **Admin**: Tem acesso irrestrito e controla outros usuários e configurações através do Painel do Admin.
- **User/Usuário**: Tem acesso restrito e controlado através de Permissões e Grupos.
- **Pending/Pendente**: Usuário que ainda não teve acesso liberado.

#### Grupos
Permite organizar usuários para controle de acesso em escala, gerenciando Permissões e acesso de controle a recursos.

#### Permissões
Uma permissão pode dar controle de acesso fino de uma funcionalidade. É importante notar que permissões no OpenWebUI são aditivas, portanto se um usuário está em pelo menos grupo que dá a ele determinada permissão, então ele tem essa
permissão, ela não pode ser "negada".

## Problemas conhecidos
### Chat não consegue continuar após erro de ação incompatível com modelo selecionado
Os chats do OpenWebUI são multi modelos, os modelos podem ser modificados durante a conversa, porém ao mudar o modelo e dar erro, o chat para e trava. Mesmo mudando para outro modelo, o chat não consegue continuar. 
Vai ser preciso orientar ou forçar os usuários a usar sempre o modelo correto durante o chat.
<img width="1306" height="867" alt="image" src="https://github.com/user-attachments/assets/df0cfb92-caa2-481c-8574-3aa39a69d659" />

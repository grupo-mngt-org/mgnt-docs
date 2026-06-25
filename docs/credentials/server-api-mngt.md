---
hide:
  - toc
---

# Servidor APIMNGT

## Dados de Acesso

## Máquina 1

> IP: `{{SERVER_API_MNGT_IP_1}}`<br>
> Usuário: `{{SERVER_API_MNGT_USER_1}}`<br>
> Senha: `{{SERVER_API_MNGT_PASS_1}}`<br>
> SSH: `{{SERVER_API_MNGT_SSH_CMD_1}}`<br>
> Pasta com configs: `etc/nginx/sites-enable`

## Máquina 2

> IP: `{{SERVER_API_MNGT_IP_2}}`<br>
> Usuário: `{{SERVER_API_MNGT_USER_2}}`<br>
> Senha: `{{SERVER_API_MNGT_PASS_2}}`<br>
> SSH: `{{SERVER_API_MNGT_SSH_CMD_2}}`<br>
> Pasta com configs: `etc/nginx/sites-enable`

## Comandos

- `rebuild` = faz com que dê o pull no código e levante o servidor novamente
- `sudo nginx -t` = Testa a sintaxe da configuração
- `sudo systemctl status nginx` = verifica o status após as mudanças
- `sudo systemctl restart nginx` = reinicia para aplicar mudanças

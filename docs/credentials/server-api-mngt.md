---
hide:
  - toc
---

# Servidor APIMNGT

## Dados de Acesso

> IP: `{{SERVER_API_MNGT_IP}}`<br>
> Usuário: `{{SERVER_API_MNGT_USER}}`<br>
> Senha: `{{SERVER_API_MNGT_PASS}}`<br>
> SSH: `{{SERVER_API_MNGT_SSH_CMD}}`<br>
> Pasta com configs: `etc/nginx/sites-enable`

## Comandos

- `rebuild` = faz com que dê o pull no código e levante o servidor novamente
- `sudo nginx -t` = Testa a sintaxe da configuração
- `sudo systemctl status nginx` = verifica o status após as mudanças
- `sudo systemctl restart nginx` = reinicia para aplicar mudanças


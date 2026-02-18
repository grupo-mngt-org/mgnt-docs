---
hide:
  - toc
---

# Caiu de paraquedas no projeto? Vamos as configurações!

!!! warning
    #### Antes de prosseguir, é necessário configurar a chave SSH. Certifique-se de que você já fez isso. Se não, faça este passo antes ou solicite a ajuda da equipe.

### Atualização APT-GET

=== "Ubuntu"
    ```shell
    sudo apt-get update
    ```
=== "Debian"
    ```shell
    sudo apt-get update
    ```
=== "Arch"
    ```shell
    sudo pacman -Syu
    ```

### Instalação de Pacotes Essenciais

=== "Ubuntu"
    ```shell
    sudo apt-get install -y git-core zlib1g-dev build-essential NetworkManager libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev micro libmysqlclient-dev mysql-client-core-8.0 libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libnss3 libxss1 libasound2 libxtst6 xauth xvfb libbz2-dev
    ```
=== "Debian"
    ```shell
    sudo apt-get install -y git zlib1g-dev build-essential curl libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev micro libmariadb-dev-compat libmariadb-dev mariadb-server mariadb-client-core libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libnss3 libxss1 libasound2 libxtst6 xauth xvfb libbz2-dev
    ```
=== "Arch"
    ```shell
    sudo pacman -S git zlib base-devel openssl readline libyaml sqlite libxml2 libxslt curl libffi micro mariadb-libs gtk2 gtk3 mesa libnotify nss libxss alsa-lib libxtst xorg-xauth xorg-server-xvfb bzip2
    ```

### Instalação ASDF (Gerenciador de pacotes)

```shell
cd
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0
echo '. "$HOME/.asdf/asdf.sh"' >> ~/.bashrc
echo '. "$HOME/.asdf/completions/asdf.bash"' >> ~/.bashrc
echo 'legacy_version_file = yes' >> ~/.asdfrc
source ~/.bashrc
```

### Adicionando RUBY, NODE e PYTHON

```shell
asdf plugin add nodejs
asdf plugin add python
```


### Instalação NodeJS
> :bulb: **Dica**: Esta etapa é demorada, vá buscar uma água!
```shell
asdf install nodejs 20.9.0
asdf global nodejs 20.9.0
```

### Instalação Python (para documentação)
> :bulb: **Dica**: Também demora um pouco... aproveite para ir ao banheiro!
```shell
asdf install python 3.11.0
asdf global python 3.11.0
```


### Verifique se tudo correu bem

```shell
which node && node -v && which python && python --version
```

> :information_source: A etapa acima deve retornar o seguinte:
 
```{: .txt .no-copy}
/home/mercado/.asdf/shims/node
v20.9.0
/home/mercado/.asdf/shims/python
Python 3.11.0
```

### Atualizar NPM e instalar o Yarn
```shell
npm install -g npm@10.5.0
npm install -g yarn
```

### Instalação do Docker [NO CASO DE WSL, USE O DOCKER DESKTOP NO WINDOWS]

=== "Ubuntu"
    ```shell
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    rm get-docker.sh
    ```
=== "WSL"

    - Instalar Docker Desktop: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

    - Configure no Docker Desktop:

    ```text
    CONFIGS > GENERAL
    [x] Use the WSL 2 based engine

    CONFIGS > RESOURCES > WSL INTEGRATION
    [x] Enable integration with my default WSL distro
    [x] Enable integration with additional distros (selecione suas distros)
    ```

### Adicionando o usuário ao grupo Docker

```shell
sudo usermod -aG docker ${USER}
```

### Nova sessão com o usuário já no grupo Docker

```shell
exec su -l ${USER}
```

---

# **FIM!** 🙂

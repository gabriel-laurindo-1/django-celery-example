# Django + Celery com brocker RabbitMQ

Exemplo de utilização do Django utilizando celery com o brocker RabbitMQ.

---

## Preparação do ambiente virtual

---
Execute a seguinte sequência de comandos no seu terminal de comando.

~~~bash
# Cria da pasta do virtualenv
$ virtualenv <nome_ambiente>

# ativação do ambiente virtual
$ <nome_ambiente>\Scripts\activate

# instalação dos pacotes
$ pip install -r requirements.txt
~~~

---

## Instalação do RabbitMQ

No site oficial do [RabbitMQ](https://www.rabbitmq.com/download.html) você pode encontrar a explicação completa sobre como instalar o RabbitMQ para Windows, MAC e Linux.

Porém, para instalar no Windows você percisa somente executar os seguintes passos:

- Baixe o RabbitMQ para Windows: [Clique aqui!](https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.7/rabbitmq-server-3.8.7.exe)

- Baixe o ERLang de acordo com o sistema operacional: [Clique aqui!](https://www.erlang.org/downloads)

- Execute <strong>primeiramente</strong> o instalador do ERLang como adminstrador e siga os passos de instalação normalmente.

- Após o fim da instalação do ERLang, instale o RabbitMQ de forma semelhante.

- Ao concluir a instalação do RabbitMQ, execute o programa "RabbitMQ Command Prompt (sbin dir)".

- Dentro do terminal do RabbitMQ Command Prompt (sbin dir), digite os seguintes comandos:

~~~bash
# Comando 1
rabbitmq-plugins enable 

# Comando 2
rabbitmq_management
~~~

- Em seu navegador de internet, acesse http://localhost:15672/

- Para conectar ao seu painel de gerenciamento do RabbitMQ utilize:

~~~
Username: guest
Password: guest
~~~

---

## Iniciando o Celery

No terminal digite uma das linhas de comando abaixo para iniciar o celery utilizando o eventlet ou o gevent:

~~~bash
# utiliando eventlet
$ celery -A <project_name> worker -l info -P eventlet

# utilizando gevent
$ celery -A <project_name> worker -l info -P gevent 
~~~

---

## Iniciando o Django

Para executar o projeto no Django, digite o comando abaixo no terminal de seu ambiente virtual.

~~~bash
# Preparar as migrações necessárias
$ python manage.py makemigrations

# Executar as migrações
$ python manage.py migrate

# Iniciar aplicação do Django
$ python manage.py runserver
~~~

---

<p align=center> Desenvolvido por <a href="https://github.com/gabriel-laurindo-1" title="Gabriel Laurindo">Gabriel Laurindo</a></p>
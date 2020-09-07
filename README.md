# API Flask

Utilizando Flask para API Backend, e as seguintes ferramentas:

- Flask
- sqlite3
- pytest
- SQLAlchemy

## Instalação
Preparação de ambiente da aplicação.
Para aplicação é indicado rodar em um ambiente isolado, uma [virtualenv](https://docs.python.org/pt-br/dev/library/venv.html).
Requisitos:

* Python 3.6+


Com o ambiente virtual ativado instale as dependências com o seguinte comando no terminal:
```shell
$ pip install -r requirements.txt
```

## Criação do banco de dados
Entre no python shell com o comando 'python'.
Digite os comandos:

```shell
$ from app import db
$ db.create_all()
```
Em seguida aparecerá um arquivo com extensão .sqlite3 na raiz do projeto.
Para visualização dos registros pode-se utilizar o programa [DB Browser](https://sqlitebrowser.org/)


## Como executar o projeto

Vamos executar os comandos abaixo partindo que esteja no diretório raiz onde fez o clone do projeto.
```sh
python app.py
```

### Inserindo Transações

Para criar uma entrada no banco iremos utilizar o path abaixo em algum aplicativo como Postman ou Insomnia

```sh
http://localhost:5000/transaction
```

Via metódo POST, passaremos o corpo do objeto JSON a ser inserido
## Requisição
```json
{
   "estabelecimento": "45.283.163/0001-69",
   "cliente": "094.214.930-01",
   "valor": 10.5,
   "descricao": "compra via Shipay, Supermercado"
}
```
## Resposta
```json
{
  "aceito": true
}
```

## Testes

*Aplicação possui 6 testes.*

- Verificação de retorno status code metodo não permitido como GET.

- Verificação de retorno status code envio de corpo JSON vazio.

- Verificação de retorno status code criação de registro no banco de dados.

- Verificação de retorno de copo da requisição de criação de registro.


- Verificação de retorno status code com envio de JSON com alguns campos vazios.

- Verificação de registro no banco de dados.


## Como executar os testes

Vamos executar os comandos abaixo partindo que esteja no diretório raiz onde fez o clone do projeto.
```sh
py.test
```
# Book Search Application

## Descrição

Este é um projeto Django para gerenciar e buscar informações sobre livros a partir de um arquivo CSV. O projeto inclui um backend desenvolvido com Django e Django REST Framework.

## Pré-requisitos

Certifique-se de ter o seguinte instalado em sua máquina:

- Docker
- Docker Compose
- Make (opcional, mas recomendado)

## Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd book-search
```
#### 1.1 Se for a primeira vez que estiver usando, execute primeiro o script:
```
    $ make migrate
    $ make up
```
Entre na maquina docker gerada e execute o comando de criar superusuário.
```
    $ docker exec -ti book-search-web-1 bash
    $ python src/manage.py createsuperuser
```
Com o email e senha inseridos entre no sistema de admin:
[Admin](http://localhost:8000/admin/)

Lá você terá acesso a criação de usuários, inserção e edição de livros manualmente.

Você pode criar novos usuários também via URL:
```
curl --location 'http://localhost:8000/api/register/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzk5MDY4LCJpYXQiOjE3MjMzOTg3NjgsImp0aSI6IjExYWFlNWUzZTAwNDQ4ZGI5ZTg1ZmUyZjY3NThjODUyIiwidXNlcl9pZCI6MX0.RzuAFmu7E1jCknHA2BrE3EeEV6OIkJlgLQvcsrVpfjU' \
--data-raw '
{
    "username": "novo_usuario",
    "password": "senha_segura123",
    "email": "novo_usuario@example.com",
    "first_name": "Nome",
    "last_name": "Sobrenome"
}'

```
### Para executar você pode rodar
```
$ make up
```
### Para executar os testes
```
$ make test
```
### Helps
```
$ make help
```

## Para usar
### Pegar as informações de token
```
curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{"username": "root", "password": "pass"}'
```
#### Response
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzU0OTI1OSwiaWF0IjoxNzIzNDYyODU5LCJqdGkiOiI5N2U4M2I5ZjM1YWQ0M2IzOTM4MWVjOWViNDNlMDBkYyIsInVzZXJfaWQiOjF9.sevCLOpPo8TRMUvyi3uHSVvi4cJl2-Dqdw9ME9XVDvI",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNDYzMTU5LCJpYXQiOjE3MjM0NjI4NTksImp0aSI6ImQwNzQ0M2E4Y2E5MTQ0OGE5NWMyNWIwYjM0NjUzZWZhIiwidXNlcl9pZCI6MX0.dEs5A605NGw38JjxcJ--P3IRsHFoZgdTjr0iC-pW1Hg"
}
```

### Processamento de CSV em massa
#### Enviar o CSV
Para fazer um envio em massa você acessa o endpoint para enviar o csv
```
curl --location 'http://localhost:8000/api/csv/upload/' \
--header 'Content-Type: application/json' \
--data '{"csv_file": "data_csv" }
```
O formato do CSV_FILE deve ser base64. O arquivo CSV deve ser convertido a Base64. 

É preciso cadastrar em variavel de ambiente também as variáveis:
SENDGRID_API_KEY = 'A variável da Key do Sendgrid'
SENDGRID_EMAIL = 'Email para qual será enviado o email'

### Fazer busca na API
#### Fazer a busca de elementos já cadastrados
Para fazer a busca de elementos dentro do sistema é possível fazer com o seguinte request:
```
curl --location 'http://localhost:8000/api/books/?isbn=141439661' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzk5OTg0LCJpYXQiOjE3MjMzOTk2ODQsImp0aSI6ImE1YWQzZDY1ZjAzZDRmYTg5ZGI2YWRiMDZjOGI3YWQ5IiwidXNlcl9pZCI6MX0.AuRh-NXR8QUqN_LShtevnLQmkXOOy_75hKcz2rjF1ZU' \
--data ''
```
Os seguintes campos são possíveis de serem buscados: Title, Authors and ISBN
```
curl --location 'http://localhost:8000/api/books/?title=Harry%20Potter' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzk5OTg0LCJpYXQiOjE3MjMzOTk2ODQsImp0aSI6ImE1YWQzZDY1ZjAzZDRmYTg5ZGI2YWRiMDZjOGI3YWQ5IiwidXNlcl9pZCI6MX0.AuRh-NXR8QUqN_LShtevnLQmkXOOy_75hKcz2rjF1ZU' \
--data ''
```
```
curl --location 'http://localhost:8000/api/books/?authors=Jane%20Austen' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzk5OTg0LCJpYXQiOjE3MjMzOTk2ODQsImp0aSI6ImE1YWQzZDY1ZjAzZDRmYTg5ZGI2YWRiMDZjOGI3YWQ5IiwidXNlcl9pZCI6MX0.AuRh-NXR8QUqN_LShtevnLQmkXOOy_75hKcz2rjF1ZU' \
--data ''
```
```
curl --location 'http://localhost:8000/api/books/?isbn=439554934' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzk5OTg0LCJpYXQiOjE3MjMzOTk2ODQsImp0aSI6ImE1YWQzZDY1ZjAzZDRmYTg5ZGI2YWRiMDZjOGI3YWQ5IiwidXNlcl9pZCI6MX0.AuRh-NXR8QUqN_LShtevnLQmkXOOy_75hKcz2rjF1ZU' \
--data ''
```

### Docs
[Link para documentação](https://documenter.getpostman.com/view/4020852/2sA3s4kVcj)
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
### Docs
[Link para documentação](https://documenter.getpostman.com/view/4020852/2sA3s4kVcj)
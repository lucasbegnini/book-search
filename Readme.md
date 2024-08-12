# Book Search Application

## Description

This is a Django project to manage and search for book information from a CSV file. The project includes a backend developed with Django and the Django REST Framework.

## Prerequisites

Make sure you have the following installed on your machine:

- Docker
- Docker Compose
- Make (optional, but recommended)

## Environment Setup

### 1. Clone the repository

```bash
git clone <URL_DO_REPOSITORIO>
cd book-search
```
#### 1.1 If this is your first time using it, run the script first:
```
    $ make migrate
    $ make up
```
Enter the generated docker machine and run the create superuser command.
```
    $ docker exec -ti book-search-web-1 bash
    $ python src/manage.py createsuperuser
```
With the email and password entered, enter the admin system:
[Admin](http://localhost:8000/admin/)

There you will have access to create users, insert and edit books manually.

You can also create new users via URL:
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
### To run
```
$ make up
```
### To run the tests
```
$ make test
```
### Helps
```
$ make help
```

## To use
### Get token information
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

### Bulk CSV Processing
#### Send CSV
To make a mass sending you access the endpoint to send the csv
```
curl --location 'http://localhost:8000/api/csv/upload/' \
--header 'Content-Type: application/json' \
--data '{"csv_file": "data_csv" }
```
The CSV_FILE format must be base64. The CSV file must be converted to Base64.

You must also register the following variables in the environment variable:
SENDGRID_API_KEY = 'The Sendgrid Key variable'
SENDGRID_EMAIL = 'Email to which the email will be sent'

### Search the API
#### Search for elements already registered
To search for elements within the system, you can do so using the following request:
```
curl --location 'http://localhost:8000/api/books/?isbn=141439661' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzk5OTg0LCJpYXQiOjE3MjMzOTk2ODQsImp0aSI6ImE1YWQzZDY1ZjAzZDRmYTg5ZGI2YWRiMDZjOGI3YWQ5IiwidXNlcl9pZCI6MX0.AuRh-NXR8QUqN_LShtevnLQmkXOOy_75hKcz2rjF1ZU' \
--data ''
```
The following fields are searchable: Title, Authors and ISBN
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
# Voter bot

Three bots to conduct elections

## Features

1. authenticated users (only superuser) can include voters and candidates
2. authenticated users can vote

## Tables

1. Voters
2. Candidates

### Schema

Voter:

| name       | type | description                     |
| ---------- | ---- | ------------------------------- |
| id         | int  | primary key                     |
| username   | str  | unique telegram username        |
| first_name | str  | User first name                 |
| last_name  | str  | User last name                  |
| Position   | str  | Job position                    |
| dapartment | str  | Department of the place of work |

Candidates:

| name       | type  | description                     |
| ---------- | ----- | ------------------------------- |
| id         | int   | primary key                     |
| username   | str   | unique telegram username        |
| first_name | str   | User first name                 |
| last_name  | str   | User last name                  |
| Position   | str   | Job position                    |
| dapartment | str   | Department of the place of work |
| voter      | Voter | Associated with the voter table |
| yes        | int   | the number of yes votes         |
| no         | int   | the number of yes votes         |

## Libraries used

- Django
- python-telegram-bot
- Django-import-export

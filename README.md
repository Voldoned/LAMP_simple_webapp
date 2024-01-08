# LAMP_project

## Services

server: Apache 2

db: MySQL 5.7

site: php 8.2, laravel 10

tests: Python 3.10 (pytest, locust)

## URLs

### web.php

GET-requests:

- /test;
- /test/create;
- /test/delete;
 
POST-requests:

- /test/post;
- /test/create/post;
- /test/delete/post;

### api.php

GET-requests:

- /api/tests;

POST-requests:

- /api/test/create/post;
- /api/test/delete/post;

# Running project

Create in work directory file '.env' with variables for mysql root and database user:
- 'ROOT_USER'
- 'ROOT_PASSWORD'
- 'LARAVEL_USER'
- 'LARAVEL_PASSWORD'

And install lib 'pydantic-settings'
```bash
pip install pydantic-settings
```

Run in directory with project:
```bash
python3 start.py
```
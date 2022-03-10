# ToDo-API

## How to debug.

1. Clone.

```bash
git clone https://github.com/chun37/todo-api.git
```

2. Install dependencies.

```bash
pipenv install
```

3. Copy .env file.

```bash
cp .env-sample .env
```

4. Generate secret key.

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

5. Write the key to an .env file.

6. Run!!!!

```bash
pipenv run python manage.py runserver
```

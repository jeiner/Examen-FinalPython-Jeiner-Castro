### Configuración del proyecto

1.-  You need create virtual env:

```sh
$ python3.8 -m venv env
$ source env/bin/activate
```

2.-  you need install requirements.txt

```sh
$ pip install -r requirements.txt
```

3.-  you need execute migrations

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
4.-  create environment variable, and configure variables

```sh
$ touch .env
$ cp .env.example .env
```

4.- run project
```sh
$ python manage.py runserver
```



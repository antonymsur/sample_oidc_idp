# Sample provider using `django-oidc-provider` package.

## Setup & Running

- [Manually](#manually)
- [Using Docker](#using-docker)

### Manually

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
# For Python 2.7.
$ virtualenv project_env
# Or Python 3.
$ virtualenv -p /usr/bin/python3.4 project_env

$ source project_env/bin/activate

$ git clone https://github.com/juanifioren/django-oidc-provider.git
$ cd django-oidc-provider/example_project
$ pip install -r requirements.txt
```

Run your provider.

```bash
$ python manage.py migrate
$ python manage.py creatersakey
$ python manage.py runserver
```

### Using Docker

Build and run the container.

```bash
$ docker build -t django-oidc-provider .
$ docker run -d -p 8000:8000 django-oidc-provider
```

## Install package for development

After you run `pip install -r requirements.txt`.
```bash
# Remove pypi package.
$ pip uninstall django-oidc-provider

# Go back and add the package again.
$ cd ..
$ pip install -e .
```

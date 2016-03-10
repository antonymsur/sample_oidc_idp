# Sample provider using django-oidc-provider package.

## Setup & Running

### Manually

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
# For Python 2.7.
$ virtualenv project_env
# Or Python 3.
$ virtualenv -p /usr/bin/python3.4 project_env

$ source project_env/bin/activate

$ pip install -r requirements.txt
```

Run your provider.

```bash
$ python manage.py migrate
$ python manage.py creatersakey
$ python manage.py runserver
```


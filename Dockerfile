FROM python:2-onbuild

RUN [ "python", "manage.py", "migrate" ]
RUN [ "python", "manage.py", "creatersakey" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0" ]

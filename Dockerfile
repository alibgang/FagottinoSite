FROM python:3
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir -p /src
RUN mkdir -p /config
WORKDIR /src
ADD ./src /src
RUN pip install -r requirements.pip
RUN pip install --upgrade pip

RUN sleep 2
RUN pipenv lock --pre
CMD pipenv run python manage.py migrate && python manage.py makemigrations; gunicorn fagottino.wsgi -b 0.0.0.0:80
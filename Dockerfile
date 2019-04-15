FROM python:3
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
ENV django_port=$(env_port)
RUN mkdir -p /src
RUN mkdir -p /config

# add linux tools
RUN apt-get update && apt-get upgrade -y \
    && apt-get -y install nano \
    && apt-get -y install sudo  \
    && apt-get -y install python3-dev 


WORKDIR /src
ADD ./src /src


COPY requirements.pip /src/requirements.pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.pip


CMD sleep 3 && python manage.py migrate && python manage.py makemigrations && gunicorn fagottino.wsgi -b 0.0.0.0:$DJANGO_PORT
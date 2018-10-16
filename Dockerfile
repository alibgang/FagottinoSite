FROM python:3
ENV PYTHONUNBUFFERED 1

COPY ./src /src
RUN mkdir -p /config
RUN mkdir /static

COPY ./requirements.pip /config/requirements.pip
RUN pip install -r /config/requirements.pip

# Copy in our django project
WORKDIR /src
CMD python manage.py collectstatic --no-input
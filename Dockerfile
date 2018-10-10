FROM python:3
ENV PYTHONUNBUFFERED 1

COPY ./src /src

RUN mkdir -p /config
COPY ./requirements.pip /config/requirements.pip
RUN pip install -r /config/requirements.pip

# Copy in our django project
WORKDIR /src


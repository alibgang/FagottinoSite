
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# FROM ubuntu:16.04 

# ENV USER=colbyc
# ENV SHELL=/bin/bash

# # install various tools we need
# RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
# RUN sudo apt-get update && apt-get install -y --no-install-recommends apt-utils
# RUN apt-get update -y && \
# 	apt-get upgrade -y && \
# 	apt-get install -y \
# 	git \
# 	python3  \
#     python3-dev \
# 	python3-setuptools \
# 	python3-pip \
# 	# nginx \
# 	# supervisor \
# 	# sqlite3 && \
# 	# pip3 install --upgrade pip setuptools && \
#     # rm -rf /var/lib/apt/lists/*


# COPY . /home/jenkins/Code

# WORKDIR /home/jenkins
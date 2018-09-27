FROM ubuntu:16.04 

ENV USER=jenkins
ENV SHELL=/bin/bash

# install various tools we need
RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	supervisor \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt

# add (the rest of) our code
COPY . /home/docker/code/

# Setup sudoers
RUN echo "jenkins   ALL=(ALL)  NOPASSWD: ALL" >> /etc/sudoers

USER jenkins
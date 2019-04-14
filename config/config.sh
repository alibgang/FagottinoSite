#!/bin/bash

# config.sh
# usage: ./config.sh local

# Copy the configs we want to use
cp "./nginx/$1.env" ./nginx/nginx.env
cp "./nginx/$1.conf" ./nginx/nginx.conf

# Load the env vars to the .env file that lives at the root of the project
cat ./nginx/nginx.env >> ../.env


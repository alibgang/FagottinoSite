#!/bin/bash

# config.sh
# usage: ./config.sh local

# Copy the configs we want to use
cp "./nginx/$1.env" ./nginx/nginx.env

# Load the env vars to the .env file that lives at the root of the project
cat ./nginx/nginx.env >> ../.env


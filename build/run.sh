#!/bin/bash

# run.sh
# Runs the application
# usage: ./run.sh env 


# docker-compose will read values from a .env file that lives in the same path where your docker-compose.yaml lives.
# This script will construct the .env file and run docker-compose for you.

# Remove the existing env file (if it's there)
rm -f ../.env

# Update the configs to the right config for the env
cd ../config && ./config.sh $1
cd ../

docker-compose up -d


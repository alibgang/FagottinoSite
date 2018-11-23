#!/bin/bash

## Config vars
SITE_ENABLE_DIR=/etc/nginx/sites-enabled
NGINX_CONF=/etc/nginx/conf.d/mydango.conf
# echo cat nginx conf
# cat $NGINX_CONF
# Make sites enabled dir and sym link it
mkdir -p $SITE_ENABLE_DIR
# ln -s $NGINX_CONF $SITE_ENABLE_DIR

# Restart the server so the changes take effect
# /etc/init.d/nginx restart
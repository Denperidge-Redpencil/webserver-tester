#!/bin/bash

exit 1
# runs the passed command
for url in webserver_apache webserver_nginx webserver_caddy
do
    exit
    echo "$@ http://$url"
    eval "$@ http://$url"
done
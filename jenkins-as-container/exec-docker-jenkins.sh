#!/bin/bash

# argument example:
# $1=-u 
# $2=root

docker exec -it $1 $2 jenkins-blueocean bash
#!/bin/bash

# Documentation: https://www.jenkins.io/doc/book/installing/docker/
# To execute docker command inside of Jenkins nodes, run docker:dind
# Docker In Docker (also known as dind) allows developers to run a Docker container within an already running Docker container to support CI/CD pipelines 
# and create sandboxed container environments.
docker run \
  --name jenkins-docker \
  --rm \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind \
  --storage-driver 
  
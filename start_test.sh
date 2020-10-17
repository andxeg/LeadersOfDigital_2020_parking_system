#!/bin/sh

sudo docker-compose -f "./docker-compose.test.yml" down && \
sudo docker-compose -f "./docker-compose.test.yml" build && \
sudo docker-compose -f "./docker-compose.test.yml" up -d --remove-orphans && \
sudo docker-compose -f "./docker-compose.test.yml" ps && \
sudo docker-compose -f "./docker-compose.test.yml" logs -f

#!/bin/sh
sudo docker-compose build \
  && sudo docker-compose run --rm ids_web sh -c "/wait && python recreate_db.py"



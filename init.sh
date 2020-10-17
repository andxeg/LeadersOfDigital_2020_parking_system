#!/bin/sh
sudo docker-compose build \
  && sudo docker-compose run --rm rospark_web sh -c "/wait && python recreate_db.py"



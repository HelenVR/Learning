#!/bin/sh
docker rm -f homework_3
docker run \
-p 8000:8000 \
--name=homework_3 \
--restart=always \
--detach=True \
homework_3:0.0.1

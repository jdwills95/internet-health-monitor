# Internet Health Logger
mongodb required

Following Environment Variables Required:
DB_ADDRESS='IP Address of mongodb'
DB_PORT='Port of mongodb'

Example Docker run:
sudo docker run -e DB_ADDRESS='10.5.0.101' -e DB_PORT='27017' -p 8000:8000 --name internethealthlogger darthmanatee/internethealthlogger:latest

Docker Hub:
https://hub.docker.com/repository/docker/darthmanatee/internethealthlogger/general

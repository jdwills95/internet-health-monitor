# Internet Health Logger
API for internethealthlogger

mongodb required

Following Environment Variables Required:
DB_ADDRESS='IP Address of mongodb'
DB_PORT='Port of mongodb'
UI_ORIGIN='Address of UI for cross-origin request'

Example Docker run:
sudo docker run -e DB_ADDRESS='10.5.0.101' -e DB_PORT='27017' -e UI_ORIGIN='http://localhost:4200' -p 8000:8000 --name internethealthlogger darthmanatee/internethealthlogger:latest

Docker Hub for UI:
https://hub.docker.com/repository/docker/darthmanatee/internethealthloggerui/general

Docker Hub for API:
https://hub.docker.com/repository/docker/darthmanatee/internethealthlogger/general

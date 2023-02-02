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

Docker Compose Example:
```
version: "3.8"
services:

    mongodb_container:
        image: mongo:latest
        container_name: internethealthloggerdb
        ports:
          - 27017:27017
        volumes:
          - <set-where-you-want-volume-mounted>:/data/db
        restart: unless-stopped
    
    InternetHealthLogger:
        image: darthmanatee/internethealthlogger:latest
        container_name: internethealthloggerapi
        ports:
          - 8000:8000
        environment: 
          - DB_ADDRESS=10.100.100.5 #Set this to the address of your Mongo DB
          - DB_PORT=27017 #Set this to the port of your Mongo DB
          - UI_ORIGIN=http://10.100.100.5:4200  #Set this to the IPAddress:PORT of the Internet Health Logger UI
        restart: unless-stopped

    InternetHealthLoggerUI:
        image: darthmanatee/internethealthloggerui:latest
        container_name: internethealthloggerui
        ports:
          - 4200:80
        environment:
          - API_URL=http://10.100.100.5:8000 #Set this to the IPAddress:PORT of the Internet Health Logger API
        restart: unless-stopped
```
set -ex
# SET THE FOLLOWING VARIABLES
# docker hub username
USERNAME=darthmanatee
# image name
IMAGE=internethealthlogger

docker build -t $USERNAME/$IMAGE:latest .

FROM python:3
ADD VERSION .
ADD requirements.txt /
RUN pip install -r requirements.txt
# Installing ping
RUN apt-get update
RUN apt-get install -y iputils-ping
ADD get_internet_health_database.py /
ADD internet_health_logger.py /
ADD main.py /
# CMD [ "python", "./internet_health_logger.py" ]
CMD [ "python","-u", "./main.py" ]
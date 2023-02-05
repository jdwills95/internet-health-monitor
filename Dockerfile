FROM python:3
ADD VERSION .
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD get_internet_health_database.py /
ADD internet_health_logger.py /
ADD main.py /
ADD docker_entrypoint.sh /
RUN chmod +x docker_entrypoint.sh
ENTRYPOINT ["/docker_entrypoint.sh"]

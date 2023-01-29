# main.py

import os
from datetime import datetime, timedelta
from time import sleep
from get_internet_health_database import get_database
import speedtest
from pythonping import ping

db_adr = os.environ['DB_ADDRESS']
db_port = os.environ['DB_PORT']

connection_string = "mongodb://{}:{}".format(db_adr, db_port)

dbname = get_database(connection_string)
collection_ping = dbname["ping_data"]
collection_speed = dbname["speed_data"]

st = speedtest.Speedtest(secure=True)
ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4"]
interval = 300
delete_after_days = 365


# Ping Address and log response
def pingAdr(ip_adr):
    response = ping('127.0.0.1', verbose=True)
    ping_data = {
        "date_time": datetime.utcnow(),
        "ip": ip_adr,
        "packets_received": response.stats_packets_returned,
        "packets_sent": response.stats_packets_sent,
        "latency": response.rtt_avg_ms
    }
    collection_ping.insert_one(ping_data)


# Run and log speed test up and down
def run_speed_test():
    st.get_best_server()
    speed_down = st.download()
    speed_up = st.upload()
    speed_data = {
        "date_time": datetime.utcnow(),
        "speed_down": speed_down,
        "speed_up": speed_up
    }
    collection_speed.insert_one(speed_data)


def purge_old_data():
    dlt_pass_date = datetime.utcnow() - timedelta(days=delete_after_days)
    collection_speed.delete_many({'date_time': {'$lte': dlt_pass_date}})


def start_collection():
    while True:
        for ip in ips:
            mes = "{}: Pinging {}".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), ip)
            print(mes, end='\n')
            pingAdr(ip)
        mes = "{}: Running Speed Test".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
        print(mes, end='\n')
        run_speed_test()
        mes = "{}: Purging Old Data".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
        print(mes, end='\n')
        purge_old_data()
        sleep(interval)


if __name__ == "__main__":
    print("Starting Data Collection", end='\n')
    start_collection()

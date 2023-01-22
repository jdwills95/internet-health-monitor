from datetime import datetime
from time import sleep
from get_internet_health_database import get_database
import subprocess
import speedtest

dbname = get_database()
collection_ping = dbname["ping_data"]
collection_speed = dbname["speed_data"]

st = speedtest.Speedtest(secure=True)
ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4"]
interval = 300


# Ping Address and log response
def ping(ip_adr):
    ping_cmd = "ping {}".format(ip_adr)
    response = subprocess.run(ping_cmd, shell=True, stdout=subprocess.PIPE)
    received = str(response.stdout).split("Received = ", 1)[1].split(",", 1)[0]
    sent = str(response.stdout).split("Sent = ", 1)[1].split(",", 1)[0]
    latency = str(response.stdout).split("Average = ")[1].split("\\r\\n", 1)[0]
    ping_data = {
        "date_time": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "ip": ip_adr,
        "packets_received": received,
        "packets_sent": sent,
        "latency": latency
    }
    collection_ping.insert(ping_data)


# Run and log speed test up and down
def run_speed_test():
    st.get_best_server()
    speed_down = st.download()
    speed_up = st.upload()
    speed_data = {
        "date_time": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "speed_down": speed_down,
        "speed_up": speed_up
    }
    collection_speed.insert(speed_data)


while True:
    for ip in ips:
        mes = "{}: Pinging {}".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), ip)
        print(mes, end='\n')
        ping(ip)
    mes = "{}: Running Speed Test".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    print(mes, end='\n')
    run_speed_test()
    sleep(interval)

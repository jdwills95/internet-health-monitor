from datetime import datetime
from time import sleep
import os
import subprocess
import speedtest

st = speedtest.Speedtest(secure=True)
ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4"]
interval = 300


# Ping Address and log response
def ping(ip_adr):
    ping_cmd = "ping {}".format(ip_adr)
    response = subprocess.run(ping_cmd, shell=True, stdout=subprocess.PIPE)
    log_ping(response, ip_adr)


# Run and log speed test up and down
def run_speed_test():
    st.get_best_server()
    down_speed = st.download()
    up_speed = st.upload()
    log = "speed_down: {}, speed_up: {}" \
        .format(round(down_speed / 1000 / 1000, 1),
                round(up_speed / 1000 / 1000, 1))
    log_speed(log, "speed_test")


# Log ping response in current file
def log_ping(to_log, ip_adr):
    cur_file = get_cur_file(ip_adr)
    cur_file.write("{}\n".format(str(to_log)))
    cur_file.close


# Log speed test results in current file
def log_speed(to_log, dir_name):
    cur_file = get_cur_file(dir_name)
    cur_file.write("date: {}, res: {}\n".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), str(to_log)))
    cur_file.close


# Get current day's file
def get_cur_file(dir_name):
    cur_date = datetime.utcnow().strftime('%Y-%m-%d')
    cur_file_name = "logs/{}/{}.txt".format(dir_name, cur_date)
    if os.path.exists(cur_file_name):
        file = open(cur_file_name, 'a')
    else:
        os.makedirs(os.path.dirname(cur_file_name), exist_ok=True)
        file = open(cur_file_name, 'x')
    return file


while True:
    for ip in ips:
        mes = "{}: Pinging {}".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), ip)
        print(mes, end='\n')
        ping(ip)
    mes = "{}: Running Speed Test".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    print(mes, end='\n')
    run_speed_test()
    sleep(interval)

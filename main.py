# main.py

import os
import uvicorn
from fastapi import FastAPI
from datetime import datetime
from get_internet_health_database import get_database
from pydantic import BaseModel
import internet_health_logger

db_adr = os.environ['DB_ADDRESS']
db_port = os.environ['DB_PORT']

connection_string = "mongodb://{}:{}".format(db_adr, db_port)

dbname = get_database(connection_string)
collection_ping = dbname["ping_data"]
collection_speed = dbname["speed_data"]


class Ping(BaseModel):
    date_time: datetime
    ip: str
    packets_received: str
    packets_sent: str
    latency: str


class Speed(BaseModel):
    date_time: datetime
    speed_down: float
    speed_up: float


app = FastAPI()


def __aiter__(self):
    return self


@app.get("/ping/{from_date}/{to_date}")
def root(from_date: str, to_date: str):
    f_from_date = datetime.fromisoformat(from_date)
    f_to_date = datetime.fromisoformat(to_date)
    ping_data = collection_ping.find({'date_time': {'$gte': f_from_date, '$lt': f_to_date}})
    pings = []
    for ping in ping_data:
        pings.append(Ping(**ping))
    return pings


@app.get("/speedtest/{from_date}/{to_date}")
def root(from_date: str, to_date: str):
    f_from_date = datetime.fromisoformat(from_date)
    f_to_date = datetime.fromisoformat(to_date)
    speed_data = collection_speed.find({'date_time': {'$gte': f_from_date, '$lt': f_to_date}})
    speeds = []
    for speed in speed_data:
        speeds.append(Speed(**speed))
    return speeds


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

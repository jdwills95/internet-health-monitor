# main.py

import os
import uvicorn
from fastapi import FastAPI
from datetime import datetime
from get_internet_health_database import get_database
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


db_adr = os.environ['DB_ADDRESS']
db_port = os.environ['DB_PORT']
ui_origin = os.environ['UI_ORIGIN']

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

origins = [ui_origin]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    return sorted(pings, key=lambda p: p.date_time, reverse=True)


@app.get("/speedtest/{from_date}/{to_date}")
def root(from_date: str, to_date: str):
    f_from_date = datetime.fromisoformat(from_date)
    f_to_date = datetime.fromisoformat(to_date)
    speed_data = collection_speed.find({'date_time': {'$gte': f_from_date, '$lt': f_to_date}})
    speeds = []
    for speed in speed_data:
        speeds.append(Speed(**speed))
    return sorted(speeds, key=lambda s: s.date_time, reverse=True)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#!/usr/bin/env python3
from celery import Celery
import datetime

app = Celery('tasks',
             backend='rpc',
             broker='amqp://hello:world@rmq:5672//')


@app.task
def hello_world():
    return "Hello world"


if __name__ == '__main__':
    res = hello_world.apply_async(eta=datetime.datetime(2016, 12, 2, 14, 0))
    print(res.get())

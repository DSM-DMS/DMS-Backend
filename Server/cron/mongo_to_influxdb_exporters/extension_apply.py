import sys
import os

sys.path.append(os.path.abspath(os.path.join('../..', 'app')))

from mongoengine import *
from influxdb import InfluxDBClient

from models.account import StudentModel
from models.apply import ExtensionApply11Model, ExtensionApply12Model

connect(**{
    'db': 'dms-v2',
    'host': None,
    'port': None,
    'username': os.getenv('MONGO_ID'),
    'password': os.getenv('MONGO_PW')
})

CLIENT = InfluxDBClient(**{
    'host': 'localhost',
    'port': 8086,
    'username': 'root',
    'password': os.getenv('INFLUX_PW_{}'.format('DMS_V2'), 'root'),
    'database': 'dms_v2'
})


def export(measurement, model):
    CLIENT.drop_measurement(measurement)
    # 시간의 흐름에 따른 변화가 필요 없음

    apply_counts = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }

    for apply in model.objects:
        apply_counts[apply.class_] += 1

    payload = [
        {
            'measurement': measurement,
            'fields': apply_counts
        }
    ]

    CLIENT.write_points(payload)


export('extension_apply_11', ExtensionApply11Model)
export('extension_apply_12', ExtensionApply12Model)

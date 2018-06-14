import sys
import os

sys.path.append(os.path.abspath(os.path.join('../..', 'app')))

from mongoengine import *
from influxdb import InfluxDBClient

from models.account import StudentModel
from models.apply import StayApplyModel

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
MEASUREMENT = 'stay_apply'

apply_counts = {1: 0, 2: 0, 3: 0, 4: 0}

for apply in StayApplyModel.objects:
    apply_counts[apply.value] += 1

    payload = [
        {
            'measurement':  MEASUREMENT,
            'fields': apply_counts
        }
    ]

    CLIENT.write(payload)

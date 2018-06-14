import sys
import os

sys.path.append(os.path.abspath(os.path.join('../..', 'app')))

from mongoengine import *
from influxdb import InfluxDBClient

from models.account import StudentModel
from models.apply import GoingoutApplyModel

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
MEASUREMENT = 'goingout_apply'

saturday_goingout_applier = 0
sunday_goingout_applier = 0

for apply in GoingoutApplyModel.objects:
    saturday_goingout_applier += 1 if apply.on_saturday else 0
    sunday_goingout_applier += 1 if apply.on_sunday else 0

    payload = [
        {
            'measurement': MEASUREMENT,
            'fields': {
                'saturday': saturday_goingout_applier,
                'sunday': sunday_goingout_applier
            }
        }
    ]

    CLIENT.write_points(payload)

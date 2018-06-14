import sys
import os

sys.path.append(os.path.abspath(os.path.join('../..', 'app')))

from mongoengine import *
from influxdb import InfluxDBClient

from models.version import VersionModel

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
MEASUREMENT = 'version'

version_data = {1: None, 2: None, 3: None}

for version in VersionModel.objects:
    version_data[version.platform] = version.version

    payload = [
        {
            'measurement': MEASUREMENT,
            'fields': version_data
        }
    ]

    CLIENT.write(payload)

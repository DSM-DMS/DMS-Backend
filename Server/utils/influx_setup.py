import time
import random
from datetime import datetime

from influxdb import InfluxDBClient

from app import app
from app.models.version import VersionModel

c = InfluxDBClient(database=app.config['INFLUX_DB_SETTINGS']['db'])


def _setup_version_data():
    c.drop_measurement('version')

    for version in VersionModel.objects:
        payload = [
            {
                'measurement': 'version',
                'tags': {
                    'platform': version.platform
                },
                'fields': {
                    'value': version.version
                }
            }
        ]

        c.write_points(payload)


def setup():
    _setup_version_data()

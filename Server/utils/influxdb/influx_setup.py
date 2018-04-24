import time
import random
from datetime import datetime

from influxdb import InfluxDBClient

from app import app
from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel
from app.models.version import VersionModel

c = InfluxDBClient(database=app.config['INFLUX_DB_SETTINGS']['db'])


def _setup_version_data():
    measurement = 'version'

    c.drop_measurement(measurement)

    for version in VersionModel.objects:
        payload = [
            {
                'measurement': measurement,
                'tags': {
                    'platform': version.platform
                },
                'fields': {
                    'value': version.version
                }
            }
        ]

        c.write_points(payload)


def _setup_extension_apply_data():
    def _setup(measurement, model):
        c.drop_measurement(measurement)

        for apply in model.objects:
            payload = [
                {
                    'measurement': measurement,
                    'tags': {
                        'class': apply.class_
                    },
                    'fields': {
                        'value': apply.seat
                    }
                }
            ]

            c.write_points(payload)

    _setup('extension_apply_11', ExtensionApply11Model)
    _setup('extension_apply_12', ExtensionApply12Model)


def _setup_goingout_apply_data():
    measurement = 'goingout_apply'

    c.drop_measurement(measurement)

    for apply in GoingoutApplyModel.objects:
        payload = [
            {
                'measurement': measurement,
                'tags': {
                    'on': 'saturday'
                },
                'fields': {
                    'value': apply.on_saturday
                }
            },
            {
                'measurement': measurement,
                'tags': {
                    'on': 'sunday'
                },
                'fields': {
                    'value': apply.on_sunday
                }
            }
        ]

        c.write_points(payload)


def setup():
    while True:
        _setup_version_data()
        _setup_extension_apply_data()
        _setup_goingout_apply_data()

        time.sleep(3600)

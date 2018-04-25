import time

from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel
from app.models.version import VersionModel

from utils.influxdb import c


def _setup_version_data(sleep_seconds=3600):
    measurement = 'version'

    while True:
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

        time.sleep(sleep_seconds)


def _setup_extension_apply_data(sleep_seconds=3600):
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

    while True:
        _setup('extension_apply_11', ExtensionApply11Model)
        _setup('extension_apply_12', ExtensionApply12Model)

        time.sleep(sleep_seconds)


def _setup_goingout_apply_data(sleep_seconds=3600):
    measurement = 'goingout_apply'

    while True:
        c.drop_measurement(measurement)

        for apply in GoingoutApplyModel.objects:
            payload = [
                {
                    'measurement': measurement,
                    'tags': {
                        'on': 'saturday',
                        'status': apply.on_saturday
                    },
                    'fields': {
                        'value': 1
                    }
                },
                {
                    'measurement': measurement,
                    'tags': {
                        'on': 'sunday',
                        'status': apply.on_sunday
                    },
                    'fields': {
                        'value': 1
                    }
                }
            ]

            c.write_points(payload)

        time.sleep(sleep_seconds)


def _setup_stay_apply_data(sleep_seconds=3600):
    measurement = 'stay_apply'

    while True:
        c.drop_measurement(measurement)

        for apply in StayApplyModel.objects:
            payload = [
                {
                    'measurement': measurement,
                    'tags': {
                        'when': apply.value
                    },
                    'fields': {
                        'value': 1
                    }
                }
            ]

            c.write_points(payload)

        time.sleep(sleep_seconds)


def setup():
    _setup_version_data()
    _setup_extension_apply_data(10)
    _setup_goingout_apply_data()
    _setup_stay_apply_data(60)

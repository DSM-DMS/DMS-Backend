import time
from threading import Thread

from influxdb import InfluxDBClient

from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel
from app.models.version import VersionModel


class Influx:
    def __init__(self, app=None):
        self.client = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        db_name = app.config['INFLUX_DB_SETTINGS']['db']

        self.client = InfluxDBClient(database=db_name)

        if db_name not in self.client.get_list_database():
            self.client.create_database(db_name)

        threads = [
            Thread(target=self._setup_version_data),
            Thread(target=self._setup_extension_apply_data, args=(10,)),
            Thread(target=self._setup_goingout_apply_data, args=(60,)),
            Thread(target=self._setup_stay_apply_data, args=(60,))
        ]

        for thread in threads:
            thread.start()

    def _log(self, measurement, payload):
        print('[InfluxDB] [{}] write points complete : {}'.format(measurement, payload))

    def _setup_version_data(self, sleep_seconds=3600):
        measurement = 'version'

        while True:
            self.client.drop_measurement(measurement)

            version_data = {
                1: '',
                2: '',
                3: ''
            }

            for version in VersionModel.objects:
                version_data[version.platform] = version.version

            payload = [
                {
                    'measurement': measurement,
                    'fields': version_data
                }
            ]

            self.client.write_points(payload)
            self._log(measurement, payload)

            time.sleep(sleep_seconds)

    def _setup_extension_apply_data(self, sleep_seconds=3600):
        def _setup(measurement, model):
            self.client.drop_measurement(measurement)
            # 시간의 흐름에 따른 변화가 현재는 필요없으므로

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

            self.client.write_points(payload)
            self._log(measurement, payload)

        while True:
            _setup('extension_apply_11', ExtensionApply11Model)
            _setup('extension_apply_12', ExtensionApply12Model)

            time.sleep(sleep_seconds)

    def _setup_goingout_apply_data(self, sleep_seconds=3600):
        measurement = 'goingout_apply'

        while True:
            saturday_goingout_applier = 0
            sunday_goingout_applier = 0

            for apply in GoingoutApplyModel.objects:
                saturday_goingout_applier += 1 if apply.on_saturday else 0
                sunday_goingout_applier += 1 if apply.on_sunday else 0

            payload = [
                {
                    'measurement': measurement,
                    'fields': {
                        'saturday': saturday_goingout_applier,
                        'sunday': sunday_goingout_applier
                    }
                }
            ]

            self.client.write_points(payload)
            self._log(measurement, payload)

            time.sleep(sleep_seconds)

    def _setup_stay_apply_data(self, sleep_seconds=3600):
        measurement = 'stay_apply'

        while True:
            apply_counts = {
                1: 0,
                2: 0,
                3: 0,
                4: 0
            }

            for apply in StayApplyModel.objects:
                apply_counts[apply.value] += 1

            payload = [
                {
                    'measurement': measurement,
                    'fields': apply_counts
                }
            ]

            self.client.write_points(payload)
            self._log(measurement, payload)

            time.sleep(sleep_seconds)

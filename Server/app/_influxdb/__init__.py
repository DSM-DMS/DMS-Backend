import time
from threading import Thread
from pymongo import MongoClient
import os

from app.models.apply import ExtensionApply11Model, ExtensionApply12Model, GoingoutApplyModel, StayApplyModel
from app.models.version import VersionModel


class InfluxCronJob:
    def __init__(self, app=None):
        self.client = None
        self.db_name = None

        self.mongo = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.client = app.config['INFLUXDB_CLIENT']
        self.db_name = app.config['INFLUXDB_SETTINGS']['database']

        self.mongo = MongoClient(
            username=os.getenv('MONGO_ID'),
            password=os.getenv('MONGO_PW'),
            authSource=app.config['SERVICE_NAME']
        )['dms-v2']

        if self.db_name not in self.client.get_list_database():
            self.client.create_database(self.db_name)

        threads = [
            Thread(target=self._setup_version_data),
            Thread(target=self._setup_extension_apply_data, args=(60,)),
            Thread(target=self._setup_goingout_apply_data, args=(120,)),
            Thread(target=self._setup_stay_apply_data, args=(120,)),
            Thread(target=self._setup_document_count, args=(120,))
        ]

        if not app.testing:
            for thread in threads:
                thread.start()

    def _log(self, payload):
        measurement = payload[0].pop('measurement')

        print('[InfluxDB] [{}] write points complete : {}'.format(measurement, payload[0]))

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
            self._log(payload)

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
            self._log(payload)

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
            self._log(payload)

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
            self._log(payload)

            time.sleep(sleep_seconds)

    def _setup_document_count(self, sleep_seconds=3600):
        measurement = 'document_count'

        while True:
            self.client.drop_measurement(measurement)

            collections = self.mongo.collection_names()

            document_counts = {
                collection: self.mongo[collection].count()
                for collection in collections}

            payload = [
                {
                    'measurement': measurement,
                    'fields': document_counts
                 }
            ]

            self.client.write_points(payload)
            self._log(payload)

            time.sleep(sleep_seconds)

import ujson
from binascii import hexlify
from hashlib import pbkdf2_hmac
from unittest import TestCase as TC

from flask import Response
from flask_jwt_extended import create_access_token, create_refresh_token
import pymongo

from app import create_app
from config.test import TestConfig
from app.models.account import AdminModel, StudentModel

app = create_app(TestConfig)


class TCBase(TC):
    def __init__(self, *args, **kwargs):
        self.client = app.test_client()

        super(TCBase, self).__init__(*args, **kwargs)

    def _create_fake_account(self):
        self.admin = AdminModel(
            id=self.admin_id,
            pw=self.encrypted_pw,
            name=self.admin_name
        ).save()

        self.student = StudentModel(
            id=self.student_id,
            pw=self.encrypted_pw,
            name=self.student_name,
            number=self.student_number
        ).save()

    def _get_tokens(self):
        with app.app_context():
            self.admin_access_token = 'JWT {}'.format(create_access_token(self.admin_id))
            self.admin_refresh_token = 'JWT {}'.format(create_refresh_token(self.admin_id))
            self.student_access_token = 'JWT {}'.format(create_access_token(self.student_id))
            self.student_refresh_token = 'JWT {}'.format(create_refresh_token(self.student_id))

    def setUp(self):
        self.admin_id = self.admin_name = 'admin'
        self.student_id = self.student_name = 'student'
        self.student_number = 3118
        self.pw = 'pw'
        self.encrypted_pw = hexlify(
            pbkdf2_hmac(
                'sha256',
                self.pw.encode(),
                app.secret_key.encode(),
                100000
            )
        ).decode()

        self._create_fake_account()
        self._get_tokens()

    def tearDown(self):
        setting = app.config['MONGODB_SETTINGS']
        db_name = setting.pop('db')

        pymongo.MongoClient(**setting).drop_database(db_name)

        setting['db'] = db_name

    def json_request(self, method, target_url_rule, token=None, *args, **kwargs):
        """
        Helper for json request

        Args:
            method (func): Request method
            target_url_rule (str): URL rule for request
            token (str) : JWT or OAuth's access token with prefix(Bearer, JWT, ...)

        Returns:
            Response
        """
        data = kwargs.pop('data')

        return method(
            target_url_rule if target_url_rule.startswith('/v2') else '/v2' + target_url_rule,
            data=ujson.dumps(data) if data else None,
            content_type='application/json',
            headers={'Authorization': token or self.admin_access_token},
            *args,
            **kwargs
        )

    def request(self, method, target_url_rule, token=None, *args, **kwargs):
        """
        Helper for common request

        Args:
            method (func): Request method
            target_url_rule (str): URL rule for request
            token (str) : JWT or OAuth's access token with prefix(Bearer, JWT, ...)

        Returns:
            Response
        """
        return method(
            target_url_rule if target_url_rule.startswith('/v2') else '/v2' + target_url_rule,
            headers={'Authorization': token or self.admin_access_token},
            *args,
            **kwargs
        )

    def decode_response_data(self, resp):
        return resp.data.decode()

    def get_response_data_as_json(self, resp):
        return ujson.loads(self.decode_response_data(resp))

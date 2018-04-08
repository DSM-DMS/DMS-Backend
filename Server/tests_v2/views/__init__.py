from binascii import hexlify
from datetime import datetime
from hashlib import pbkdf2_hmac
from unittest import TestCase as TC

import ujson

from app_v2 import app
from app_v2.models.account import AdminModel, StudentModel


class TCBase(TC):
    def __init__(self, *args, **kwargs):
        TC.__init__(self, *args, **kwargs)

        self.client = app.test_client()

    def _create_fake_account(self):
        pw = hexlify(
            pbkdf2_hmac(
                'sha256',
                b'pw',
                app.secret_key.encode(),
                100000
            )
        ).decode()

        AdminModel(
            signup_time=datetime.now,
            id='admin',
            pw=pw,
            name='fake_admin'
        ).save()

        StudentModel(
            signup_time=datetime.now,
            id='student',
            pw=pw,
            name='fake_student',
            number=1111,
        ).save()

    def _get_tokens(self):
        resp = self.client.post('/admin/auth', data={'id': 'admin', 'pw': 'pw'})
        data = ujson.loads(resp.data.decode())
        self.admin_access_token = 'JWT {}'.format(data['access_token'])
        self.admin_refresh_token = 'JWT {}'.format(data['refresh_token'])

        resp = self.client.post('/auth', data={'id': 'student', 'pw': 'pw'})
        data = ujson.loads(resp.data.decode())
        self.student_access_token = 'JWT {}'.format(data['access_token'])
        self.student_refresh_token = 'JWT {}'.format(data['refresh_token'])

    def setUp(self):
        self._create_fake_account()
        self._get_tokens()

    def tearDown(self):
        AdminModel.objects.delete()
        StudentModel.objects.delete()

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
        if token is None:
            token = self.student_access_token

        data = kwargs.pop('data')

        return method(
            target_url_rule,
            data=ujson.dumps(data) if data else None,
            content_type='application/json',
            headers={'Authorization': token},
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
        if token is None:
            token = self.student_access_token

        return method(
            target_url_rule,
            headers={'Authorization': token},
            *args,
            **kwargs
        )

    def get_response_data(self, resp):
        return ujson.loads(resp.data.decode())

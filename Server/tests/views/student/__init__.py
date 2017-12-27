from binascii import hexlify
from hashlib import pbkdf2_hmac
import json

from app import app

from app.models.account import StudentModel


def create_fake_account():
    pw = hexlify(
        pbkdf2_hmac(
            hash_name='sha256',
            password=b'fake',
            salt=app.secret_key.encode(),
            iterations=100000
        )
    ).decode('utf-8')

    StudentModel(
        id='fake',
        pw=pw,
        name='fake',
        number=1234
    ).save()


def remove_fake_account(id='fake'):
    StudentModel.objects(
        id=id
    ).delete()


def get_access_token(client, id='fake', pw='fake'):
    rv = client.post('/auth', data={'id': id, 'pw': pw})

    return 'JWT ' + json.loads(rv.data.decode())['access_token']


def get_refresh_token(client, id='fake', pw='fake'):
    rv = client.post('/auth', data={'id': id, 'pw': pw})

    return 'JWT ' + json.loads(rv.data.decode())['refresh_token']

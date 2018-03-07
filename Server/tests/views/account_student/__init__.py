from binascii import hexlify
from datetime import datetime
from hashlib import pbkdf2_hmac
import json

from app import app

from app.models.account import StudentModel
from app.models.apply import GoingoutApplyModel, StayApplyModel


def create_fake_account(id='fake_student'):
    pw = hexlify(
        pbkdf2_hmac(
            hash_name='sha256',
            password=b'fake',
            salt=app.secret_key.encode(),
            iterations=100000
        )
    ).decode('utf-8')

    StudentModel(
        id=id,
        pw=pw,
        name='fake',
        number=1111,
        goingout_apply=GoingoutApplyModel(apply_date=datetime.now()),
        stay_apply=StayApplyModel(apply_date=datetime.now())
    ).save()


def remove_fake_account(id='fake_student'):
    StudentModel.objects(
        id=id
    ).delete()


def get_access_token(client, id='fake_student', pw='fake'):
    rv = client.post('/auth', data={'id': id, 'pw': pw})

    return 'JWT ' + json.loads(rv.data.decode())['access_token']


def get_refresh_token(client, id='fake_student', pw='fake'):
    rv = client.post('/auth', data={'id': id, 'pw': pw})

    return 'JWT ' + json.loads(rv.data.decode())['refresh_token']

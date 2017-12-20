import json


def get_access_token(client, id='fake', pw='fake'):
    rv = client.post('/auth', data={'id': id, 'pw': pw})

    return 'JWT ' + json.loads(rv.data.decode())['access_token']


def get_refresh_token(client, id='fake', pw='fake'):
    rv = client.post('/auth', data={'id': id, 'pw': pw})

    return 'JWT ' + json.loads(rv.data.decode())['refresh_token']

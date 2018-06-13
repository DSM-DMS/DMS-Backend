import os

MONGODB_SETTINGS = {
    'db': 'dms-v2',
    'host': None,
    'port': None,
    'username': os.getenv('MONGO_ID'),
    'password': os.getenv('MONGO_PW')
}

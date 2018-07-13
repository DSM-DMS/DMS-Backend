from mongoengine import *


class VersionModel(Document):
    """
    각 클라이언트의 버전 관리를 위한 collection
    """
    meta = {
        'collection': 'versions'
    }

    platform = IntField(
        required=True,
        primary_key=True
    )
    # 1: Web
    # 2: Android
    # 3: IOS

    version = StringField(
        required=True
    )

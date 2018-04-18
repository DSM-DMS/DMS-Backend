from app.models import *


class VersionModel(Document):
    """
    각 클라이언트의 버전 관리를 위한 collection
    
    1 : Web
    2 : Android
    3 : IOS
    """
    meta = {
        'collection': 'versions'
    }

    platform = IntField(
        required=True,
        primary_key=True,
        min_value=1,
        max_value=3
    )

    version = StringField(
        required=True
    )

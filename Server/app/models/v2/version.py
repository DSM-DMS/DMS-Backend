from app.models.v2 import *


class VersionModel(Document):
    """
    Application newest version document
    
    platform
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
    # 타입을 int로 변경, primary key로 지정

    version = StringField(
        required=True
    )

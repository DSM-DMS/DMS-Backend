from app.models import *


class VersionModel(Document):
    """
    Application newest version document
    """
    meta = {
        'collection': 'version'
    }

    platform = StringField(required=True)
    version = StringField(required=True)
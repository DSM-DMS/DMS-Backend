from datetime import datetime

from app.models import *


class PostBase(Document):
    """
    Post data base document
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    write_time = DateTimeField(
        required=True,
        default=datetime.now()
    )
    author = StringField(
        required=True,
        default='사감실'
    )
    title = StringField(
        required=True
    )
    content = StringField(
        required=True
    )
    pinned = BooleanField(
        required=True,
        default=False
    )


class FAQModel(PostBase):
    meta = {
        'collection': 'faq'
    }


class NoticeModel(PostBase):
    meta = {
        'collection': 'notice'
    }


class RuleModel(PostBase):
    meta = {
        'collection': 'rule'
    }

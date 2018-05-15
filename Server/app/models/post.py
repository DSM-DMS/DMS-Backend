from datetime import datetime

from mongoengine import *


class PostBase(Document):
    """
    게시글에 대한 상위 collection
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    write_time = DateTimeField(
        required=True,
        default=datetime.now
    )
    # 게시글 작성 시간

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
    # 고정 게시글 여부


class FAQModel(PostBase):
    meta = {
        'collection': 'post_faq'
    }


class NoticeModel(PostBase):
    meta = {
        'collection': 'post_notice'
    }


class RuleModel(PostBase):
    meta = {
        'collection': 'post_rule'
    }

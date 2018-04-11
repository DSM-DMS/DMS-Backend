from app.models.v2 import *


class PostBase(Document):
    """
    Post data base document
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }
    # collection claim 제거

    write_time = DateTimeField(
        required=True
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
        'collection': 'post_faq'
    }
    # collection name 변경


class NoticeModel(PostBase):
    meta = {
        'collection': 'post_notice'
    }
    # collection name 변경


class RuleModel(PostBase):
    meta = {
        'collection': 'post_rule'
    }
    # collection name 변경

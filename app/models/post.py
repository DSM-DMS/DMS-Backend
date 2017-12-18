from datetime import date

from app.models import *
from app.models.account import AdminModel


class PostBase(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    author = ReferenceField(AdminModel, required=True)
    pinned = BooleanField(required=True, default=False)

    write_date = StringField(required=True, default=str(date.today()))
    meta = {'allow_inheritance': True}


class FAQModel(PostBase):
    pass


class NoticeModel(PostBase):
    pass


class RuleModel(PostBase):
    pass

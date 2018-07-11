from uuid import uuid4

from flask_jwt_extended import create_access_token, create_refresh_token
from mongoengine import *

from app.models.account import AccountBase


class TokenBase(Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    class Key(EmbeddedDocument):
        owner = ReferenceField(
            document_type=AccountBase,
            required=True,
            unique_with='user_agent'
        )

        user_agent = StringField(
            required=True
        )

    key = EmbeddedDocumentField(
        document_type=Key,
        primary_key=True
    )
    # 여러 필드를 합쳐 PK로 두기 위함

    identity = UUIDField(
        unique=True,
        default=uuid4
    )

    @classmethod
    def _create_token(cls, account, user_agent):
        return cls(
            key=cls.Key(owner=account, user_agent=user_agent)
        ).save().identity

    @classmethod
    def create_access_token(cls, account, user_agent):
        return create_access_token(
            str(cls._create_token(account, user_agent))
        )

    @classmethod
    def create_refresh_token(cls, account, user_agent):
        return create_refresh_token(
            str(cls._create_token(account, user_agent))
        )


class AccessTokenModelV2(TokenBase):
    meta = {
        'collection': 'access_token_v2'
    }


class RefreshTokenModelV2(TokenBase):
    meta = {
        'collection': 'refresh_token_v2'
    }
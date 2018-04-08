from flask import Response

from app_v1.models.support.mongo_helper import mongo_to_dict
from app_v1.views import BaseResource


class PostAPIResource(BaseResource):
    def get_list_as_response(self, model):
        data = [mongo_to_dict(obj, ['content']) for obj in model.objects]

        return self.unicode_safe_json_response(data)

    def get_item_as_response(self, model, post_id):
        if len(post_id) != 24:
            return Response('', 204)

        post = model.objects(id=post_id).first()

        if not post:
            return Response('', 204)

        data = mongo_to_dict(post, ['id'])

        return self.unicode_safe_json_response(data)

    def get_preview_item_as_response(self, model):
        post = model.objects(pinned=True).first()

        if not post:
            post = model.objects.first()
            if not post:
                return Response('', 204)

        data = mongo_to_dict(post, ['id'])

        return self.unicode_safe_json_response(data)

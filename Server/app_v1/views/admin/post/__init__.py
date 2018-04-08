from datetime import datetime

from flask import Response, g, request

from app_v1.models.support.mongo_helper import mongo_to_dict
from app_v1.views import BaseResource


class PostAPIResource(BaseResource):
    def upload_post(self, model):
        title = request.form['title']
        content = request.form['content']

        admin = g.user

        post = model(
            author=admin.name,
            title=title,
            content=content,
            write_time=datetime.now()
        ).save()

        return {
            'id': str(post.id)
        }, 201

    def modify_post(self, model):
        id = request.form['id']
        title = request.form['title']
        content = request.form['content']

        if len(id) != 24:
            return Response('', 204)

        post = model.objects(id=id).first()
        if not post:
            return Response('', 204)

        post.update(title=title, content=content)

        return Response('', 200)

    def delete_post(self, model):
        id = request.form['id']

        if len(id) != 24:
            return Response('', 204)

        post = model.objects(id=id).first()
        if not post:
            return Response('', 204)

        post.delete()

        return Response('', 200)

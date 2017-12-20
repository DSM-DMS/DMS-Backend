from datetime import datetime, time
import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.student.apply.extension import *
from app.models.account import StudentModel
from app.models.apply import ExtensionApplyModel

from utils.extension_meta import *


class Extension11(Resource):
    @jwt_required
    def get(self):
        """
        11시 연장신청 정보 조회
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
            return Response('', 403)

        return ({
            'class': student.extension_apply_11.class_,
            'seat': student.extension_apply_11.seat
        }, 200) if student.extension_apply_11 else ('', 204)

    def post(self):
        """
        11시 연장신청
        """
        student = StudentModel.objects(
            id=get_jwt_identity()
        ).first()
        if not student:
            return Response('', 403)

        now = datetime.now().time()

        if not APPLY_START < now < APPLY_END_11:
            return Response('', 204)

        class_ = int(request.form['class'])
        seat = int(request.form['seat'])

        student.update(
            extension_apply_11=ExtensionApplyModel(
                class_=class_,
                seat=seat
            )
        )

        return Response('', 201)

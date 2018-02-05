from flask import Blueprint, Response
from flask_jwt_extended import jwt_required
from flask_restful import Api, request
from flasgger import swag_from

from app.docs.admin.point.point import *
from app.models.account import StudentModel
from app.models.point import PointRuleModel, PointHistoryModel
from app.views import BaseResource

api = Api(Blueprint('admin-point-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/point')
class PointManaging(BaseResource):
    @swag_from(POINT_MANAGING_GET)
    @jwt_required
    @BaseResource.admin_only
    def get(self):
        """
        특정 학생의 상벌점 내역 조회
        """
        id = request.args['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        response = [{
            'time': str(history.time)[:10],
            'reason': history.reason,
            'point': history.point,
            'id': str(history.id)
        } for history in student.point_histories]

        return self.unicode_safe_json_response(response)

    @swag_from(POINT_MANAGING_POST)
    @jwt_required
    @BaseResource.admin_only
    def post(self):
        """
        특정 학생에 대한 상벌점 부여
        """
        id = request.form['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        rule_id = request.form['rule_id']
        if len(rule_id) != 24:
            return Response('', 205)

        rule = PointRuleModel.objects(id=rule_id).first()
        if not rule:
            return Response('', 205)

        point = int(request.form['point'])

        student.point_histories.append(PointHistoryModel(
            reason=rule.name,
            point=point
        ))
        # Append history

        if point < 0:
            student.bad_point += abs(point)
        else:
            student.good_point += point

        student.save()

        return Response('', 201)

    @swag_from(POINT_MANAGING_DELETE)
    @jwt_required
    @BaseResource.admin_only
    def delete(self):
        """
        상벌점 내역 삭제
        """
        student_id = request.form['student_id']
        point_id = request.form['point_id']

        student = StudentModel.objects(id=student_id).first()
        if not student:
            return Response('', 204)

        point = student.point_histories.filter(id=point_id).first()
        if not point:
            return Response('', 205)

        student.point_histories = student.point_histories.exclude(id=point_id)
        student.save()

        return Response('', 200)

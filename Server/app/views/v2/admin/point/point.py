from flask import Blueprint, Response, request
from flask_restful import Api
from flasgger import swag_from

from app.docs.v2.admin.point.point import *
from app.models.account import AdminModel, StudentModel
from app.models.point import PointRuleModel, PointHistoryModel
from app.views.v2 import BaseResource, auth_required, json_required

api = Api(Blueprint(__name__, __name__))
api.prefix = '/admin/point/point'


@api.resource('/<student_id>')
class Point(BaseResource):
    @auth_required(AdminModel)
    @swag_from(POINT_GET)
    def get(self, student_id):
        """
        특정 학생의 상벌점 내역 조회
        """
        student = StudentModel.objects(id=student_id).first()

        return self.unicode_safe_json_dumps([{
            'id': str(history.id),
            'date': history.time.strftime('%Y-%m-%d'),
            'reason': history.reason,
            'pointType': history.point_type,
            'point': history.point
        } for history in student.point_histories]) if student else Response('', 204)

    @auth_required(AdminModel)
    @json_required({'ruleId': str, 'applyGoodPoint': bool, 'point': int})
    @swag_from(POINT_POST)
    def post(self, student_id):
        """
        특정 학생에게 상벌점 부여
        """
        payload = request.json

        rule_id = payload['ruleId']
        apply_good_point = payload['applyGoodPoint']
        point = payload['point']

        student = StudentModel.objects(id=student_id).first()

        if not student:
            return Response('', 204)

        if len(rule_id) != 24 or not PointRuleModel.objects(id=rule_id):
            return Response('', 205)

        rule = PointRuleModel.objects(id=rule_id).first()

        point_history = PointHistoryModel(
            reason=rule.name,
            point_type=rule.point_type,
            point=point
        )

        student.point_histories.append(point_history)

        if (student.bad_point - 10) // 5 > student.penalty_level and not student.penalty_training_status:
            student.penalty_level = student.penalty_level + 1
            student.penalty_training_status = True

        if apply_good_point:
            student.good_point += point
        else:
            student.bad_point += point

        student.save()

        return {
            'id': str(point_history.id)
        }, 201

    @auth_required(AdminModel)
    @json_required({'historyId': str})
    @swag_from(POINT_DELETE)
    def delete(self, student_id):
        """
        특정 학생의 상벌점 내역 삭제
        """
        payload = request.json

        history_id = payload['historyId']

        student = StudentModel.objects(id=student_id).first()

        if not student:
            return Response('', 204)

        if len(history_id) != 24:
            return Response('', 205)

        history = student.point_histories.filter(id=history_id).first()
        if not history:
            return Response('', 205)

        student.point_histories = student.point_histories.exclude(id=history_id)
        if history.point_type:
            student.good_point = student.good_point - history.point
        else:
            student.bad_point = student.bad_point - history.point

        student.save()

        return Response('', 200)

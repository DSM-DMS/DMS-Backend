from flask import Blueprint, Response, abort, g, request
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

        if not student:
            return Response('', 204)

        return self.unicode_safe_json_dumps([{
            'id': str(history.id),
            'date': history.time.strftime('%Y-%m-%d'),
            'reason': history.reason,
            'pointType': history.point_type,
            'point': history.point
        } for history in student.point_histories])

    @auth_required(AdminModel)
    @json_required('ruleId', 'point')
    @swag_from(POINT_POST)
    def post(self, student_id):
        """
        특정 학생에게 상벌점 부여
        """
        rule_id = request.json['ruleId']
        point = request.json['point']

        student = StudentModel.objects(id=student_id).first()

        if not student:
            return Response('', 204)

        if len(rule_id) != 24 or not PointRuleModel.objects(id=rule_id):
            return Response('', 205)

        rule = PointRuleModel.objects(id=rule_id).first()

        if not rule.min_point <= point <= rule.max_point:
            # 최소 점수와 최대 점수 외의 점수를 부여하는 경우
            abort(403)

        point_history = PointHistoryModel(
            reason=rule.name,
            point_type=rule.point_type,
            point=point
        )

        student.point_histories.append(point_history)

        if (student.bad_point - 10) // 5 > student.penalty_level and not student.penalty_training_status:
            student.penalty_level = student.penalty_level + 1
            student.penalty_training_status = True

        if rule.point_type:
            student.good_point += point
        else:
            student.bad_point += point

        student.save()

        return {
            'id': str(point_history.id)
        }, 201

    @auth_required(AdminModel)
    @json_required('historyId')
    @swag_from(POINT_DELETE)
    def delete(self, student_id):
        """
        특정 학생의 상벌점 내역 삭제
        """
        history_id = request.json['historyId']

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
            student.update(good_point=student.good_point - history.point)
        else:
            student.update(bad_point=student.bad_point - history.point)

        student.save()

        return Response('', 200)

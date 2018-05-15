from bson import ObjectId
from datetime import datetime

from flask import Blueprint, Response, request
from flask_restful import Api


from app.views.v1 import BaseResource
from app.views.v1 import admin_only


from app.models.account import StudentModel
from app.models.point import PointRuleModel, PointHistoryModel
from app.models.support.mongo_helper import mongo_to_dict

api = Api(Blueprint('admin-point-api', __name__))
api.prefix = '/admin/managing'


@api.resource('/point')
class PointManaging(BaseResource):
    
    @admin_only
    def get(self):
        """
        특정 학생의 상벌점 내역 조회
        """
        id = request.args['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        response = [mongo_to_dict(history) for history in student.point_histories]

        return self.unicode_safe_json_response(response)

    
    @admin_only
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
            point_type=rule.point_type,
            point=point,
            time=datetime.now(),
            id=ObjectId()
        ))
        # Append history

        if rule.point_type:
            student.good_point += point
        else:
            student.bad_point += point

        if (student.bad_point - 10) // 5 > student.penalty_level and not student.penalty_training_status:
            student.penalty_level = student.penalty_level + 1
            student.penalty_training_status = True

        student.save()

        return Response('', 201)

    
    @admin_only
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

        if point.point_type:
            student.update(good_point=student.good_point - point.point)
        else:
            student.update(bad_point=student.bad_point - point.point)
        student.save()

        return Response('', 200)

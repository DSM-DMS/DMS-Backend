import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.models.account import AdminModel, StudentModel
from app.models.point import PointRuleModel, PointHistoryModel


class StudentManaging(Resource):
    @jwt_required
    def get(self):
        """
        학생 목록 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        response = [{
            'id': student.id,
            'name': student.name,
            'number': student.number,
            'good_point': student.good_point,
            'bad_point': student.bad_point,
            'penalty_training_status': student.penalty_training_status
        } for student in StudentModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @jwt_required
    def post(self):
        """
        새로운 학생 상벌점 데이터 등록
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        good_point = int(request.form['good_point'])
        bad_point = int(request.form['bad_point'])
        penalty_training_status = int(request.form['penalty_training_status'])

        student.update(
            good_point=good_point,
            bad_point=bad_point,
            penalty_training_status=penalty_training_status
        )

        return Response('', 201)


class PointManaging(Resource):
    @jwt_required
    def get(self):
        """
        특정 학생의 상벌점 내역 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        response = [{
            'time': str(history.time)[:-7],
            'reason': history.reason.name,
            'point': history.point
        } for history in student.point_histories]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @jwt_required
    def post(self):
        """
        특정 학생에 대한 상벌점 부여
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form['id']
        student = StudentModel.objects(id=id).first()
        if not student:
            return Response('', 204)

        rule_id = request.form['rule_id']
        rule = PointRuleModel.objects(id=rule_id).first()
        if not rule:
            return Response('', 205)

        point = int(request.form['point'])

        student.point_histories.append(PointHistoryModel(
            reason=rule,
            point=point
        ))
        student.save()

        return Response('', 201)


class PointRuleManaging(Resource):
    @jwt_required
    def get(self):
        """
        상벌점 규칙 목록 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        response = [{
            'id': rule.id,
            'name': rule.name,
            'min_point': rule.min_point,
            'max_point': rule.max_point
        } for rule in PointRuleModel.objects]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @jwt_required
    def post(self):
        """
        상벌점 규칙 추가
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        name = request.form['name']
        min_point = int(request.form['min_point'])
        max_point = int(request.form['max_point'])

        PointRuleModel(
            name=name,
            min_point=min_point,
            max_point=max_point
        ).save()

        return Response('', 201)

    @jwt_required
    def patch(self):
        """
        상벌점 규칙 수정
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        rule_id = request.form['rule_id']
        rule = PointRuleModel.objects(id=rule_id).first()
        if not rule:
            return Response('', 205)

        name = request.form['name']
        min_point = int(request.form['min_point'])
        max_point = int(request.form['max_point'])

        rule.update(
            name=name,
            min_point=min_point,
            max_point=max_point
        )

        return Response('', 200)

from bson.objectid import ObjectId
from datetime import datetime

from pymongo import MongoClient

from app.models.v2.account import *

client = MongoClient()
db = client['dms']


def _migration_account():
    account = db['account_base']
    for account in account.find():
        if account['_cls'] == 'StudentModel':
            student = StudentModel(
                signup_time=account['signup_time'] if 'signup_time' in account else datetime.now(),
                id=account['_id'],
                pw=account['pw'],
                name=account['name'],

                number=account['number'],
                good_point=account['good_point'],
                bad_point=account['bad_point'],
                point_histories=[PointHistoryModel(id=ObjectId(), time=history['time'], reason=history['reason'], point_type=history['point_type'], point=history['point']) for history in account['point_histories']],
                penalty_training_status=account['penalty_training_status'],
                penalty_level=account['penalty_level']
            )

            # print(student.point_histories)
            # print(student.point_histories[0].reason)

            student.save()

            if 'stay_apply' in account:
                stay_apply = account['stay_apply']

                apply_date = stay_apply['apply_date']
                value = stay_apply['value']
            else:
                apply_date = datetime.now()
                value = 4

            StayApplyModel(student=student, apply_date=apply_date, value=value).save()

            if 'goingout_apply' in account:
                goingout_apply = account['goingout_apply']

                apply_date = goingout_apply['apply_date']
                on_saturday = goingout_apply['on_saturday']
                on_sunday = goingout_apply['on_sunday']
            else:
                apply_date = datetime.now()
                on_saturday = False
                on_sunday = False

            GoingoutApplyModel(
                student=student,
                apply_date=apply_date,
                on_saturday=on_saturday,
                on_sunday=on_sunday
            ).save()

        elif account['_cls'] == 'AdminModel':
            AdminModel(
                signup_time=account['signup_time'] if 'signup_time' in account else datetime.now(),
                id=account['_id'],
                pw=account['pw'],
                name=account['name']
            ).save()
        else:
            SystemModel(
                signup_time=account['signup_time'] if 'signup_time' in account else datetime.now(),
                id=account['_id'],
                pw=account['pw'],
                name=account['name']
            ).save()


def _migration_point_rule():
    point_rules = db['point_rule']
    for rule in point_rules.find():
        PointRuleModel(
            name=rule['name'],
            point_type=rule['point_type'],
            min_point=rule['min_point'],
            max_point=rule['max_point']
        ).save()


def _migration_post():
    FAQs = db['faq']
    notices = db['notice']
    rules = db['rule']

    for FAQ in FAQs.find():
        FAQModel(
            write_time=FAQ['write_time'],
            author=FAQ['author'],
            title=FAQ['title'],
            content=FAQ['content'],
            pinned=FAQ['pinned']
        ).save()

    for notice in notices.find():
        NoticeModel(
            write_time=notice['write_time'],
            author=notice['author'],
            title=notice['title'],
            content=notice['content'],
            pinned=notice['pinned']
        ).save()

    for rule in rules.find():
        RuleModel(
            write_time=rule['write_time'],
            author=rule['author'],
            title=rule['title'],
            content=rule['content'],
            pinned=rule['pinned']
        ).save()


def _migration_report():
    facilities = db['facility_report']
    for facility in facilities.find():
        FacilityReportModel(
            report_time=facility['report_time'],
            author=facility['author'],
            content=facility['content'],
            room=facility['room']
        ).save()


def _migration_version():
    versions = db['version']
    for version in versions.find():
        if version['platform'].upper == 'ANDROID':
            platform = 2
        elif version['platform'].upper == 'IOS':
            platform = 3
        else:
            platform = 1

        VersionModel(
            platform=platform,
            version=version['version']
        ).save()


def _migration_meal():
    meal = db['meal']
    for m in meal.find():
        MealModel(date=m['_id'], breakfast=m['breakfast'], lunch=m['lunch'], dinner=m['dinner']).save()


def _migration_refresh_tokens():
    token = db['refresh_token']
    for t in token.find():
        token_owner = StudentModel.objects(id=t['token_owner'].id).first() or\
            AdminModel.objects(id=t['token_owner'].id).first() or\
            SystemModel.objects(id=t['token_owner'].id).first()

        if not token_owner:
            continue

        RefreshTokenModel(token=t['_id'], token_owner=token_owner, pw_snapshot=t['pw_snapshot']).save()


def migration():
    _migration_account()
    _migration_point_rule()
    _migration_post()
    _migration_report()
    _migration_version()
    _migration_meal()
    _migration_refresh_tokens()

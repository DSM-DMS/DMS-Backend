from bson.objectid import ObjectId
from datetime import datetime

from pymongo import MongoClient

from app.models.v2.account import *
from app.models.v2.apply import *
from app.models.v2.meal import *
from app.models.v2.point import *
from app.models.v2.post import *
from app.models.v2.report import *
from app.models.v2.version import *

client = MongoClient()
db = client['dms']


def _migration_account():
    def _migrate_apply(query_res, student_obj):
        if 'stay_apply' in query_res:
            stay_apply = query_res['stay_apply']

            apply_date = stay_apply['apply_date']
            value = stay_apply['value']
        else:
            apply_date = datetime.now()
            value = 4

        StayApplyModel(student=student_obj, apply_date=apply_date, value=value).save()

        if 'goingout_apply' in query_res:
            goingout_apply = query_res['goingout_apply']

            apply_date = goingout_apply['apply_date']
            on_saturday = goingout_apply['on_saturday']
            on_sunday = goingout_apply['on_sunday']
        else:
            apply_date = datetime.now()
            on_saturday = False
            on_sunday = False

        GoingoutApplyModel(
            student=student_obj,
            apply_date=apply_date,
            on_saturday=on_saturday,
            on_sunday=on_sunday
        ).save()

    account_col = db['account_base']

    account_count = 0

    for account in account_col.find():
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
            ).save()

            _migrate_apply(account, student)

            account_count += 1

        elif account['_cls'] == 'AdminModel':
            AdminModel(
                signup_time=account['signup_time'] if 'signup_time' in account else datetime.now(),
                id=account['_id'],
                pw=account['pw'],
                name=account['name']
            ).save()

            account_count += 1
        else:
            SystemModel(
                signup_time=account['signup_time'] if 'signup_time' in account else datetime.now(),
                id=account['_id'],
                pw=account['pw'],
                name=account['name']
            ).save()

            account_count += 1

    print('Migrated {} accounts'.format(account_count))


def _migration_point_rule():
    point_rule_col = db['point_rule']

    point_rule_count = 0

    for point_rule in point_rule_col.find():
        PointRuleModel(
            name=point_rule['name'],
            point_type=point_rule['point_type'],
            min_point=point_rule['min_point'],
            max_point=point_rule['max_point']
        ).save()

        point_rule_count += 1

    print('Migrated {} rules'.format(point_rule_count))


def _migration_post():
    faq_col = db['faq']
    notice_col = db['notice']
    rule_col = db['rule']

    faq_count = notice_count = rule_count = 0

    for FAQ in faq_col.find():
        FAQModel(
            write_time=FAQ['write_time'],
            author=FAQ['author'],
            title=FAQ['title'],
            content=FAQ['content'],
            pinned=FAQ['pinned']
        ).save()

        faq_count += 1

    print('Migrated {} FAQs'.format(faq_count))

    for notice in notice_col.find():
        NoticeModel(
            write_time=notice['write_time'],
            author=notice['author'],
            title=notice['title'],
            content=notice['content'],
            pinned=notice['pinned']
        ).save()

        notice_count += 1

    print('Migrated {} notices'.format(notice_count))

    for rule in rule_col.find():
        RuleModel(
            write_time=rule['write_time'],
            author=rule['author'],
            title=rule['title'],
            content=rule['content'],
            pinned=rule['pinned']
        ).save()

        rule_count += 1

    print('Migrated {} rules'.format(rule_count))


def _migration_report():
    facility_report_col = db['facility_report']

    facility_report_count = 0

    for facility in facility_report_col.find():
        FacilityReportModel(
            report_time=facility['report_time'],
            author=facility['author'],
            content=facility['content'],
            room=facility['room']
        ).save()

        facility_report_count += 1

    print('Migrated {} facility reports'.format(facility_report_count))


# def _migration_version():
#     version_col = db['version']
#
#     version_count = 0
#
#     for version in version_col.find():
#         if version['platform'].upper == 'ANDROID':
#             platform = 2
#         elif version['platform'].upper == 'IOS':
#             platform = 3
#         else:
#             platform = 1
#
#         VersionModel(
#             platform=platform,
#             version=version['version']
#         ).save()
#
#         version_count += 1
#
#     print('Migrated {} version data'.format(version_count))


def _migration_meal():
    meal_col = db['meal']

    meal_count = 0

    for m in meal_col.find():
        MealModel(date=m['_id'], breakfast=m['breakfast'], lunch=m['lunch'], dinner=m['dinner']).save()

        meal_count += 1

    print('Migrated {} meals'.format(meal_count))


def _migration_refresh_tokens():
    token_col = db['refresh_token']

    token_count = 0

    for token in token_col.find():
        token_owner = StudentModel.objects(id=token['token_owner'].id).first() or\
            AdminModel.objects(id=token['token_owner'].id).first() or\
            SystemModel.objects(id=token['token_owner'].id).first()

        if not token_owner:
            continue

        RefreshTokenModel(token=token['_id'], token_owner=token_owner, pw_snapshot=token['pw_snapshot']).save()

        token_count += 1

    print('Migrated {} refresh tokens'.format(token_count))


def migration():
    start_migration = input('Start migration? (Y/N)')

    if start_migration.upper() == 'N':
        return

    _migration_account()
    _migration_point_rule()
    _migration_post()
    _migration_report()
    # _migration_version()
    _migration_meal()
    _migration_refresh_tokens()

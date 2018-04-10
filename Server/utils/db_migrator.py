from pymongo import MongoClient

from app_v2.models.account import *
from app_v2.models.point import *
from app_v2.models.post import *
from app_v2.models.report import *
from app_v2.models.version import *

client = MongoClient()
db = client['dms']


def _migration_account():
    student = db['student_model']
    for student_account in student.find():
        StudentModel(
            signup_time=student_account['signup_time'],
            id=student_account['id'],
            pw=student_account['pw'],
            name=student_account['name'],

            number=student_account['number'],
            good_point=student_account['good_point'],
            bad_point=student_account['bad_point'],
            point_histories=student_account['point_history'],
            penalty_training_status=student_account['penalty_training_status'],
            penalty_level=student_account['penalty_level']
        ).save()

    admin = db['admin_model']
    for admin_account in admin.find():
        AdminModel(
            signup_time=admin_account['signup_time'],
            id=admin_account['id'],
            pw=admin_account['pw'],
            name=admin_account['name']
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
    for version in versions:
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


def migration():
    _migration_account()
    _migration_point_rule()
    _migration_post()
    _migration_report()
    # _migration_version()
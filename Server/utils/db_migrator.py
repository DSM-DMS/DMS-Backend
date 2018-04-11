from pymongo import MongoClient

from app_v2.models.account import *
from app_v2.models.point import *
from app_v2.models.post import *
from app_v2.models.report import *
from app_v2.models.version import *

client = MongoClient()
db = client['dms']


def _migration_account():
    account = db['account_base']
    for account in account.find():
        if account['_cls'] == 'StudentModel':
            StudentModel(
                signup_time=account['signup_time'],
                id=account['id'],
                pw=account['pw'],
                name=account['name'],

                number=account['number'],
                good_point=account['good_point'],
                bad_point=account['bad_point'],
                point_histories=account['point_history'],
                penalty_training_status=account['penalty_training_status'],
                penalty_level=account['penalty_level']
            ).save()

        else:
            AdminModel(
                signup_time=account['signup_time'],
                id=account['id'],
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
# import os
#
# import pymysql
# from pymysql.cursors import DictCursor
#
# from app.models.account import StudentModel
# from app.models.apply import GoingoutApplyModel, StayApplyModel
# from app.models.post import FAQModel, NoticeModel, RuleModel
#
# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password=os.getenv('MYSQL_PW'),
#     db='dsm_dms',
#     charset='utf8'
# )
#
#
# def migrate_apply(id, uuid):
#     student = StudentModel.objects(id=id).first()
#
#     cursor = connection.cursor(DictCursor)
#
#     cursor.execute("SELECT * FROM goingout_apply WHERE uid='{0}'".format(uuid))
#     result = cursor.fetchall()
#     goingout_apply = GoingoutApplyModel(on_saturday=result[0]['sat'], on_sunday=result[0]['sun']) if result else None
#
#     cursor.execute("SELECT * FROM stay_apply WHERE uid='{0}'".format(uuid))
#     result = cursor.fetchall()
#     stay_apply = StayApplyModel(value=result[0]['value']) if result else None
#
#     student.update(goingout_apply=goingout_apply, stay_apply=stay_apply)
#
#
# def migrate_posts():
#     FAQModel.drop_collection()
#     NoticeModel.drop_collection()
#     RuleModel.drop_collection()
#
#     cursor = connection.cursor(DictCursor)
#
#     cursor.execute('SELECT * FROM faq')
#     faqs = cursor.fetchall()
#     for faq in faqs:
#         FAQModel(title=faq['title'], content=faq['content'], author='사감실').save()
#
#     cursor.execute('SELECT * FROM notice')
#     notices = cursor.fetchall()
#     for notice in notices:
#         NoticeModel(title=notice['title'], content=notice['content'], author='사감실').save()
#
#     cursor.execute('SELECT * FROM rule')
#     rules = cursor.fetchall()
#     for rule in rules:
#         RuleModel(title=rule['title'], content=rule['content'], author='사감실').save()

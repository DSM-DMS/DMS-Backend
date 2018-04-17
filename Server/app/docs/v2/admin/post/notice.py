from app.docs.v2.admin.post import *

TYPE = '공지사항'

NOTICE_POST = get_post_doc(TYPE)
NOTICE_PATCH = get_patch_doc(TYPE)
NOTICE_DELETE = get_delete_doc(TYPE)

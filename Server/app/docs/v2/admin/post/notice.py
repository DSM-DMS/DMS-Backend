from app.docs.v2.admin.post import *

TYPE = '공지사항'

NOTICE_POST = generate_post_doc(TYPE)
NOTICE_PATCH = generate_patch_doc(TYPE)
NOTICE_DELETE = generate_delete_doc(TYPE)

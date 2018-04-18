from app.docs.v2.admin.post import *

TYPE = '기숙사규정'

RULE_POST = generate_post_doc(TYPE)
RULE_PATCH = generate_patch_doc(TYPE)
RULE_DELETE = generate_delete_doc(TYPE)

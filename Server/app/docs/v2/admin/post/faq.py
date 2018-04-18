from app.docs.v2.admin.post import *

TYPE = 'FAQ'

FAQ_POST = generate_post_doc(TYPE)
FAQ_PATCH = generate_patch_doc(TYPE)
FAQ_DELETE = generate_delete_doc(TYPE)

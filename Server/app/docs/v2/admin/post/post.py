from app.docs.v2 import SAMPLE_OBJECT_IDS

POST_POST = {
    'tags': ['[Admin] 게시글 관리'],
    'description': '게시글 업로드',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'category',
            'description': '게시글 카테고리(faq, notice, rule)',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '게시글 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': '게시글 내용',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '게시글 업로드에 성공했으며, 업로드된 게시글의 ID를 응답합니다.',
            'examples': {
                '': {
                    'id': SAMPLE_OBJECT_IDS[0]
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POST_PATCH = {
    'tags': ['[Admin] 게시글 관리'],
    'description': '게시글 수정',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'category',
            'description': '게시글 카테고리(faq, notice, rule)',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'post_id',
            'description': '수정할 게시글의 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '수정할 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': '수정할 내용',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '수정 성공'
        },
        '204': {
            'description': '존재하지 않는 게시글 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POST_DELETE = {
    'tags': ['[Admin] 게시글 관리'],
    'description': '게시글 삭제',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'category',
            'description': '게시글 카테고리(faq, notice, rule)',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'post_id',
            'description': '삭제할 게시글의 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '삭제 성공'
        },
        '204': {
            'description': '존재하지 않는 게시글 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

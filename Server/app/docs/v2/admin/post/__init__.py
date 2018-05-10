from app.docs.v2 import SAMPLE_OBJECT_IDS


def generate_post_doc(type):
    return {
        'tags': ['[Admin] 게시글 관리'],
        'description': '{} 업로드'.format(type),
        'parameters': [
            {
                'name': 'Authorization',
                'description': 'JWT Token',
                'in': 'header',
                'type': 'str',
                'required': True
            },
            {
                'name': 'title',
                'description': '{} 제목'.format(type),
                'in': 'json',
                'type': 'str',
                'required': True
            },
            {
                'name': 'content',
                'description': '{} 내용'.format(type),
                'in': 'json',
                'type': 'str',
                'required': True
            }
        ],
        'responses': {
            '201': {
                'description': '{} 업로드 성공했으며, 업로드된 {}의 ID를 응답합니다.'.format(type, type),
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


def generate_patch_doc(type):
    return {
        'tags': ['[Admin] 게시글 관리'],
        'description': '{} 수정'.format(type),
        'parameters': [
            {
                'name': 'Authorization',
                'description': 'JWT Token',
                'in': 'header',
                'type': 'str',
                'required': True
            },
            {
                'name': 'post_id',
                'description': '수정할 {}의 ID'.format(type),
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


def generate_delete_doc(type):
    return {
        'tags': ['[Admin] 게시글 관리'],
        'description': '{} 삭제'.format(type),
        'parameters': [
            {
                'name': 'Authorization',
                'description': 'JWT Token',
                'in': 'header',
                'type': 'str',
                'required': True
            },
            {
                'name': 'post_id',
                'description': '삭제할 {}의 ID'.format(type),
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

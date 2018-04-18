def generate_preview_post_doc(type):
    return {
        'tags': ['게시글 관리'],
        'description': '{} 프리뷰를 설정합니다.'.format(type),
        'parameters': [
            {
                'name': 'Authorization',
                'description': 'JWT Token',
                'in': 'header',
                'type': 'str',
                'required': True
            },
            {
                'name': 'id',
                'description': '프리뷰를 설정할 {}의 ID'.format(type),
                'in': 'json',
                'type': 'str',
                'required': True
            }
        ],
        'responses': {
            '201': {
                'description': '설정 성공'
            },
            '204': {
                'description': '존재하지 않는 게시글 ID'
            },
            '403': {
                'description': '권한 없음'
            }
        }
    }


FAQ_PREVIEW_POST = generate_preview_post_doc('FAQ')
NOTICE_PREVIEW_POST = generate_preview_post_doc('공지사항')
RULE_PREVIEW_POST = generate_preview_post_doc('기숙사규정')

PREVIEW_POST = {
    'tags': ['[Admin] 게시글 관리'],
    'description': '게시글 프리뷰를 설정합니다.',
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
            'name': 'id',
            'description': '프리뷰를 설정할 게시글의 ID',
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

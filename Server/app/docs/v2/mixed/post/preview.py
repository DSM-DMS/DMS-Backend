PREVIEW_GET = {
    'tags': ['[Mixed] 게시글'],
    'description': '게시글 프리뷰를 조회합니다. 별도로 프리뷰로 설정된 게시글이 없으면 가장 최신 글을 불러옵니다.',
    'parameters': [
        {
            'name': 'category',
            'description': '프리뷰를 조회할 게시글 카테고리(faq, notice, rule)',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '프리뷰 조회 성공',
            'examples': {
                '': {
                    'writeTime': '2017-10-11',
                    'author': '교촌치킨',
                    'title': '치킨 먹는법',
                    'content': '교촌허니콤보를 웨지감자와 함께'
                }
            }
        },
        '204': {
            'description': '게시글이 하나도 없어 반환할 정보가 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

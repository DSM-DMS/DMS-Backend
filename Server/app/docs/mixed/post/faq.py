FAQ_LIST_GET = {
    'tags': ['게시글', '게시글 관리'],
    'description': 'FAQ 리스트',
    'responses': {
        '200': {
            'description': 'FAQ 리스트 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'id': 'fkdo13kroafdgmb',
                        'write_time': '2017-10-11',
                        'author': '교촌치킨',
                        'title': '치킨 먹는법',
                        'pinned': True
                    },
                    {
                        'id': 'eoqk1kcmdkallw',
                        'write_time': '2017-10-13',
                        'author': '코레일',
                        'title': 'KTX 싸게 예매하는법',
                        'pinned': False
                    },
                    {
                        'id': 'p1o9d0vmzjswek',
                        'write_time': '2017-10-16',
                        'author': '갓석진',
                        'title': '서울에서 먹고살기',
                        'pinned': False
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

FAQ_ITEM_GET = {
    'tags': ['게시글', '게시글 관리'],
    'description': 'FAQ 내용 조회',
    'parameters': [
        {
            'name': 'post_id',
            'description': '조회할 FAQ 아이템의 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'FAQ 조회 성공',
            'examples': {
                'application/json': {
                    'write_time': '2017-10-11',
                    'author': '교촌치킨',
                    'title': '치킨 먹는법',
                    'content': '교촌허니콤보를 웨지감자와 함께',
                    'pinned': True
                }
            }
        },
        '204': {
            'description': 'FAQ 조회 실패(존재하지 않는 ID)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

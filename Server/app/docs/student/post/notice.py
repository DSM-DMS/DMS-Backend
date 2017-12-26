NOTICE_LIST_GET = {
    'tags': ['게시글'],
    'description': '공지사항 리스트',
    'responses': {
        '200': {
            'description': '공지사항 리스트 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'id': 'fkdo13kroafdgmb',
                        'write_date': '2017-10-11',
                        'author': '사감부',
                        'title': '치킨 먹자',
                        'pinned': True
                    },
                    {
                        'id': 'eoqk1kcmdkallw',
                        'write_date': '2017-10-13',
                        'author': '교육부',
                        'title': '아침운동 제거 안내',
                        'pinned': False
                    },
                    {
                        'id': 'p1o9d0vmzjswek',
                        'write_date': '2017-10-16',
                        'author': '사감부',
                        'title': '내일 아침 11시 기상 안내',
                        'pinned': False
                    }
                ]
            }
        },
    }
}

NOTICE_ITEM_GET = {
    'tags': ['게시글'],
    'description': '공지사항 내용 조회',
    'parameters': [
        {
            'name': 'id',
            'description': '조회할 공지사항 아이템의 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '공지사항 조회 성공',
            'examples': {
                'application/json': {
                    'write_date': '2017-10-16',
                    'author': '사감부',
                    'title': '내일 아침 11시 기상 안내',
                    'content': '11시 기상 후 9시간동안 자습 줍니다. 그리고 하교 개꿀 동의? 어 보감~',
                    'pinned': False
                }
            }
        },
        '204': {
            'description': '공지사항 조회 실패(존재하지 않는 ID)'
        }
    }
}

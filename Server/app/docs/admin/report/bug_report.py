BUG_REPORT_GET = {
    'tags': ['신고 관리'],
    'description': '버그신고 리스트 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '버그신고 리스트 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'author': '이병찬',
                        'title': 'DMS 앱이 왜 안나와요',
                        'content': '내가쥔짜 이걸 얼마나 열쒸미했는데말양'
                    },
                    {
                        'author': '조민규',
                        'title': '항아리게임은 누가만들었어요?',
                        'content': '진짜 게임 시ㅂ'
                    },
                    {
                        'author': '김동규',
                        'title': '태초마을이야!',
                        'content': '이제야 도착했어 피카츄! (피카피카!) 어때 토개피 너도 기분좋지?'
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

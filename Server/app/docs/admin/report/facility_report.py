FACILITY_REPORT_DOWNLOAD_GET = {
    'tags': ['신고 관리'],
    'description': '시설고장신고 리스트 조회',
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
            'description': '시설고장신고 리스트 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'author': '이병찬',
                        'title': '방에서 냄새가 나요',
                        'content': '내 발냄새인거같기도 하고',
                        'room': 415
                    },
                    {
                        'author': '조민규',
                        'title': '계엄령을 선포한다',
                        'content': '치킨먹고싶어',
                        'room': 415
                    },
                    {
                        'author': '김동규',
                        'title': '피카츄가 포켓볼에서 안나와요',
                        'content': '내가 이걸 얼마주고 샀는데',
                        'room': 320
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

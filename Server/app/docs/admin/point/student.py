STUDENT_MANAGING_GET = {
    'tags': ['상벌점 관리'],
    'description': '학생 목록 조회',
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
            'description': '목록 조회 성공. 학번 기준으로 오름차순 정렬됩니다.',
            'examples': {
                'application/json': [
                    {
                        'id': 'city7310',
                        'name': '조민규',
                        'number': 2120,
                        'good_point': 1,
                        'bad_point': 15,
                        'bad_point_status': 2,
                        'point_histories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '치킨 먹음',
                                'point': 4
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '이유 없음',
                                'point': -3
                            }
                        ],
                        'penalty_trained': False
                    },
                    {
                        'id': 'geni429',
                        'name': '정근철',
                        'number': 2117,
                        'good_point': 0,
                        'bad_point': 0,
                        'bad_point_status': 0,
                        'point_histories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '치킨 먹음',
                                'point': 4
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '이유 없음',
                                'point': -3
                            }
                        ],
                        'penalty_trained': False
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

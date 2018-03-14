STUDENT_MANAGING_GET = {
    'tags': ['상벌점 관리'],
    'description': '학생 목록 조회. 벌점 교육 단계는 9점 이하가 0, 10점 이상이 1, 15점 이상 2, ...',
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
                        'penalty_level': 2,
                        'point_histories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '깔끔한 청소',
                                'point_type': True,
                                'point': 4
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '치킨 냠냠',
                                'point_type': False,
                                'point': 3
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
                        'penalty_level': 0,
                        'point_histories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '기타 잘침',
                                'point_type': True,
                                'point': 5
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '기타 줄 자습실에 버림',
                                'point_type': False,
                                'point': 4
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

STUDENT_PENALTY_MANAGING_PATCH = {
    'tags': ['상벌점 관리'],
    'description': '학생 벌점 교육 상태 변경',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '상벌점 교육 상태 변경 대상 학생 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'status',
            'description': '교육 상태(true : 교육됨, false : 교육되지 않음)',
            'in': 'formData',
            'type': 'bool',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '변경 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

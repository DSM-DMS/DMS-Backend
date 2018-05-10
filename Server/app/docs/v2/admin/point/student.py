STUDENT_LIST_GET = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '학생 목록을 조회합니다. 벌점 교육 단계는 9점 이하가 0, 10점 이상이 1, 15점 이상 2, 20점 이상 3, ...',
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
                '': [
                    {
                        'id': 'city7310',
                        'name': '조민규',
                        'number': 2120,
                        'goodPoint': 4,
                        'badPoint': 16,
                        'penaltyLevel': 3,
                        'pointHistories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '깔끔한 청소',
                                'pointType': True,
                                'point': 4
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '치킨 냠냠',
                                'pointType': False,
                                'point': 3
                            }
                        ],
                        'penaltyTrainingStatus': False
                    },
                    {
                        'id': 'geni429',
                        'name': '정근철',
                        'number': 2117,
                        'goodPoint': 5,
                        'badPoint': 4,
                        'penaltyLevel': 0,
                        'pointHistories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '기타 잘침',
                                'pointType': True,
                                'point': 5
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '기타 치다가 기타줄 끊어짐',
                                'pointType': False,
                                'point': 4
                            }
                        ],
                        'penaltyTrainingStatus': False
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

STUDENT_PENALTY_PATCH = {
    'tags': ['[Admin] 상벌점 관리'],
    'description': '특정 학생의 벌점 교육 상태를 변경합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'student_id',
            'description': '상벌점 교육 상태 변경 대상 학생 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        },
        {
            'name': 'status',
            'description': '교육 상태(true : 교육됨, false : 교육되지 않음)',
            'in': 'json',
            'type': 'bool',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '변경 성공'
        },
        '204': {
            'description': '존재하지 않는 학생 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

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
            'description': '목록 조회 성공. 상벌점 데이터가 없는 경우 상벌점과 벌점 교육 단계가 null입니다.',
            'examples': {
                'application/json': [
                    {
                        'id': 'city7310',
                        'name': '조민규',
                        'number': 2120,
                        'good_point': 1,
                        'bad_point': 50,
                        'penalty_training_status': 4
                    },
                    {
                        'id': 'geni429',
                        'name': '정근철',
                        'number': 2117,
                        'good_point': None,
                        'bad_point': None,
                        'penalty_training_status': None
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

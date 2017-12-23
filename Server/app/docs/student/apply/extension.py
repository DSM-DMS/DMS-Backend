EXTENSION_GET = {
    'tags': ['신청'],
    'description': '연장신청 정보 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '연장신청 정보 조회 성공',
            'examples': {
                'application/json': {
                    'class': 1,
                    'seat': 16
                }
            }
        },
        '204': {
            'description': '연장신청 정보 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

EXTENSION_POST = {
    'tags': ['신청'],
    'description': '연장신청',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'class',
            'description': '''
            연장 학습실 번호
            1: 가온실
            2: 나온실
            3: 다온실
            4: 라온실
            5: 3층 독서실
            6: 4층 독서실
            7: 5층 열린교실
            ''',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
        {
            'name': 'seat',
            'description': '연장 학습실 자리 번호',
            'in': 'formData',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '연장신청 성공'
        },
        '204': {
            'description': '연장신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

EXTENSION_MAP_GET = {
    'tags': ['신청'],
    'description': '연장신청 지도 조회',
    'parameters': [
        {
            'name': 'class',
            'description': '지도를 조회할 학습실 번호',
            'in': 'formData',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '지도 조회 성공',
            'examples': {
                'application/json(가온실)': [
                    [
                        1,
                        2,
                        0,
                        3,
                        4
                    ],
                    [
                        5,
                        6,
                        0,
                        "조민규",
                        8
                    ],
                    [
                        9,
                        10,
                        0,
                        11,
                        12
                    ],
                    [
                        13,
                        14,
                        0,
                        15,
                        16
                    ],
                    [
                        17,
                        18,
                        0,
                        19,
                        20
                    ]
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

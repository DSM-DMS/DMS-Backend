from app.docs.v2 import SAMPLE_OBJECT_IDS, jwt_header


FACILITY_REPORT_GET = {
    'tags': ['[Admin] 신고 정보 관리'],
    'description': '시설고장 신고 정보를 조회합니다.',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': '시설고장 신고 리스트 조회 성공',
            'examples': {
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'author': '이병찬',
                        'content': '내 발냄새인거같기도 하고',
                        'room': 415
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'author': '조민규',
                        'content': '치킨먹고싶어',
                        'room': 415
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[2],
                        'author': '김동규',
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


FACILITY_REPORT_DELETE = {
    'tags': ['[Admin] 신고 정보 관리'],
    'description': '시설고장 신고 정보를 삭제합니다.',
    'parameters': [
        jwt_header,
        {
            'name': 'id',
            'description': '삭제할 시설고장 신고 ID',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '시설고장신고 삭제 성공'
        },
        '204': {
            'description': '존재하지 않는 시설고장 신고 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

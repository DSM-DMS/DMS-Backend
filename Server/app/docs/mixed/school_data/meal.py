MEAL_GET = {
    'tags': ['학교'],
    'description': '급식 정보 조회',
    'parameters': [
        {
            'name': 'date',
            'description': '급식 정보를 조회할 날짜(YYYY-MM-DD)',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '급식 정보 있음',
            'examples': {
                'application/json': {
                    'breakfast': ['피자', '먹고싶다', '토마토쏘-쓰'],
                    'lunch': ['점심은', '파스타'],
                    'dinner': ['저녁은', '밥이고뭐고', '집가자']
                }
            }
        },
        '204': {
            'description': '급식 정보 없음'
        }
    }
}

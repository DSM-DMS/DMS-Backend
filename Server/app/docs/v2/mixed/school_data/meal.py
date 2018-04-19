MEAL_GET = {
    'tags': ['학교 정보'],
    'description': '특정 날짜에 대한 급식 정보를 조회합니다.',
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
            'description': '해당 날짜에 대한 급식 정보 있음',
            'examples': {
                '': {
                    'breakfast': ['교촌 허니콤보', 'BBQ 황금올리브', '굽네 갈비천왕'],
                    'lunch': ['참깨빵', '위에', '순쇠고기', '패티 두장', '특별한 소스', '양상추', '치즈', '피클', '양파까지'],
                    'dinner': ['집밥']
                }
            }
        },
        '204': {
            'description': '해당 날짜에 대한 급식 정보 없음'
        }
    }
}

def get_excel_doc(msg):
    return {
        'tags': ['신청 정보 다운로드'],
        'description': '{}신청 정보를 다운로드합니다.'.format(msg),
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
                'description': '{}신청 정보가 담긴 엑셀 파일 응답. Cache-Control: no-cache 헤더를 함께 응답'.format(msg)
            },
            '403': {
                'description': '권한 없음'
            }
        }
    }
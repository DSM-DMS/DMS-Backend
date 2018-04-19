BUG_REPORT_POST = {
    'tags': ['신고'],
    'description': '버그를 신고하며, Slackbot이 Slack의 #bug-report 채널로 메시지를 전송합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'platform',
            'description': '버그 신고를 한 플랫폼 타입(1: Android, 2: iOS, 3: Web)',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'content',
            'description': '버그 신고 내용',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '버그 신고 성공'
        },
        '400': {
            'description': 'platform 타입이 1, 2, 3 중 하나가 아님'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

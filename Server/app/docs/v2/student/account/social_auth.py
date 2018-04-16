ADD_SOCIAL_POST = {
    'tags': ['소셜 계정'],
    'description': '소셜 계정 연동',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'socialPlatform',
            'description': '소셜 계정 플랫폼',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': '소셜 계정 구분자',
            'description': '소셜 계정 구분자',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '소셜 계정 연동 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SOCIAL_AUTH_POST = {
    'tags': ['소셜 계정'],
    'description': '소셜 계정 로그인',
    'parameters': [
        {
            'name': '소셜 계정 구분자',
            'description': '소셜 계정 구분자',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '소셜 로그인 성공',
            'examples': {
                'application/json': {
                    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlkZW50aXR5IjoiYSIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE1NDA1NTc0NDYsImp0aSI6ImJiN2M3MjJmLTZkZjMtNDljYy1iZTk5LWRkMjMzNDU1NDRjZSIsIm5iZiI6MTUwOTAyMTQ0NiwiaWF0IjoxNTA5MDIxNDQ2fQ.wmytxSuQlH-KjhxO2EzrIioWHWgEnyiqWpRBwWuM15M',
                    'refreshToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTM5MDQ3NjMsImlkZW50aXR5IjoibmlsIiwiZnJlc2giOmZhbHNlLCJqdGkiOiI1Yzg1ZDAxNy1lYjIwLTRmYjgtYmVhYi1iYmYyZTQyY2NlYmYiLCJuYmYiOjE1MTM2NDU1NjMsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE1MTM2NDU1NjN9.075C0_-b-oqSWc-jz7G35y00erRVntpcqN9uMIAnvfI'
                }
            }
        },
        '401': {
            'description': '소셜 로그인 실패'
        }
    }
}
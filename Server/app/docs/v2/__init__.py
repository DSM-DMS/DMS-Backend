SAMPLE_UUID = '3e04'
SAMPLE_OBJECT_IDS = [
    '5acddc2bc2a93f68ce96f5c4',
    '5acddc2bc2a93f68ce96f5c9',
    '5acddc2bc2a93f68ce96f5ce'
]
SAMPLE_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.' \
                      'eyJmcmVzaCI6ZmFsc2UsImlkZW50aXR5IjoiYSIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE1NDA1NT' \
                      'c0NDYsImp0aSI6ImJiN2M3MjJmLTZkZjMtNDljYy1iZTk5LWRkMjMzNDU1NDRjZSIsIm5iZiI6MTUwOTA' \
                      'yMTQ0NiwiaWF0IjoxNTA5MDIxNDQ2fQ.' \
                      'wmytxSuQlH-KjhxO2EzrIioWHWgEnyiqWpRBwWuM15M'
SAMPLE_REFRESH_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.' \
                       'eyJleHAiOjE1MTM5MDQ3NjMsImlkZW50aXR5IjoibmlsIiwiZnJlc2giOmZhbHNlLCJqdGkiOiI1Y' \
                       'zg1ZDAxNy1lYjIwLTRmYjgtYmVhYi1iYmYyZTQyY2NlYmYiLCJuYmYiOjE1MTM2NDU1NjMsInR5cGU' \
                       'iOiJhY2Nlc3MiLCJpYXQiOjE1MTM2NDU1NjN9.' \
                       '075C0_-b-oqSWc-jz7G35y00erRVntpcqN9uMIAnvfI'

TEMPLATE = {
    'schemes': [
        'http'
    ],
    'tags': [
        {
            'name': '계정 관리',
            'description': '관리자 권한으로 접근 가능한 계정/계정 관리 API'
        },
        {
            'name': '관리자 계정',
            'description': '관리자 계정 관련 API'
        },
        {
            'name': '신청 정보 다운로드',
            'description': '관리자 권한으로 접근 가능한 신청 정보 엑셀 다운로드 API'
        },
        {
            'name': '상벌점 괸리',
            'description': '관리자 권한으로 접근 가능한 상벌점 관리 API'
        },
        {
            'name': '게시글 괸리',
            'description': '관리자 권한으로 접근 가능한 게시글 관리 API'
        },
        {
            'name': '신고 정보 관리',
            'description': '관리자 권한으로 접근 가능한 신고 정보 관리 API'
        }
    ]
}

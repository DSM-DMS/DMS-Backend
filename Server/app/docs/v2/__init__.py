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
        # --- Admin
        {
            'name': '[Admin] 계정',
            'description': '관리자 계정 관련 API'
        },
        {
            'name': '[Admin] 계정 관리',
            'description': '관리자 권한으로 접근 가능한 계정 관리 API'
        },
        {
            'name': '[Admin] 신청 정보',
            'description': '관리자 권한으로 접근 가능한 신청 정보 엑셀 다운로드 API'
        },
        {
            'name': '[Admin] 상벌점 관리',
            'description': '관리자 권한으로 접근 가능한 상벌점 관리 API'
        },
        {
            'name': '[Admin] 게시글 관리',
            'description': '관리자 권한으로 접근 가능한 게시글 관리 API'
        },
        {
            'name': '[Admin] 신고 정보 관리',
            'description': '관리자 권한으로 접근 가능한 신고 정보 관리 API'
        },
        {
            'name': '[Admin] 설문지 관리',
            'description': '관리자 권한으로 접근 가능한 설문지 관리 API'
        },
        # --- Admin

        # --- Mixed
        {
            'name': '[Mixed] JWT 관련',
            'description': '로그인 상태 체크, Access token refresh 등 JWT 관련 API'
        },
        {
            'name': '[Mixed] 메타데이터',
            'description': 'DMS에 들어갈 Github/Facebook 링크, 개발자 목록 등 메타데이터용 API'
        },
        {
            'name': '[Mixed] 게시글',
            'description': '로그인된 계정 권한으로 접근 가능한 게시글 API'
        },
        {
            'name': '[Mixed] 학교 정보',
            'description': '학교 정보 API'
        },
        # --- Mixed

        # --- Student
        {
            'name': '[Student] 계정',
            'description': '학생 계정 관련 API'
        },
        {
            'name': '[Student] 계정 관리',
            'description': '학생 계정으로 접근 가능한 계정 관리 API'
        },
        {
            'name': '[Student] 소셜 계정',
            'description': '학생 소셜 계정 관련 API'
        },
        {
            'name': '[Student] 신청',
            'description': '학생 신청 관련 API'
        },
        {
            'name': '[Student] 신고',
            'description': '학생 신고 관련 API'
        },
        {
            'name': '[Student] 설문 조사',
            'description': '학생 설문조사 관련 API'
        }
        # --- Student
    ]
}

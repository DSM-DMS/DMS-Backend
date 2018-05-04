from datetime import timedelta
import os


class Config:
    SERVICE_NAME = 'dms-v2'
    REPRESENTATIVE_HOST = 'dsm2015.cafe24.com'

    RUN_SETTING = {
        'threaded': True
    }

    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')
    # Secret key for any 3-rd party libraries

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
    JWT_HEADER_TYPE = 'JWT'

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'username': os.getenv('MONGO_ID'),
        'password': os.getenv('MONGO_PW')
    }

    INFLUX_DB_SETTINGS = {
        'db': SERVICE_NAME.replace('-', '_')
    }

    SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/'
    }

    SWAGGER_TEMPLATE = {
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

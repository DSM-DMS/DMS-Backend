DEVELOPER_INFO_GET = {
    'tags': ['[Mixed] 메타데이터'],
    'description': 'DMS 개발자 정보를 조회합니다.',
    'responses': {
        '200': {
            'description': '정보 조회 성공',
            'examples': {
                '': {
                    'app': ['조성빈', '이병찬', '윤정현', '이성현'],
                    'server': ['김성래', '조민규', '인상민'],
                    'webFrontend': ['김지수', '김건', '서윤호', '김형규', '오인서', '윤효상'],
                    'desktop': ['김경식', '정원태', '김동현', '이종현', '류근찬'],
                    'design': ['윤여환', '김동규']
                }
            }
        }
    }
}

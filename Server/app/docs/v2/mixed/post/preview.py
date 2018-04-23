def generate_preview_get_doc(type):
    return {
        'tags': ['[Mixed] 게시글'],
        'description': '{} 프리뷰를 조회합니다. 별도로 프리뷰로 설정된 게시글이 없으면 가장 최신 글을 불러옵니다.'.format(type),
        'responses': {
            '200': {
                'description': '프리뷰 조회 성공',
                'examples': {
                    '': {
                        'writeTime': '2017-10-11',
                        'author': '교촌치킨',
                        'title': '치킨 먹는법',
                        'content': '교촌허니콤보를 웨지감자와 함께',
                        'pinned': True
                    }
                }
            },
            '204': {
                'description': '게시글이 하나도 없어 반환할 정보가 없음'
            },
            '403': {
                'description': '권한 없음'
            }
        }
    }


FAQ_PREVIEW_GET = generate_preview_get_doc('FAQ')
NOTICE_PREVIEW_GET = generate_preview_get_doc('공지사항')
RULE_PREVIEW_GET = generate_preview_get_doc('기숙사규정')

# Project-DMS-Backend [![Build Status](https://travis-ci.org/DSM-DMS/Project-DMS-Backend.svg?branch=master)](https://travis-ci.org/DSM-DMS/Project-DMS-Backend)
## About
DMS 프로젝트의 2017년 12월 리메이크 일정에 의해 만들어진 백엔드 포지션의 Repository입니다.

### Technical Stacks
- Python
- Flask
- MongoDB
- JWT, ODM, Swagger, Cafe24, etc.

### 프로젝트 진행
1. TDD 기반으로 진행하며, 이를 위해 Flask 어플리케이션의 구조를 테스트에 알맞게 설계해 두었습니다.
~~~
|- app/
    |- __init__.py
    |- docs/
        |- __init__.py
    |- models/
        |- __init__.py
    |- static/
        |- css/
        |- img/
        |- js/
    |- templates/
        |- 403.html
        |- 404.html
        |- etc.
    |- views/
        |- __init__.py
    |- middleware.py
|- config/
    |- __init__.py
    |- dev.py
    |- production.py
|- tests/
    |- __init__.py
    |- mocks/
        |- __init__.py
    |- models/
        |- __init__.py
    |- views/
        |- __init__.py
|- server.py
~~~
2. 현재 저장소에 Travis CI를 적용하였습니다. 빌드 테스트와 리포팅을 위해 사용합니다.
3. 무조건 짧은 코드보단 유지보수 가능하며 명시적인 코드 작성을 지향합니다. 컨벤션은 기본적으로 모두 PEP8을 따릅니다.

## Contributors
- <a href="https://github.com/JoMingyu">2기 조민규</a>
- <a href="https://github.com/RISMME">3기 인상민</a>

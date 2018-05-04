# DMS for DSM - Backend [![Build Status](https://travis-ci.org/DSM-DMS/DMS-Backend.svg?branch=master)](https://travis-ci.org/DSM-DMS/DMS-Backend) [![Coverage Status](https://coveralls.io/repos/github/DSM-DMS/DMS-Backend/badge.svg?branch=master)](https://coveralls.io/github/DSM-DMS/DMS-Backend?branch=master) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/DSM-DMS/DMS-Backend/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/DSM-DMS/DMS-Backend/?branch=master) [![Code Intelligence Status](https://scrutinizer-ci.com/g/DSM-DMS/DMS-Backend/badges/code-intelligence.svg?b=master)](https://scrutinizer-ci.com/code-intelligence)

## Technical Stack
### Host
- cafe24
### API Architecture
- REST
- Swagger
### Software Stack
- Python
- Flask
### WAS
- nginx
### Database
- MongoDB(메인 데이터베이스) with Sharded Cluster
- Redis(Expire가 필요하거나 latency가 적어야 하는 캐싱 데이터)
### Monitoring
- InfluxDB(로그 데이터 저장)
- Grafana(시각화)
### TDD
- Travis-CI
- Coveralls(커버리지 리포트)
- Scrutinizer(코드 퀄리티 관리)

## 인프라 구축 과정에서의 특별한 점
### Swagger
1. 모든 API에 Swagger로 문서를 작성하고, 환경 변수로 관리되는 경로에서 문서를 제공합니다.
### Travis-CI
1. sudo를 false로 두어, Ubuntu Trusty 빌드 환경에서 docker 기반으로 빌드되도록 합니다. 이는 부팅 시간이 줄여 빌드 시간을 줄이기 위함입니다.
2. 모든 솔루션들을 docker 기반으로 실행합니다. apt-get 이후 서비스로 돌리는 것보다 이슈가 적고, 커맨드도 직관적이기 때문입니다.
3. before_script에서 `cd Server` 커맨드를 실행합니다. 개발 시 프로젝트를 Server 디렉토리로 잡기 때문에, 프로젝트 root directory를 `Server/`로 설정하여 로컬 테스트와 CI의 테스트 환경을 동일하게 하기 위함입니다.
4. run_test.py를 coverage 유틸리티로 실행합니다. `.coveragerc` 파일을 생성하여 coveralls에 업로드하고, 커버리지 리포트하기 위함입니다.
5. notification을 이메일이 아닌 slack 채널에 보냅니다.
### Scrutinizer
1. `web_files`를 `excluded_paths`에 등록하여, 코드 퀄리티 측정 대상에서 제외합니다.
### Database
1. Cafe24 ubuntu에서 apt-get을 실행할 때 발생하는 dpkg 관련 이슈 때문에, docker를 설치할 수 없어 screen에 MongoDB와 InfluxDB를 실행해 두었습니다.
2. MongoDB는 기본적으로 인증을 거치지 않는 형태로 동작합니다. 이는 외부에서 별도의 ID/PW 없이 바로 접근하여 DB를 조작할 수 있게 됩니다. MongoDB는 ID/PW로 접근하는 기본적인 보안 모델을 가지고 있으며, 일반적인 RDB들과 다르게 하나의 DB에 하나의 사용자가 할당되는 형식입니다. `root`라는 role을 가진 관리자 계정을 만들고, `mongod --auth`로 mongodb 서버를 재시작한 후, DMS 서버를 위한 계정을 별도로 생성하였습니다. 데이터베이스 비밀번호는 환경 변수에서 관리됩니다.

### 특수한 전제
#### 연장신청
- 11시 연장신청은 매일 오후 5시 30분부터 8시 30분까지
- 12시 연장신청은 매일 오후 5시 30분부터 10시까지
#### 외출신청
- 확실히 정해진 조건 없음
#### 잔류신청
- 매주 일요일 오후 8시 30분부터 목요일 오후 10시까지
#### 설문조사
- 한번 업로드한 설문조사는 수정 불가능

## Contributors
- <a href="https://github.com/JoMingyu">2기 조민규</a>
- <a href="https://github.com/RISMME">3기 인상민</a>

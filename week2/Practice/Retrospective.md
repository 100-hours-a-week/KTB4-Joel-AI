### venv
- 특정 프로젝트만을 위해 파이썬 인터프리터, 표준 라이브러리, 추가 패키지를 물리적으로 분리하는 기술 
- 글로벌 환경에 패키지를 설치 시 프로젝트 간 버전 충돌이 발생을 방지하기 위해 프로젝트 폴더 내부에 .venv를 생성하여 독립된 디렉터리에 패키지를 격리 설치
- 프로젝트의 순수 소스코드가 아니며 용량이 비대하므로 Git 추적에서 제외 -> .gitignore

### requirements.txt
- 현재 파이썬 가상환경에 설치된 외부 라이브러리의 이름과 정확한 버전 정보를 기록한 텍스트 파일
- 무거운 가상환경 폴더를 직접 공유하는 대신, 텍스트 포맷의 명세서만 추출하여 Git으로 공유
- pip freeze > requirements.txt 
-  pip install -r requirements.txt

### 한글 깨짐 문제
- FastAPI는 기본적으로 JSON 응답을 UTF-8로 내려주기 때문에 한글이 깨진다면 보통 보는 쪽의 인코딩 문제
- Python 객체 → JSON 직렬화 → UTF-8 인코딩 → application/json 헤더 설정
- 내장 브라우저에서는 dict list


### Extras
- fastapi dev (vs. uvicorn main:app --reload)
    - FastAPI 공식 CLI, 자동으로 app이라는 fastapi 인스턴스 찾아서 실행, reload 옵션 default
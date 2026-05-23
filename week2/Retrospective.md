### venv
- 특정 프로젝트만을 위해 파이썬 인터프리터, 표준 라이브러리, 추가 패키지를 물리적으로 분리하는 기술 
- 글로벌 환경에 패키지를 설치 시 프로젝트 간 버전 충돌이 발생을 방지하기 위해 프로젝트 폴더 내부에 .venv를 생성하여 독립된 디렉터리에 패키지를 격리 설치
- 프로젝트의 순수 소스코드가 아니며 용량이 비대하므로 Git 추적에서 제외 -> .gitignore

### requirements.txt
- 현재 파이썬 가상환경에 설치된 외부 라이브러리의 이름과 정확한 버전 정보를 기록한 텍스트 파일
- 무거운 가상환경 폴더를 직접 공유하는 대신, 텍스트 포맷의 명세서만 추출하여 Git으로 공유
- pip freeze > requirements.txt 
- pip install -r requirements.txt

### 한글 깨짐 문제
- FastAPI는 기본적으로 JSON 응답을 UTF-8로 내려주기 때문에 한글이 깨진다면 보통 보는 쪽의 인코딩 문제
- Python 객체 → JSON 직렬화 → UTF-8 인코딩 → application/json 헤더 설정
- 내장 브라우저에서는 dict list

### fastapi lifespan
- e.g., from contextlib import asynccontextmanager  (contextmanager <= decorator + generator)
- Application 시작과 종료까지의 기간
- 시작 이벤트와 종료 이벤트가 발생할 때 동작하는 로직 실행 가능하며, 시작 이벤트에서 발생한 리소스를 계속 유지 가능
- 본 과제에서는 서버 시작 시에만 DB 테이블을 만들기 위해 사용

### DB session (<-> 로그인 인증 세션)
- 백엔드 서버와 DB 간의 짧고 안전한 데이터 조작용 연결 통로
- context manager(with Session)로 DB session open
- generator(yield session)로 열린 session을 밖으로 던지고, 함수는 freeze = 세션은 열린 채로 유지
- 세션 사용(API 함수) 완료되면 함수 wake up, session close, db 연결 닫힘

### Dependency Injection
- e.g., Depends(get_session)
- API 엔드포인트에 필요한 외부 객체나 로직을 자동으로 주입

### Summary
- summaries.py(summarize_post_api(), 라우터) -> summary_service.py(summarize_post(), 서비스) -> summarizer(summarize(), 실제 llm api)

### Project Structure
main.py
app/
 ├─ routers/
 │   ├─ posts.py            # 게시글/댓글 API
 │   └─ summaries.py        # 요약 API
 ├─ services/
 │   └─ summary_service.py  # 요약 비즈니스 로직
 ├─ ai/
 │   ├─ summarizer.py       # 실제 추론
 │   └─ prompt.py           # 프롬프트 생성
 ├─ schemas.py              # 요청/응답 DTO
 ├─ database.py             # SQLite 연결, DB 테이블 생성, Session 제공
 └─ models.py               # 실제 DB 테이블 모델

### Extras
- "fastapi dev" (vs."uvicorn main:app --reload")
    - FastAPI 공식 CLI, 자동으로 app이라는 fastapi 인스턴스 찾아서 실행, reload 옵션 default


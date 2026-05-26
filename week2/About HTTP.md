# HTTP(HyperText Transfer Protocol)
- **What?** 파일이나 문서들이 링크를 통해 서로 연결되어 있는 **구조화된 텍스트**(html, css, js, png, jpeg)를 전송하기 위해 사용되는 통신 규약
- **Why?** 웹 서버와 클라이언트 간의 **표준화 된 문서 전송**을 위해
- **How?** 클라이언트가 **URL**을 통해 특정 웹 주소로 요청을 보냄


### HTTP Message
- client-server 간 파일 전달 통신의 기본 단위
  - Start Line: Request, Response의 status
  - HTTP Headers: Message Body를 요약하는 header들의 집합
  - Empty Line: Header와 본문을 구분하기 위한 빈 줄
  - Body: 실제 내용(HTML, JSON)
- HTTP Request  

    ![image1.png](./img/HTTP_REQUEST.png)

- HTTP Response  

    ![image2.png](./img/HTTP_RESPONSE.png)

※ FastAPI 에서는?
- **Pydantic Model**(Request Body의 데이터 구조와 타입을 정의하는 DTO 역할)을 사용하여 요청으로 전달된 데이터를 해당 모델로 변환하는 과정에서 자동으로 Request Body 유효성 검사를 수행

### HTTP 특징
- **Client-Server 구조**: 클라이언트가 요청(Request)을 보내면 서버가 응답(Response)을 반환
- **Stateless**: 서버가 이전 요청의 상태를 기억하지 않음
  - 매 요청은 독립적으로 처리
  - 로그인 상태처럼 유지가 필요한 정보는 Cookie, Session, Token 등을 사용 (Cookie: client browser, Session: server)
- **Connectionless**: 요청과 응답이 끝나면 연결 종료
  - 서버 자원의 효율적 사용, 유지비용 감소
  - HTTP/1.1 Keep-Alive (일정 시간 연결 재사용 가능)
  - HTTP/2 Multiplexing (스트림 다중화를 통한 병렬 통신)


### HTTP Method
- 클라이언트가 서버에게 어떤 작업을 원하는지 알려주는 방식
- **GET**: 리소스 조회
- **POST**: 새로운 리소스 생성 또는 데이터 전달
- **PUT**: 리소스 전체 수정
- **PATCH**: 리소스 일부 수정
- **DELETE**: 리소스 삭제

※ RESTful API란?
- 클라이언트와 서버가 데이터를 주고받기 위해 REST(Representational State Transfer) 아키텍처 스타일의 설계 원칙을 충실하게 지켜서 만든 HTTP 기반 API

※ FastAPI 에서는?
- `@app.get()`, `@app.post()`, `@app.put()`, `@app.patch()`, `@app.delete()` 처럼 데코레이터로 HTTP Method를 지정


### HTTP Status Code
- 서버가 요청 처리 결과를 숫자로 알려주는 응답 코드
- **1xx**: 요청을 처리 중
- **2xx**: 요청 성공
  - `200 OK`: 요청 성공
  - `201 Created`: 리소스 생성 성공
- **3xx**: 리다이렉션
  - `301 Moved Permanently`: 영구 이동
  - `302 Found`: 임시 이동
- **4xx**: 클라이언트 오류
  - `400 Bad Request`: 잘못된 요청
  - `401 Unauthorized`: 인증 필요
  - `403 Forbidden`: 권한 없음
  - `404 Not Found`: 리소스를 찾을 수 없음
- **5xx**: 서버 오류
  - `500 Internal Server Error`: 서버 내부 오류
  - `503 Service Unavailable`: 서버가 일시적으로 요청 처리 불가


### URL 구조
- 클라이언트가 요청을 보낼 리소스의 위치를 나타내는 주소

```
https://example.com:443/posts?page=1&size=10
```

- **Scheme, Protocol**: `https`
- **Host**: `example.com`
- **Port**: `443`
- **Path**: `/posts`
- **Query String**: `page=1&size=10`


### HTTP vs HTTPS
- **HTTP**: 데이터를 암호화하지 않고 전송
- **HTTPS**: HTTP에 SSL/TLS 암호화를 적용한 방식

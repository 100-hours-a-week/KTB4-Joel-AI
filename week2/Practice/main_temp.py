from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

# cd .\week2\Practice\
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .\.venv\Scripts\activate.ps1

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "todos.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=True) # DB 연결의 중심 객체, echo = 터미널에 실제 SQL 찍히도록

# TODO: 커뮤니티 게시판
# Post CRUD: 제목, 내용, 글쓴이, 좋아요 수, 댓글 수, 조회수, 작성 시간
# Comment CRUD: 본문, 글쓴이, 작성 시간

# main.py
# app/
#  ├─ routers/
#  │   ├─ posts.py
#  │   └─ summaries.py        # 요약 API 입구
#  ├─ services/
#  │   └─ summary_service.py  # 요약 비즈니스 로직
#  ├─ ai/
#  │   ├─ model_loader.py     # 모델 로딩
#  │   ├─ summarizer.py       # 실제 추론 함수
#  │   └─ prompt.py           # 프롬프트 템플릿
#  ├─ schemas/
#  │   └─ summary_schema.py   # 요청/응답 DTO
#  └─ database.py



class TodoBase(SQLModel): # 공통 필드를 모아둔 클래스 -> Todo 관련 모델들이 같은 필드를 반복해서 쓰기 때문
    title: str
    done: bool = False


class Todo(TodoBase, table=True): # 실제 DB 테이블 모델, table=True면 SQLite에 실제 table 제작
    id: int | None = Field(default=None, primary_key=True)


class TodoCreate(TodoBase): # 생성 요청 모델, 새로운 todo를 만들 때 클라이언트가 아닌 DB가 id를 정해야 하기 때문에, Todo 대신 Todo Create사용 
    pass


class TodoRead(TodoBase): # 여긴 무조건 id가 int인 것만 읽어야 한다
    id: int


class TodoUpdate(SQLModel): # PATCH 요청용, 하나의 column값 만 patch할 수도 있으므로, optional
    title: str | None = None
    done: bool | None = None


def get_session(): # Session == 실제 DB 작업 단위
    with Session(engine) as session: # 처리가 끝나면 자동으로 session close 까지
        yield session # FastAPI dependency

def create_db_and_tables(): # table=True 모델로 DB 제작, 첫 실행 때만 제작, 이미 있으면 만들지 x
    SQLModel.metadata.create_all(engine)

@asynccontextmanager # 서버 시작 시 DB 테이블 생성, 1회성 작업이기에 close 필요 없음
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Hello FastAPI with SQLModel"}


@app.get("/todos", response_model=list[TodoRead])
def get_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo).order_by(Todo.id)).all()
    return todos


@app.get("/todos/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@app.post("/todos", response_model=TodoRead, status_code=201)
def create_todo(todo_create: TodoCreate, session: Session = Depends(get_session)):
    todo = Todo.model_validate(todo_create)

    session.add(todo)
    session.commit() # DB 저장
    session.refresh(todo) # python 객체에 반영

    return todo


@app.patch("/todos/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo_update: TodoUpdate, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    update_data = todo_update.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    todo.sqlmodel_update(update_data)
    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    session.delete(todo)
    session.commit()

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()


class TodoCreate(BaseModel):
    title: str
    done: bool = False


todos = [
    {"id": 1, "title": "FastAPI 설치하기", "done": True},
    {"id": 2, "title": "API 요청 보내보기", "done": False},
]


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/todos")
def get_todos():    
    return todos
    # return JSONResponse(
    #         content=todos, 
    #         media_type="application/json; charset=utf-8" # for safari
    #     )


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}


@app.post("/todos")
def create_todo(todo: TodoCreate):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "done": todo.done,
    }
    todos.append(new_todo)
    return new_todo
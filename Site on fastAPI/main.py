from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Сайт на FastAPi",
    description="Первое описание",
    version="1.0.1",
)

# 1. Модель данных (схема)
# Она гарантирует, что пользователь всегда имеет имя и возраст
class User(BaseModel):
    id: int
    name: str
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


# 2. Наша "База данных" Хранится в ОЗУ и не сохраняет изменения после ребута
users_db = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 19},
    {"id": 3, "name": "Ivan", "age": 21},
    {"id": 4, "name": "Oleg", "age": 23},
    {"id": 5, "name": "Prihod", "age": 41},
]
#Динамический URL через async
@app.get("/users/{user_id}")
async def read_user(user_id: int): # Добавили ': int'
    return {"user_id": user_id,"type": str(type(user_id))}


@app.get("/")
def get_user(user_id: int):
    """Возвращает конкретного пользователя по ID"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")



@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Возвращает конкретного пользователя по ID"""
    for user in users_db:
        if user["id"] == user_id:
            return user
        # Если не нашли - выдаем 404
    raise HTTPException(status_code=404, detail="User not found")




@app.post("/users")
def create_user(user: User):
    """Добавляет нового пользователя"""
    # Превращаем модель Pydantic в словарь и добавляем в список
    users_db.append(user.model_dump())
    return {"message": "User created", "user": user}

@app.put("/users/{user_id}")
def update_user_complete(user_id: int,updated_user: User):
    """Полностью заменяет пользователя с указанным ID"""
    for index,user in enumerate(users_db):
        if user["id"] == user_id:
        # Полная замена элемента списка
            users_db[index] == updated_user.model_dump()
        return {"message": "User updated completely", "user":updated_user}
    
    raise HTTPException(status_code=404, detail="User not found")

@app.patch("/users/{user_id}")
def update_user_partial(user_id: int, user_update: UserUpdate):
    for user in users_db:
        if user["id"] == user_id:
            # Если прислали имя — обновляем имя
            if user_update.name is not None:
                user["name"] = user_update.name
            # Если прислали возраст — обновляем возраст
            if user_update.age is not None:
                user["age"] = user_update.age
            return {"message": "User updated partially", "user": user}
            
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Удаляет пользователя по ID"""
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[index] #Удаляем из списка
            return {"message": f"User {user_id} deleted"}
    
    raise HTTPException(status_code=404, detail="User not found")






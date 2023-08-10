from typing import List, Optional
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
import uvicorn

from models import Roles
from models import User
from models import Gender



app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)  # Specify port 8080

db: List[User] = [

    User(
        id = UUID("e4c15b6e-e5da-4ff1-89b8-a710c2bb192b"),
        first_name='David',
        last_name='Gyebi',
        middle_name = None,
        gender=Gender.male,
        roles =[Roles.user, Roles.admin]
        ),

    User(
        id = UUID("96cb10de-1a12-46fd-b889-cd961d41999e"),
        first_name="Abigail",
        last_name="Gyebi",
        middle_name='Abena',
        gender=Gender.female,
        roles=[Roles.student]
    )
]

@app.get("/")
async def root():
    return {"Hello: Abigail"}

@app.get("/api/v1/users")
async def fetch_users():
   return db;

@app.post("/api/v1/users")
async def register_user(user: User):
   db.append(user)
   return {"id" : user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user_id == user_id:
            db.remove(user)
            return {"user has been deleted"}
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )


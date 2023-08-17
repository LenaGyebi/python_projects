from typing import List, Optional
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
import uvicorn

from models import Roles, UpdateRequest, AddDetails
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
        middle_name=None,
        gender=Gender.male,
        roles=[Roles.user, Roles.admin],
        address="",
        employer=""
        ),

    User(
        id = UUID("96cb10de-1a12-46fd-b889-cd961d41999e"),
        first_name="Abigail",
        last_name="Gyebi",
        middle_name='Abena',
        gender=Gender.female,
        roles=[Roles.student],
        address="",
        employer=""
    )
]

db: List[AddDetails] = [
    AddDetails(
        employer_name = 'Bost Growth',
        employer_address = 'London street',
        employer_business_start_date = '5th June 2013'
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
   return {"id": user.id}

@app.post("/api/vi/users/{user_id}")
async def add_employer_details(user_id: UUID, AddDetails):
    for user in db:
        if user_id == user.id:


@app.put("/api/v1/users/{user_id}/")
async def update_user(user_id: UUID, update_request: UpdateRequest):
    for user in db:
        if user_id == user.id:
            if update_request.address is not None:
                user.address = update_request.address
            if update_request.employer is not None:
                user.employer = update_request.employer
            return {"message": "User address and employer is updated"}
        if not user:
            raise HTTPException( status_code=404, detail=f"user not found")
    return {"User address and employer has been added"}


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


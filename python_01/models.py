from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"

class Roles(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Roles]
    address: Optional[str]
    employer: Optional[str]


class UpdateRequest(BaseModel):
    address: Optional[str]
    employer: Optional[str]


"""class AddDetails(BaseModel):
    id: UUID = uuid4()
    employer_name: str
    employer_address: str
    employer_business_start_date: str
"""

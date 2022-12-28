from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserSchema(BaseModel):
    id: Optional[int] = None
    username: EmailStr
    email: EmailStr

    class Config:
        orm_mode = True


class UserUpdateSchema(BaseModel):
    username: Optional[EmailStr] = None
    email: Optional[EmailStr] = None

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: EmailStr
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

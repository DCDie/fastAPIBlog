from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserSchema(BaseModel):
    id: Optional[int] = None
    username: EmailStr
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

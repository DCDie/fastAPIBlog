from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

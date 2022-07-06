from fastapi import APIRouter

from apps.users.schemas import UserSchema
from apps.users.models import User

router = APIRouter()


@router.get(path="/", response_model=list[UserSchema])
async def list_users():
    users = await User.objects.all()
    return users


@router.get(path="/{pk}/", response_model=UserSchema)
async def get_user(pk: int):
    user = await User.objects.get(id=pk)
    return user

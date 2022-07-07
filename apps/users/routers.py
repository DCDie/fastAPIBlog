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


@router.post(path="/", response_model=UserSchema, response_model_exclude_unset=True)
async def create_user(user: UserSchema):
    validated_data = user.dict()
    user = await User.objects.create(**validated_data)
    return user


@router.put(path="/{pk}/", response_model=UserSchema, response_model_exclude_unset=True)
async def update_user(pk: int, user: UserSchema):
    instance = await User.objects.get(id=pk)
    validated_data = user.dict()
    user = await instance.update(**validated_data)
    return user


@router.delete(path="/{pk}/", response_model=UserSchema)
async def delete_user(pk: int):
    instance = await User.objects.get(id=pk)
    await instance.delete()
    return instance


@router.patch(path="/{pk}/", response_model=UserSchema, response_model_exclude_unset=True)
async def patch_user(pk: int, user: UserSchema):
    instance = await User.objects.get(id=pk)
    validated_data = user.dict()
    user = await instance.update(**validated_data)
    return user

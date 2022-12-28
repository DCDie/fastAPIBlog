from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from apps.users.models import User
from apps.users.schemas import UserSchema, UserCreateSchema, UserUpdateSchema
from config.settings import async_session

router = APIRouter()


@router.get(path="/", response_model=list[UserSchema], status_code=200)
async def list_users():
    users = await async_session().execute(select(User))
    return users.scalars().all()


@router.get(path="/{pk}/", response_model=UserSchema, status_code=200)
async def get_user(pk: int):
    user = await async_session().execute(select(User).where(User.id == pk))
    if user := user.scalars().first():
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post(path="/", response_model=UserCreateSchema, response_model_exclude_unset=True, status_code=201)
async def create_user(user: UserCreateSchema):
    validated_data = user.dict()
    async with async_session() as session:
        async with session.begin():
            session.add(User(**validated_data))
        await session.commit()
    return validated_data


@router.patch(path="/{pk}/", response_model=UserSchema, response_model_exclude_unset=True)
async def patch_user(pk: int, data: UserUpdateSchema):
    async with async_session() as session:
        async with session.begin():
            user = await session.execute(select(User).where(User.id == pk))
            if user := user.scalars().first():
                for key, value in data.dict(exclude_unset=True).items():
                    setattr(user, key, value)
                session.add(user)
            else:
                raise HTTPException(status_code=404, detail="User not found")
        await session.commit()
    return user


@router.put(path="/{pk}/", response_model=UserSchema, response_model_exclude_unset=True)
async def put_user(pk: int, data: UserUpdateSchema):
    return await patch_user(pk, data)

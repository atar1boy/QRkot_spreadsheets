from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import get_async_session, current_user, current_superuser
from app.crud import charity_project_crud, donation_crud
from app.models import User
from app.schemas import (
    DonationCreate, DonationUserDB, DonationDB
)
from app.services import investing

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возвращает список всех пожертвований.
    """
    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    response_model=list[DonationUserDB],
    dependencies=[Depends(current_user)],
    response_model_exclude_none=True,
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """
    Возвращает список всех пожертвований пользователя.
    """
    return await donation_crud.get_user_donations(user, session)


@router.post(
    '/',
    response_model=DonationUserDB,
    dependencies=[Depends(current_user)],
    response_model_exclude_none=True,
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    new_donation = await donation_crud.create(
        donation, session, user_id=user.id, without_commit=True
    )
    session.add_all(investing(
        new_donation,
        await charity_project_crud.get_not_closed_objs(session)
    ))
    await session.commit()
    await session.refresh(new_donation)
    return new_donation

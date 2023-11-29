from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import get_async_session, current_superuser
from app.crud import charity_project_crud, donation_crud
from app.schemas import (
    CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
)
from app.api.validators import (
    check_project_exists, check_name_duplicate,
    check_project_not_invested, check_full_amount,
    check_project_not_fully_invested
)
from app.services import investing


router = APIRouter()


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    return await charity_project_crud.get_multi(session)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
        project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(project.name, session)
    new_project = await charity_project_crud.create(
        project, session, without_commit=True)
    session.add_all(investing(
        new_project,
        await donation_crud.get_not_closed_objs(session)
    ))
    await session.commit()
    await session.refresh(new_project)
    return new_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_charity_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    project = await check_project_exists(
        project_id, session
    )
    check_project_not_fully_invested(project)
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    if obj_in.full_amount is not None:
        check_full_amount(obj_in.full_amount, project.invested_amount)
    if obj_in.full_amount == project.invested_amount:
        project.fully_invested = True
    return await charity_project_crud.update(
        project, obj_in, session
    )


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    project = await check_project_exists(project_id, session)
    check_project_not_invested(project)
    return await charity_project_crud.remove(project, session)

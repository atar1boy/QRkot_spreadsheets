from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud
from app.models import CharityProject


async def check_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    project = await charity_project_crud.get(charity_project_id, session)
    if project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return project


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


def check_project_not_invested(
        project: CharityProject
) -> None:
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


def check_project_not_fully_invested(
        project: CharityProject
) -> None:
    if project.fully_invested:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )


def check_full_amount(
        obj_in_full_amount: int,
        project_invested_amount: int
) -> None:
    if obj_in_full_amount < project_invested_amount:
        raise HTTPException(
            status_code=422,
            detail='Запрещено устанавливать требуемую сумму меньше внесённой.'
        )

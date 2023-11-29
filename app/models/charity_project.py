from sqlalchemy import Column, String, Text

from app.models import BaseInvestmentFieldsModel


class CharityProject(BaseInvestmentFieldsModel):
    """
    Модель благотворительный проект.
    """
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return super().__repr__() + (
            f'Название проекта: {self.name}'
            f'Описание проекта: {self.description}'
        )

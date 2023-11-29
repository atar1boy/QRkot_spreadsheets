from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, DateTime, CheckConstraint

from app.core.db import Base


class BaseInvestmentFieldsModel(Base):
    """
    Родительский класс для моделей CharityProject и Donation.
    """
    __abstract__ = True
    __table_args__ = (
        CheckConstraint('full_amount > fully_invested'),
        CheckConstraint('fully_invested >= 0'),
    )
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    def __repr__(self):
        return (
            f'Модель: {type(self).__name__}'
            f'Полная сумма: {self.full_amount}'
            f'Количество ивестиций: {self.invested_amount}'
            f'Дата создания: {self.create_date}'
            f'Дата закрытия: {self.close_date}'
        )

from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models import BaseInvestmentFieldsModel


class Donation(BaseInvestmentFieldsModel):
    """
    Модель пожертвований.
    """
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(Text)

    def __repr__(self):
        return super().__repr__() + (
            f'id пользователя: {self.user_id}'
            f'Комментарий: {self.comment} '
        )

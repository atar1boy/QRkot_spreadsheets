from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, Extra


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationUserDB(BaseModel):
    id: int
    comment: Optional[str]
    full_amount: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationUserDB):
    user_id: Optional[int]
    invested_amount: int
    full_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

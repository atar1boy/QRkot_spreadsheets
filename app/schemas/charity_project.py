from datetime import datetime

from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, Extra


class CharityProjectBase(BaseModel):
    name: str = Field(max_length=100)
    description: str

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1
        error_msg_templates = {
            'value_error.any_str.min_length': 'min length:{limit_value}',
        }


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int
    full_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectCreate(CharityProjectBase):
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(max_length=100)
    description: Optional[str]
    full_amount: Optional[PositiveInt]

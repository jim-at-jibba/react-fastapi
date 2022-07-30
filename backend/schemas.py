import datetime as dt

import pydantic


class UserBase(pydantic.BaseModel):
    email: str


class UserCreate(UserBase):
    hashed_password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class LeadBase(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str
    notes: str


class LeadCreate(LeadBase):
    pass


class Lead(LeadBase):
    id: int
    owner_id: int
    date_created: dt.datetime
    date_last_updated: dt.datetime

    class Config:
        orm_mode = True

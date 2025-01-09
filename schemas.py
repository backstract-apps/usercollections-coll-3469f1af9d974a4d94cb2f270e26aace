from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Auth(BaseModel):
    id: int
    password: str
    created_date: datetime.time
    updated_date: datetime.time
    auth_method: str
    status: str


class ReadAuth(BaseModel):
    id: int
    password: str
    created_date: datetime.time
    updated_date: datetime.time
    auth_method: str
    status: str
    class Config:
        from_attributes = True


class BasicDetails(BaseModel):
    id: int
    username: str
    full_name: str
    dob: datetime.date
    dob_time: datetime.time
    created_date: datetime.time
    updated_date: datetime.time
    father_name: str
    mother_name: str
    mobile_number: str


class ReadBasicDetails(BaseModel):
    id: int
    username: str
    full_name: str
    dob: datetime.date
    dob_time: datetime.time
    created_date: datetime.time
    updated_date: datetime.time
    father_name: str
    mother_name: str
    mobile_number: str
    class Config:
        from_attributes = True




class PutAuthId(BaseModel):
    id: str
    password: str
    created_date: str
    updated_date: str
    auth_method: str
    status: str

    class Config:
        from_attributes = True



class PutBasicDetailsId(BaseModel):
    id: str
    username: str
    full_name: str
    dob: str
    dob_time: str
    created_date: str
    updated_date: str
    father_name: str
    mother_name: str
    mobile_number: str

    class Config:
        from_attributes = True


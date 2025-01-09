from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Auth(Base):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True)
    password = Column(String, primary_key=False)
    created_date = Column(Time, primary_key=False)
    updated_date = Column(Time, primary_key=False)
    auth_method = Column(String, primary_key=False)
    status = Column(String, primary_key=False)

class BasicDetails(Base):
    __tablename__ = 'basic_details'
    id = Column(Integer, primary_key=True)
    username = Column(String, primary_key=False)
    full_name = Column(String, primary_key=False)
    dob = Column(Date, primary_key=False)
    dob_time = Column(Time, primary_key=False)
    created_date = Column(Time, primary_key=False)
    updated_date = Column(Time, primary_key=False)
    father_name = Column(String, primary_key=False)
    mother_name = Column(String, primary_key=False)
    mobile_number = Column(String, primary_key=False)


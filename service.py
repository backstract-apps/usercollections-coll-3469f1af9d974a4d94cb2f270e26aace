from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_auth(db: Session):

    auth_all = db.query(models.Auth).order_by(models.Auth.id).all()
    res = {
        'auth_all': auth_all,
    }
    return res

async def get_auth_id(db: Session, id: int):

    auth_one = db.query(models.Auth).filter(models.Auth.id == 'id').first()
    res = {
        'auth_one': auth_one,
    }
    return res

async def post_auth(db: Session, id: int, password: str, created_date: str, updated_date: str, auth_method: str, status: str):

    record_to_be_added = {'id': id, 'password': password, 'created_date': created_date, 'updated_date': updated_date, 'auth_method': auth_method, 'status': status}
    new_auth = models.Auth(**record_to_be_added)
    db.add(new_auth)
    db.commit()
    db.refresh(new_auth)
    auth_inserted_record = new_auth


    users_records1 = []  # Creating new list



# Add element to the list 'users_records1'
    users_records1.insert(0, id)


    # Get element at index 1 from the list 'users_records1'
    id = users_records1[1]


   # Remove element(s) from the list 'users_records1'
    users_records1.pop(0)  # Remove from the front


    user_records2 = []  # Creating new list



# Add element to the list 'user_records2'
    user_records2.insert(0, id)


    user_shivam = {}  # Creating new dict



    user_records2 = list(user_shivam.keys())

    

    users_records3: list[int] = []
    res = {
        'auth_inserted_record': auth_inserted_record,
        'shivam': id,
    }
    return res

async def put_auth_id(db: Session, raw_data: schemas.PutAuthId):
    id:str = raw_data.id
    password:str = raw_data.password
    created_date:str = raw_data.created_date
    updated_date:str = raw_data.updated_date
    auth_method:str = raw_data.auth_method
    status:str = raw_data.status


    auth_edited_record = db.query(models.Auth).filter(models.Auth.id == id).first()
    for key, value in {'id': id, 'password': password, 'created_date': created_date, 'updated_date': updated_date, 'auth_method': auth_method, 'status': status}.items():
          setattr(auth_edited_record, key, value)
    db.commit()
    db.refresh(auth_edited_record)
    auth_edited_record = auth_edited_record

    res = {
        'auth_edited_record': auth_edited_record,
    }
    return res

async def delete_auth_id(db: Session, id: int):

    auth_deleted = None
    record_to_delete = db.query(models.Auth).filter(models.Auth.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        auth_deleted = record_to_delete
    res = {
        'auth_deleted': auth_deleted,
    }
    return res

async def get_basic_details(db: Session):

    basic_details_all = db.query(models.Basic_details).order_by(models.Basic_details.id).all()
    res = {
        'basic_details_all': basic_details_all,
    }
    return res

async def get_basic_details_id(db: Session, id: int):

    basic_details_one = db.query(models.Basic_details).filter(models.Basic_details.id == 'id').first()
    res = {
        'basic_details_one': basic_details_one,
    }
    return res

async def post_basic_details(db: Session, id: int, username: str, full_name: str, dob: str, dob_time: str, created_date: str, updated_date: str, father_name: str, mother_name: str, mobile_number: str):

    record_to_be_added = {'id': id, 'username': username, 'full_name': full_name, 'dob': dob, 'dob_time': dob_time, 'created_date': created_date, 'updated_date': updated_date, 'father_name': father_name, 'mother_name': mother_name, 'mobile_number': mobile_number}
    new_basic_details = models.Basic_details(**record_to_be_added)
    db.add(new_basic_details)
    db.commit()
    db.refresh(new_basic_details)
    basic_details_inserted_record = new_basic_details


    user_name1 = []  # Creating new list



    user_dob = {}  # Creating new dict



# Add element to the list 'user_name1'
    user_name1.insert(0, basic_details_inserted_record.username)


    user_dob['1'] = 'basic_details_inserted_record.username'


    user_dob['1'] = 'dob'


    dob = user_dob.get('1')


    user_name1 = list(user_dob.keys())

    # dfgdf
    del user_dob['1']
    res = {
        'basic_details_inserted_record': basic_details_inserted_record,
        'shivam': basic_details_inserted_record,
    }
    return res

async def put_basic_details_id(db: Session, raw_data: schemas.PutBasicDetailsId):
    id:str = raw_data.id
    username:str = raw_data.username
    full_name:str = raw_data.full_name
    dob:str = raw_data.dob
    dob_time:str = raw_data.dob_time
    created_date:str = raw_data.created_date
    updated_date:str = raw_data.updated_date
    father_name:str = raw_data.father_name
    mother_name:str = raw_data.mother_name
    mobile_number:str = raw_data.mobile_number


    basic_details_edited_record = db.query(models.Basic_details).filter(models.Basic_details.id == id).first()
    for key, value in {'id': id, 'username': username, 'full_name': full_name, 'dob': dob, 'dob_time': dob_time, 'created_date': created_date, 'updated_date': updated_date, 'father_name': father_name, 'mother_name': mother_name, 'mobile_number': mobile_number}.items():
          setattr(basic_details_edited_record, key, value)
    db.commit()
    db.refresh(basic_details_edited_record)
    basic_details_edited_record = basic_details_edited_record

    res = {
        'basic_details_edited_record': basic_details_edited_record,
    }
    return res

async def delete_basic_details_id(db: Session, id: int):

    basic_details_deleted = None
    record_to_delete = db.query(models.Basic_details).filter(models.Basic_details.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        basic_details_deleted = record_to_delete
    res = {
        'basic_details_deleted': basic_details_deleted,
    }
    return res


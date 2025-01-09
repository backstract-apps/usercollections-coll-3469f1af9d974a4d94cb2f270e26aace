from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/auth/')
async def get_auth(db: Session = Depends(get_db)):
    try:
        return await service.get_auth(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/auth/id')
async def get_auth_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_auth_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/auth/')
async def post_auth(id: int, password: str, created_date: str, updated_date: str, auth_method: str, status: str, db: Session = Depends(get_db)):
    try:
        return await service.post_auth(db, id, password, created_date, updated_date, auth_method, status)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/auth/id/')
async def put_auth_id(raw_data: schemas.PutAuthId, db: Session = Depends(get_db)):
    try:
        return await service.put_auth_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/auth/id')
async def delete_auth_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_auth_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/basic_details/')
async def get_basic_details(db: Session = Depends(get_db)):
    try:
        return await service.get_basic_details(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/basic_details/id')
async def get_basic_details_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_basic_details_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/basic_details/')
async def post_basic_details(id: int, username: str, full_name: str, dob: str, dob_time: str, created_date: str, updated_date: str, father_name: str, mother_name: str, mobile_number: str, db: Session = Depends(get_db)):
    try:
        return await service.post_basic_details(db, id, username, full_name, dob, dob_time, created_date, updated_date, father_name, mother_name, mobile_number)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/basic_details/id/')
async def put_basic_details_id(raw_data: schemas.PutBasicDetailsId, db: Session = Depends(get_db)):
    try:
        return await service.put_basic_details_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/basic_details/id')
async def delete_basic_details_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_basic_details_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))


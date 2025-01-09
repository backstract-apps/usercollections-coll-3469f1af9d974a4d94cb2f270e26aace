from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - usercollections-coll-3469f1af9d974a4d94cb2f270e26aace',debug=False,docs_url='/silly-aryan-195b6d40ccc511efab8d0242ac12000466/docs',openapi_url='/silly-aryan-195b6d40ccc511efab8d0242ac12000466/openapi.json')

app.include_router(router, prefix='/silly-aryan-195b6d40ccc511efab8d0242ac12000466/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()
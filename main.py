from fastapi import FastAPI
from routers.houses import router as house_router
from database import Base, engine
from routers.users import router as users_router
app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(house_router)
@app.get("/")
def home():
    return {"message": "API works"}
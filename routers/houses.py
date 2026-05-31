from http.client import HTTPException

from docutils.nodes import address
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database import get_db
from models import house
from models.house import House
from models.user import User
from schemas.house import HouseCreate

router = APIRouter(prefix="/houses", tags=["Houses"])
@router.post("/")
def create_house(house:HouseCreate,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==house.user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
new_house=House(
    name = house.name,
    address=house.address,
    user_id=house.user_id
)
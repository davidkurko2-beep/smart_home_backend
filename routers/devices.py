from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.device import Device
from models.house import House
from models.room import Room
from schemas.device import DeviceCreate

router = APIRouter(prefix="/devices", tags=["Devices"])
@router.post("/")
def create_device(device:DeviceCreate, db:Session=Depends(get_db)):
    house = db.query(House).filter(House.id==device.house_id).first()
    if house is None:
        raise HTTPException(status_code=404, detail="House not found")
    room = db.query(Room).filter(Room.id == device.room_id).first()
    if room is None:
        raise HTTPException(status_code=404, detail="House not found")
    new_device = Device (name = device.name,
                         type=device.type,
                         house_id=device.house_id,
                         room_id=device.room_id)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device
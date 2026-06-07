from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.house import House
from models.room import Room
from schemas.house import HouseUpdate
from schemas.room import RoomUpdate, RoomCreate

router = APIRouter(prefix="/rooms", tags=["Rooms"])
@router.post("/")
def create_room(room: RoomCreate,db:Session=Depends(get_db)):
    user=db.query(House).filter(House.id==room.house_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    new_room=House(
        name = room.name,
        user_id=room.user_id)
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

@router.get("/")
def get_rooms(db:Session=Depends(get_db)):
    rooms = db.query(House).all()
    return rooms
@router.get("/{room_id}")
def get_room(room_id: int, db:Session=Depends(get_db)):
    room = db.query(Room).filter(Room.id==room_id).first()
    if room is None:
        raise HTTPException(status_code=404, detail="House not found")
    return room

@router.put("/{room_id}")
def update_room(room_id: int, room_data: RoomUpdate, db:Session=Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if room is None:
        raise HTTPException(status_code=404, detail = "House not found")
    room.name = room_data.name
    room.address = room_data.addres
    db.commit()
    db.refresh(room)
    return room
@router.delete("/{room_id}")
def delete_room(room_id:int, db:Session=Depends(get_db)):
    room=db.query(Room).filter(Room.id == room_id).first()
    if room is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(room)
    db.commit()
    return {"message": "Room Deleted"}
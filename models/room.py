from sqlalchemy import Column, Integer, ForeignKey, String

from database import Base


class Room(Base):
    __tablename__ = "rooms"
    id = Column (Integer, primary_key=True)
    name = Column(String)
    house_id=Column(Integer, ForeignKey("houses.id"))

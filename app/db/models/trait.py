from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Trait(Base):
    __tablename__ = "traits"

    trait_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    cost = Column(Integer)
    type = Column(String)

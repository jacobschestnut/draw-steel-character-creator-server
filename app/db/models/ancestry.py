from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Ancestry(Base):
    __tablename__ = "ancestries"

    ancestry_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    height_feet_start = Column(Integer)
    height_feet_end = Column(Integer)
    height_inch_start = Column(Integer)
    height_inch_end = Column(Integer)
    weight_lbs_start = Column(Integer)
    weight_lbs_end = Column(Integer)
    life_exp_start = Column(Integer)
    life_exp_end = Column(Integer)
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Skill(Base):
    __tablename__ = "skills"

    skill_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    skill_group_id = Column(Integer, ForeignKey('skill_groups.skill_group_id'), primary_key=True)

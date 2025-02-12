from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class SkillGroup(Base):
    __tablename__ = "skill_groups"

    skill_group_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

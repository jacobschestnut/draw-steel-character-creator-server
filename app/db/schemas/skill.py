from pydantic import BaseModel
from typing import Optional

class SkillCreate(BaseModel):
    name: str
    skill_group_id: int

    class Config:
        orm_mode = True

class Skill(SkillCreate):
    skill_id: int

    class Config:
        orm_mode = True

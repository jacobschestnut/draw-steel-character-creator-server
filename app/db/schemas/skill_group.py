from pydantic import BaseModel

class SkillGroupCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class SkillGroup(SkillGroupCreate):
    skill_group_id: int

    class Config:
        orm_mode = True

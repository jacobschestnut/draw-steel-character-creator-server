from sqlalchemy.orm import Session
from ..models import Skill, SkillGroup
from ..schemas import SkillCreate

def create_skill(db: Session, skill: SkillCreate):
    db_skill = Skill(
        name=skill.name,
        skill_group_id=skill.skill_group_id
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def get_skills(db: Session):
    return db.query(Skill).all()

def get_skills_by_skill_group(db: Session, skill_group_id: int):
    return db.query(Skill).join(SkillGroup).filter(SkillGroup.skill_group_id == skill_group_id).all()

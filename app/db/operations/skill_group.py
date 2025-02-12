from sqlalchemy.orm import Session
from ..models import SkillGroup
from ..schemas import SkillGroupCreate

def create_skill_group(db: Session, skill_group: SkillGroupCreate):
    db_skill_group = SkillGroup(
        name=skill_group.name,
    )
    db.add(db_skill_group)
    db.commit()
    db.refresh(db_skill_group)
    return db_skill_group

def get_skill_groups(db: Session):
    return db.query(SkillGroup).all()
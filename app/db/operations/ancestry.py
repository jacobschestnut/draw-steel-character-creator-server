from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import Ancestry, AncestryTrait, Trait
from app.db.schemas import AncestryCreate

def get_ancestries(db: Session):
    return db.query(Ancestry).all()

def create_ancestry(db: Session, ancestry: AncestryCreate) -> Ancestry:
    db_ancestry = Ancestry(
        name=ancestry.name,
        height_feet_start=ancestry.height_feet_start,
        height_feet_end=ancestry.height_feet_end,
        height_inch_start=ancestry.height_inch_start,
        height_inch_end=ancestry.height_inch_end,
        weight_lbs_start=ancestry.weight_lbs_start,
        weight_lbs_end=ancestry.weight_lbs_end,
        life_exp_start=ancestry.life_exp_start,
        life_exp_end=ancestry.life_exp_end,
    )
    db.add(db_ancestry)
    db.commit()
    db.refresh(db_ancestry)
    return db_ancestry

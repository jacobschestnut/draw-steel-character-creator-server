from sqlalchemy.orm import Session
from ..models import Trait, AncestryTrait
from ..schemas import TraitCreate

def create_trait(db: Session, trait: TraitCreate):
    db_trait = Trait(
        name=trait.name,
        description=trait.description,
        cost=trait.cost,
        type=trait.type
    )
    db.add(db_trait)
    db.commit()
    db.refresh(db_trait)
    return db_trait

def get_traits(db: Session):
    return db.query(Trait).all()

def get_traits_by_ancestry(db: Session, ancestry_id: int):
    return db.query(Trait).join(AncestryTrait).filter(AncestryTrait.ancestry_id == ancestry_id).all()

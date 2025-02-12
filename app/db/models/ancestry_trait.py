from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base

class AncestryTrait(Base):
    __tablename__ = 'ancestry_traits'

    ancestry_id = Column(Integer, ForeignKey('ancestries.ancestry_id'), primary_key=True)
    trait_id = Column(Integer, ForeignKey('traits.trait_id'), primary_key=True)

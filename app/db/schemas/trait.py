from pydantic import BaseModel

class TraitCreate(BaseModel):
    name: str
    description: str
    cost: int
    type: str

    class Config:
        orm_mode = True

class Trait(TraitCreate):
    trait_id: int

    class Config:
        orm_mode = True

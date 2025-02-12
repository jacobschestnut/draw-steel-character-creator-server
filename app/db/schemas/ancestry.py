from pydantic import BaseModel

class AncestryBase(BaseModel):
    name: str
    height_feet_start: int
    height_feet_end: int
    height_inch_start: int
    height_inch_end: int
    weight_lbs_start: int
    weight_lbs_end: int
    life_exp_start: int
    life_exp_end: int

class AncestryCreate(AncestryBase):
    pass

class Ancestry(AncestryBase):
    ancestry_id: int

    class Config:
        orm_mode = True
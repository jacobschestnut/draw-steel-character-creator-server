from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from .db import operations, models, schemas
from .db.database import SessionLocal, engine, Base
from .db.models import Ancestry, Trait, AncestryTrait

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/ancestries/", response_model=schemas.Ancestry)
def create_ancestry(ancestry: schemas.AncestryCreate, db: Session = Depends(get_db)):
    return operations.create_ancestry(db=db, ancestry=ancestry)

@app.post("/traits/", response_model=schemas.Trait)
def create_trait(trait: schemas.TraitCreate, db: Session = Depends(get_db)):
    return operations.create_trait(db=db, trait=trait)

@app.get("/ancestries/", response_model=List[schemas.Ancestry])
def get_ancestries(db: Session = Depends(get_db)):
    ancestries = operations.get_ancestries(db)
    if not ancestries:
        raise HTTPException(status_code=404, detail="No ancestries found")
    return ancestries
    
@app.get("/traits/", response_model=List[schemas.Trait])
def get_traits(db: Session = Depends(get_db)):
    traits = operations.get_traits(db)
    if not traits:
        raise HTTPException(status_code=404, detail="No traits found")
    return traits

@app.get("/ancestries/{ancestry_id}/traits/", response_model=List[schemas.Trait])
def get_traits_for_ancestry(ancestry_id: int, db: Session = Depends(get_db)):
    traits = operations.get_traits_by_ancestry(db, ancestry_id)
    if not traits:
        raise HTTPException(status_code=404, detail="No traits found for this ancestry")
    return traits

@app.get("/skills/", response_model=List[schemas.Skill])
def get_skills(db: Session = Depends(get_db)):
    skills = operations.get_skills(db)
    if not skills:
        raise HTTPException(status_code=404, detail="No skills found")
    return skills

@app.get("/skillgroup/{skill_group_id}/skills/", response_model=List[schemas.Skill])
def get_skills_for_skill_group(skill_group_id: int, db: Session = Depends(get_db)):
    skills = operations.get_skills_by_skill_group(db, skill_group_id)
    if not skills:
        raise HTTPException(status_code=404, detail="No skills found for this skill group")
    return skills

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import list as models
from app.schemas import list as schemas

router = APIRouter(prefix="/lists", tags=["Lists"])

@router.post("/", response_model=schemas.ListResponse)
def create_list(list_data: schemas.ListCreate, db: Session = Depends(get_db)):
    new_list = models.List(**list_data.dict())
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list

@router.get("/{list_id}", response_model=schemas.ListResponse)
def read_list(list_id: int, db: Session = Depends(get_db)):
    list_obj = db.query(models.List).filter(models.List.id == list_id).first()
    if not list_obj:
        raise HTTPException(status_code=404, detail="List not found")
    return list_obj

@router.put("/{list_id}", response_model=schemas.ListResponse)
def update_list(list_id: int, list_update: schemas.ListUpdate, db: Session = Depends(get_db)):
    list_obj = db.query(models.List).filter(models.List.id == list_id).first()
    if not list_obj:
        raise HTTPException(status_code=404, detail="List not found")
    for key, value in list_update.dict(exclude_unset=True).items():
        setattr(list_obj, key, value)
    db.commit()
    db.refresh(list_obj)
    return list_obj

@router.delete("/{list_id}")
def delete_list(list_id: int, db: Session = Depends(get_db)):
    list_obj = db.query(models.List).filter(models.List.id == list_id).first()
    if not list_obj:
        raise HTTPException(status_code=404, detail="List not found")
    db.delete(list_obj)
    db.commit()
    return {"detail": "List deleted successfully"}

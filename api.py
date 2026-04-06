from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import 
from database import Base, get_db, engine
from models import 


Base.metadata.create_all(bind=engine)
api_router = APIRouter(prefix='/api/res')


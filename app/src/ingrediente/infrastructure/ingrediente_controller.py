from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.src.common.infrastructure.modelos_pydantic import *
from .repository.ingrediente_repositorio import IngredienteRepositorio
from ...common.infrastructure.modelos_pydantic_entrada import IngredienteEntryModel
from typing import Annotated
from sqlalchemy.orm import Session
from ...common.infrastructure.sqlalchemy_session import get_db

router = APIRouter(
    prefix='/ingredientes',
    tags=['ingredientes']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

db_dependency = Annotated[Session, Depends(get_db)]

@router.patch("/", response_model=IngredienteModel)
@as_pydantic_model
async def get_ingredient(db: db_dependency, ingredienteData: IngredienteEntryModel, token: str = Depends(oauth2_scheme)):
    ingrediente_repo = IngredienteRepositorio(db)
    nuevoIngrediente = ingrediente_repo.insertar(ingredienteData)
    return nuevoIngrediente
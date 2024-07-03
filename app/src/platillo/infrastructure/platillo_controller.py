from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.src.common.infrastructure.modelos_pydantic import *
from .repository.platillo_repositorio import PlatilloRepositorio
from ...common.infrastructure.modelos_pydantic_entrada import PlatilloEntryModel
from typing import Annotated
from sqlalchemy.orm import Session
from ...common.infrastructure.sqlalchemy_session import get_db

router = APIRouter(
    prefix='/platillos',
    tags=['platillos']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

db_dependency = Annotated[Session, Depends(get_db)]

@router.patch("/", response_model=PlatilloModel)
@as_pydantic_model
async def get_ingredient(db: db_dependency, platilloData: PlatilloEntryModel, token: str = Depends(oauth2_scheme)):
    platillo_repo = PlatilloRepositorio(db)
    nuevoPlatillo = platillo_repo.insertar(platilloData)
    return nuevoPlatillo
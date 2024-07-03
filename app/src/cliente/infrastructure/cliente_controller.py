from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.src.common.infrastructure.modelos_pydantic import *
from .repository.cliente_repositorio import ClienteRepositorio
from ...common.infrastructure.modelos_pydantic_entrada import ClienteEntryModel
from typing import Annotated
from sqlalchemy.orm import Session
from ...common.infrastructure.sqlalchemy_session import get_db
from ...common.infrastructure.auth import get_current_user

router = APIRouter(
    prefix='/clientes',
    tags=['clientes']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

db_dependency = Annotated[Session, Depends(get_db)]

@router.patch("/", response_model=ClienteModel)
@as_pydantic_model
async def get_ingredient(db: db_dependency, clienteData: ClienteEntryModel, token: str = Depends(oauth2_scheme), current_user=Depends(get_current_user)):
    print(current_user)
    cliente_repo = ClienteRepositorio(db)
    nuevoCliente = cliente_repo.insertar(clienteData, current_user)
    return nuevoCliente
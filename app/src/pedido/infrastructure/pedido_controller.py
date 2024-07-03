from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.src.common.infrastructure.modelos_pydantic import *
from .repository.pedido_repositorio import PedidoRepositorio
from ...common.infrastructure.modelos_pydantic_entrada import PedidoEntryModel
from typing import Annotated
from sqlalchemy.orm import Session
from ...common.infrastructure.sqlalchemy_session import get_db
from ...common.infrastructure.auth import get_current_user

router = APIRouter(
    prefix='/pedidos',
    tags=['pedidos']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

db_dependency = Annotated[Session, Depends(get_db)]

@router.patch("/", response_model=PedidoModel)
@as_pydantic_model
async def get_ingredient(db: db_dependency, pedidoData: PedidoEntryModel,
                          token: str = Depends(oauth2_scheme),
                            current_user=Depends(get_current_user)):
    print(current_user)
    pedido_repo = PedidoRepositorio(db)
    nuevoPedido = pedido_repo.insertar(pedidoData, current_user)
    return nuevoPedido
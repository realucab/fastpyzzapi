from fastapi import FastAPI, HTTPException
from starlette import status
from app.api.routes import router
from app.src.common.infrastructure.sqlalchemy_engine import engine
from app.src.common.infrastructure.sqlalchemy_base import Base
from app.src.ingrediente.infrastructure.mapper.ingrediente_orm_mapper import IngredienteOrm
from app.src.platillo.infrastructure.mapper.platillo_orm_mapper import PlatilloOrm
from app.src.platillo.infrastructure.mapper.platillo_ingrediente_association import platillo_ingrediente
from app.src.cliente.infrastructure.mapper.cliente_orm_mapper import ClienteOrm
from app.src.pedido.infrastructure.mapper.pedido_orm_mapper import PedidoOrm
from app.src.pedido.infrastructure.mapper.pedido_platillo_association import pedido_platillo
from app.src.common.infrastructure.auth import router as auth_router, db_dependency, user_dependency
from app.src.ingrediente.infrastructure.ingrediente_controller import router as ingredientes_router
from app.src.platillo.infrastructure.platillo_controller import router as platillos_router
from app.src.cliente.infrastructure.cliente_controller import router as clientes_router

Base.metadata.create_all(bind=engine)

def get_application():
    app = FastAPI(
        title="fastpyzzapi",
        version="1.0.0"
    )
    app.include_router(router)
    app.include_router(auth_router)
    app.include_router(ingredientes_router)
    app.include_router(platillos_router)
    app.include_router(clientes_router)
    return app

app = get_application()

@app.get("/", status_code=status.HTTP_200_OK)
async def user (user: user_dependency, db: db_dependency):
    print(user)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    return {"User": user}
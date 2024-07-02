from fastapi import FastAPI, HTTPException
from starlette import status
from app.api.routes import router
from app.src.common.infrastructure.sqlalchemy_engine import engine
from app.src.common.infrastructure.sqlalchemy_session import SessionLocal
from app.src.common.infrastructure.sqlalchemy_base import Base
from app.src.ingrediente.infrastructure.mapper.ingrediente_orm_mapper import IngredienteOrm
# from app.src.almacen.infrastructure.almacen_orm_mapper import AlmacenOrm
from app.src.platillo.infrastructure.mapper.platillo_orm_mapper import PlatilloOrm
from app.src.platillo.infrastructure.mapper.platillo_ingrediente_association import platillo_ingrediente
from app.src.cliente.infrastructure.mapper.cliente_orm_mapper import ClienteOrm
from app.src.pedido.infrastructure.mapper.pedido_orm_mapper import PedidoOrm
from app.src.pedido.infrastructure.mapper.pedido_platillo_association import pedido_platillo
from app.src.common.infrastructure.auth import auth, db_dependency, user_dependency

Base.metadata.create_all(bind=engine)

def get_application():
    app = FastAPI(
        title="Aplicación Demo de DDD",
        version="1.0.0"
    )

    app.include_router(router)
    app.include_router(auth.router)
    return app

app = get_application()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", status_code=status.HTTP_200_OK)
async def user (user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    return {"User": user}
from fastapi import FastAPI

from app.api.routes import router
from app.src.common.infrastructure.sqlalchemy_engine import engine
from app.src.common.infrastructure.sqlalchemy_base import Base
from app.src.ingrediente.infrastructure.mapper.ingrediente_orm_mapper import Ingrediente

Base.metadata.create_all(bind=engine)

def get_application():
    app = FastAPI(
        title="Aplicación Demo de DDD",
        version="1.0.0"
    )

    app.include_router(router)
    return app

app = get_application()
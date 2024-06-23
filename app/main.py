from fastapi import FastAPI

from app.api.routes import router
from app.infrastructure.database import engine
from app.infrastructure.orm import Base


Base.metadata.create_all(bind=engine)

def get_application():
    app = FastAPI(
        title="Aplicación Demo de DDD",
        version="1.0.0"
    )

    app.include_router(router)
    return app


app = get_application()
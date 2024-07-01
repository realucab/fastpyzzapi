from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from app.src.common.infrastructure.sqlalchemy_base import Base

class Ingrediente(Base):
    __tablename__ = 'ingrediente'

    id_ingrediente = Column(UUID(as_uuid=True), primary_key=True)
    nombre_ingrediente = Column(String(50))
    cantidad_ingrediente = Column(Float)
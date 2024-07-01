from sqlalchemy import Column, Float, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.src.common.infrastructure.sqlalchemy_base import Base

class AlmacenOrm(Base):

    # Tabla:
    __tablename__ = 'almacen'

    # Columnas:
    id_almacen = Column(UUID(as_uuid=True), primary_key=True)
    capacidad_maxima = Column(Float, CheckConstraint('capacidad_maxima >= 0'), nullable=False)
    
    # Relaciones:
    ingredientes = relationship('IngredienteOrm', back_populates='almacen')

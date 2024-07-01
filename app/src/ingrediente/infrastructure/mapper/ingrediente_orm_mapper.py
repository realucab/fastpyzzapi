from sqlalchemy import Column, String, Float, CheckConstraint#, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.src.common.infrastructure.sqlalchemy_base import Base
from ....platillo.infrastructure.mapper.platillo_ingrediente_association import platillo_ingrediente

class IngredienteOrm(Base):

    # Tabla:
    __tablename__ = 'ingrediente'

    # Columnas:
    id_ingrediente = Column(UUID(as_uuid=True), primary_key=True)
    nombre_ingrediente = Column(String(50), nullable=False, unique=True)
    cantidad_ingrediente = Column(Float, CheckConstraint('cantidad_ingrediente >= 0'), nullable=False)
    # almacen_id = Column(UUID(as_uuid=True), ForeignKey('almacen.id'))

    # Relaciones:
    platillos = relationship('PlatilloOrm', secondary=platillo_ingrediente, back_populates='ingredientes')
    # almacen = relationship('AlmacenOrm', back_populates='ingredientes')
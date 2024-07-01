from sqlalchemy import Column, String, Integer, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.src.common.infrastructure.sqlalchemy_base import Base

class ClienteOrm(Base):

    # Tabla:
    __tablename__ = 'cliente'

    # Columnas:
    id_cliente = Column(UUID(as_uuid=True), primary_key=True)
    nombre_cliente = Column(String(100), nullable=False)
    numero_cedula = Column(Integer, CheckConstraint('numero_cedula >= 0'), nullable=False, unique=True)
    email_cliente = Column(String(50), nullable=False, unique=True)
    numero_telefono = Column(Integer, CheckConstraint('numero_telefono >= 0'))
    
    # Relaciones:
    pedidos = relationship('PedidoOrm', back_populates='clientes')
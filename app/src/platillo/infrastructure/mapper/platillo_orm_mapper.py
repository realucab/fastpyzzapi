from sqlalchemy import Column, String, Float, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.src.common.infrastructure.sqlalchemy_base import Base
from sqlalchemy import Enum
from ...domain.value_objects.tipo_platillo import TipoPlatillo
from .platillo_ingrediente_association import platillo_ingrediente

class PlatilloOrm(Base):

    # Tabla:
    __tablename__ = 'platillo'

    # Columnas:
    id_platillo = Column(UUID(as_uuid=True), primary_key=True)
    nombre_platillo = Column(String(50), nullable=False, unique=True)
    precio_platillo = Column(Float, CheckConstraint('precio_platillo >= 0'), nullable=False)
    descripcion_platillo = Column(String(500), unique=True)
    tipo_platillo = Column(Enum(TipoPlatillo), nullable=False)

    # Relaciones:
    ingredientes = relationship('IngredienteOrm', secondary=platillo_ingrediente, back_populates='platillos')
    pedidos = relationship('PedidoOrm', secondary='pedido_platillo', back_populates='platillos')
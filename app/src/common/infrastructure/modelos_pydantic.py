from pydantic import BaseModel
from uuid import UUID
from typing import List
from functools import wraps
from datetime import datetime

'''def as_pydantic_model(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if isinstance(result, list):
            # Get the Pydantic model class based on the class name of the first domain object in the list
            pydantic_model = globals()[result[0].__class__.__name__ + "Model"]
            # Convert each domain object in the list to a dictionary, then to a Pydantic model
            return [pydantic_model(**item.to_dict()) for item in result]
        else:
            # Get the Pydantic model class based on the class name of the domain object
            pydantic_model = globals()[result.__class__.__name__ + "Model"]
            # Convert the domain object to a dictionary, then to a Pydantic model
            return pydantic_model(**result.to_dict())
    return wrapper'''

def as_pydantic_model(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        # Get the Pydantic model class based on the class name of the domain object
        pydantic_model = globals()[result.__class__.__name__ + "Model"]
        # Convert the domain object to a dictionary
        data = result.to_dict()
        # Convert the dictionary to a Pydantic model
        return pydantic_model(**data)
    return wrapper

class IngredienteModel(BaseModel):
    idIngrediente: UUID
    nombreIngrediente: str
    cantidadIngrediente: float
    eventos: List[str]

class AlmacenModel(BaseModel):
    capacidadMaxima: float
    ingredientesAlmacen: List[str]

class ClienteModel(BaseModel):
    idCliente: UUID
    nombreCliente: str
    numeroCedula: int
    emailCliente: str
    numeroTelefono: int

class PlatilloModel(BaseModel):
    idPlatillo: UUID
    nombrePlatillo: str
    precioPlatillo: float
    descripcionPlatillo: str
    tipoPlatillo: str
    ingredientesPlatillo: List[str]

class PedidoModel(BaseModel):
    idPedido: UUID
    idCliente: UUID
    platillos: List[str]
    estadoPedido: str
    totalPedido: float
    eventos: List[str]
    fechaPedido: datetime

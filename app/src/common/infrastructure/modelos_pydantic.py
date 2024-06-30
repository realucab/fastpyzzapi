from pydantic import BaseModel
from uuid import UUID
from typing import List
from functools import wraps

'''def as_pydantic_model(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        # Get the Pydantic model class based on the class name of the domain object
        pydantic_model = globals()[result.__class__.__name__ + "Model"]
        # Convert the domain object to a Pydantic model
        # Remove the leading underscore from attribute names
        data = {k.lstrip('_'): v.dict() if hasattr(v, 'dict') else v for k, v in result.__dict__.items()}
        return pydantic_model(**data)
    return wrapper

def as_pydantic_model(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        # Get the Pydantic model class based on the class name of the domain object
        pydantic_model = globals()[result.__class__.__name__ + "Model"]
        # Convert the domain object to a Pydantic model
        return pydantic_model(**result.__dict__)
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

class AlmacenModel(BaseModel):
    capacidadMaxima: float
    ingredientesAlmacen: List[str]

class ClienteModel(BaseModel):
    idCliente: UUID
    nombreCliente: str
    numeroCedula: int
    emailCliente: str
    numeroTelefono: int

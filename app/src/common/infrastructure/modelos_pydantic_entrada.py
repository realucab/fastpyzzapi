from pydantic import BaseModel, Field

class IngredienteEntryModel(BaseModel):
    nombre_ingrediente: str = Field(..., example="Tomate")
    cantidad_ingrediente: float = Field(..., example=10.5)

class PlatilloEntryModel(BaseModel):
    nombre_platillo: str = Field(..., example="Pizza margarita")
    precio_platillo: float = Field(..., example=10.5)
    descripcion_platillo: str = Field(..., example="Pizza de queso")
    tipo_platillo: str = Field(..., example="PIZZA")
    ingredientes_platillo: list[str] = Field(..., example=["e74562d3-8f20-46a6-b565-4fa2c610e63f",
                                                           "6ce504c3-f9ac-4e01-a328-201a2e1b00d7"])
    
class ClienteEntryModel(BaseModel):
    nombre_cliente: str = Field(..., example="Kvothe")
    numero_cedula: int = Field(..., example=39000555)
    email_cliente: str = Field(..., example="estudiante@est.ucab.edu.ve")
    numero_telefono: int = Field(..., example=4149997777)
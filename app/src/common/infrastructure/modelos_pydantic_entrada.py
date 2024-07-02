from pydantic import BaseModel, Field

class IngredienteEntryModel(BaseModel):
    nombre_ingrediente: str = Field(..., example="tomate")
    cantidad_ingrediente: float = Field(..., example=10.5)
from pydantic import BaseModel
from uuid import UUID4

class IdCliente(BaseModel):
    _id: UUID4
    
    def __init__(self, id: UUID4):
        self._id = id
    
    @property
    def name(self):
        return self._id
    
    @staticmethod
    def create(id):
        return IdCliente(id)
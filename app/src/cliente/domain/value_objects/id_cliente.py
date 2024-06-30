from uuid import UUID

class IdCliente:
    
    def __init__(self, id: UUID):
        self._id = id
    
    @property
    def id(self):
        return self._id
    
    @staticmethod
    def create(id: UUID):
        return IdCliente(id=id)
from uuid import UUID

class IdPlatillo:

    def __init__(self, id: UUID):
        self._id = id

    @property
    def id(self) -> UUID:
        return self._id
    
    @staticmethod
    def create(id: UUID) -> 'IdPlatillo':
        return IdPlatillo(id=id)
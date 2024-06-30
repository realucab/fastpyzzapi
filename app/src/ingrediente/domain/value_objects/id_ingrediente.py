from uuid import UUID

class IdIngrediente:

    def __init__(self, id: UUID):
        self._id = id

    @property
    def id(self):
        return self._id

    @staticmethod
    def create(id: UUID):
        return IdIngrediente(id=id)

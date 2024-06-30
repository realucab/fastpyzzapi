class PrecioPlatillo:
    def __init__(self, precio: float):
        self._precio = precio

    @property
    def precio(self) -> float:
        return self._precio

    @staticmethod
    def create(precio: float) -> 'PrecioPlatillo':
        return PrecioPlatillo(precio=precio)
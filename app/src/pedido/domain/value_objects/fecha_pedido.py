from datetime import datetime

class FechaPedido:
    def __init__(self, fecha: datetime):
        self._fecha = fecha

    @property
    def fecha(self) -> datetime:
        return self._fecha
    
    @staticmethod
    def create(fecha: datetime) -> 'FechaPedido':
        return FechaPedido(fecha=fecha)
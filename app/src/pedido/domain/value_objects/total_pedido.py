class TotalPedido:
    
    def __init__(self, total: float):
        self._total = total

    @property
    def value(self) -> float:
        return self._total
    
    @staticmethod
    def create(total: float) -> 'TotalPedido':
        return TotalPedido(total=total)
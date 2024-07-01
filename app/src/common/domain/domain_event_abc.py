from abc import ABC, abstractmethod
from uuid import UUID
from datetime import datetime

class DomainEvent(ABC):

    @abstractmethod
    def __init__(self, eventoId: UUID, usuarioId: UUID, timestamp: datetime):
        self._eventoId = eventoId
        self._usuarioId = usuarioId
        self._timestamp = timestamp

    @property
    def eventId(self) -> UUID:
        return self._eventoId
    
    @property
    def userId(self) -> UUID:
        return self._usuarioId
    
    @property
    def timestamp(self) -> datetime:
        return self._timestamp
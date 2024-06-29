from pydantic import BaseModel

class EmailCliente(BaseModel):
    _email: str
    
    def __init__(self, email: str):
        self._email = email
    
    @property
    def name(self):
        return self._email
    
    @staticmethod
    def create(email):
        return EmailCliente(email)
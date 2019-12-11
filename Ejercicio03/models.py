
from datetime import datetime

class Task:

    def __init__(self, id:int, fecha:datetime, descripcion:str, prioridad:int, estado:int):
        self.id = id
        self.fecha = fecha
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado

    @classmethod
    def new_task(cls):
        return cls(-1, datetime.now(), '', 0, 0)

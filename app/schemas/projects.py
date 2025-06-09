# PASO 1: IMPORTAR LA LIBRERIA. 
# PASO 2: CREAR LA CLASE BASE QUE CONTIENE TODOS LOS ATRIBUTOS QUE VA A ENVIAR AL FRONTEND


from pydantic import BaseModel 

class Proyecto(BaseModel): 
    id: int
    categoria: str
    imagen: str
    titulo: str
    descripcion: str
    tecnologias: str
    link_github: str
   
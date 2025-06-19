# PASO 1: IMPORTAR LA LIBRERIA. 
# PASO 2: CREAR LA CLASE BASE QUE CONTIENE TODOS LOS ATRIBUTOS QUE VA A ENVIAR AL FRONTEND


from pydantic import BaseModel,HttpUrl, field_validator

class Proyecto(BaseModel): 
    id: int
    categoria: str
    imagen: str
    titulo: str
    descripcion: str
    tecnologias: str
    link_github: HttpUrl

    @field_validator('id')
    def id_valido(cls,v): 
        if not v > 0:
            raise ValueError("El id debe ser mayor a 0")
        return v
    @field_validator('imagen')
    def imagen_valida(cls, v):
        if not v.startswith("http://127.0.0.1:8000/assets/img/"):
            raise ValueError("La imagen debe estar en la carpeta /assets/img/")
        return v

    @field_validator('categoria', 'titulo', 'descripcion')
    def validar_campos(cls,v): 
        if not v.strip():
            raise ValueError("El campo NO puede estar vacio.")
        return v

    @field_validator('tecnologias')
    def tecnologias_validas(cls, v):
        if "," not in v:
            raise ValueError("El campo 'tecnologias' debe contener al menos dos tecnologías separadas por coma")
        return v

    @field_validator('link_github')
    def link_valido(cls,v): 
        if not v.startswith("https://github.com/"):
            raise ValueError("El link debe ser de github")
        return v
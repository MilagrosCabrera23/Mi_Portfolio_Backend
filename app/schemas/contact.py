from pydantic import BaseModel, EmailStr, field_validator

class FormContact(BaseModel): 
    nombre: str
    telefono: str
    email: EmailStr
    asunto: str
    mensaje: str

    @field_validator('nombre')
    def nombre_valido(cls,v): 
         if not v.replace(" ", "").isalpha():
            raise ValueError("El nombre solo debe contener letras y espacios")
         if len (v.strip()) == 0:
            raise ValueError("El nombre NO debe estar vacio ")
         return v
    

    @field_validator('telefono')
    def telefono_valido(cls,v): 
            if not v.isdigit():
                raise ValueError("El teléfono debe ser solo números")
            if len(v) < 8:
                raise ValueError("El teléfono es demasiado corto, debe superar los 8 digitos.")
            return v

    @field_validator('asunto')
    def asunto_valido(cls,v): 
        if not (1 <= len(v) <= 50):
         raise ValueError("El asunto debe tener entre 1 y 50 caracteres")
        return v

    @field_validator('mensaje')
    def mensaje_valido(cls,v): 
         if not(7 <= len(v) <= 410):
              raise ValueError("El mensaje debe tener entre 7 y 410 caracteres")
         return v
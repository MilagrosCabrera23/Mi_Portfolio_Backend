from fastapi import APIRouter
from app.schemas.contact import FormContact

router = APIRouter()

@router.post("/contacto")
async def enviar_form(data:FormContact):
    print("Formulario recibido", data)
    return {"Mensaje": "Formulario enviado con éxito"} 
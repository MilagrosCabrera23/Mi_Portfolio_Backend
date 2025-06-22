from fastapi import APIRouter, HTTPException
from app.schemas.contact import FormContact
from fastapi_mail import FastMail, MessageSchema, MessageType
from config import conf

router = APIRouter()

@router.post("/contacto")
async def enviar_form(form: FormContact):
    try:
        # Crear el cuerpo del mensaje HTML
        mensaje = MessageSchema(
            subject=f"Nuevo mensaje: {form.asunto}", 
            recipients=["milagrosmagalycabrera@gmail.com"], 
            body=f"""
                <h2>Nuevo contacto desde el formulario</h2>
                <ul>
                    <li><strong>Nombre:</strong> {form.nombre}</li>
                    <li><strong>Email:</strong> {form.email}</li>
                    <li><strong>Teléfono:</strong> {form.telefono}</li>
                </ul>
                <p><strong>Mensaje:</strong><br>{form.mensaje}</p>
            """,
            subtype=MessageType.html
        )

        fm = FastMail(conf)          
        await fm.send_message(mensaje)  
        return {"mensaje": "Correo enviado correctamente"}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al enviar el correo: {str(e)}"
        )

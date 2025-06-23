# 💼 Portfolio API con FastAPI

Este proyecto es una API desarrollada con **FastAPI** que sirve como backend para mi portafolio web. Contiene dos funcionalidades principales:

1.  Gestión de proyectos (para mostrar en el portafolio)
2.  Formulario de contacto (con envío de correos)
--- 
# Enlaces de la API

- 📬 **Contacto:** [https://milagroscabrera-portfoliobackend.onrender.com/contacto](https://milagroscabrera-portfoliobackend.onrender.com/contacto)
- 📁 **Proyectos:** [https://milagroscabrera-portfoliobackend.onrender.com/proyectos](https://milagroscabrera-portfoliobackend.onrender.com/proyectos)
- 📚 **Documentación Swagger (docs):** [https://milagroscabrera-portfoliobackend.onrender.com/docs](https://milagroscabrera-portfoliobackend.onrender.com/docs)
---


##  Tecnologías usadas

- [FastAPI](https://fastapi.tiangolo.com/) — Framework principal
- [FastAPI-Mail](https://github.com/sabuhish/fastapi-mail) — Envío de correos electrónicos desde el formulario de contacto
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Carga de variables de entorno desde archivos `.env`
- [Pydantic](https://docs.pydantic.dev/) — Validaciones de datos
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI para correr FastAPI

---
## Estructura del proyecto
```
└── app/
    ├── assets/
    ├── routes/
    │   ├── contact.py
    │   └── projects.py
    └── schemas/
        ├── contact.py
        └── projects.py
    ├── .env
    ├── config.py
    ├── main.py
    ├── requirements.txt
```
## 🧪 Endpoints principales

### ✅ `/proyectos`
Devuelve la lista de proyectos para mostrar en el frontend del portafolio.

- **Método:** `GET`
- **Respuesta:** JSON con la información de los proyectos.

### ✅ `/contacto`
Recibe el formulario de contacto y envía un correo con los datos.

- **Método:** `POST`
- **Body:** JSON con los campos: `nombre`, `telefono`, `email`, `asunto`, `mensaje`
- **Validaciones:** implementadas con `Pydantic`
- **Envío:** mediante `FastAPI-Mail` usando variables de entorno

---

##  Configuración del archivo `.env`

El archivo `.env` contiene las variables sensibles necesarias para enviar correos. Ejemplo:

```env

MAIL_USERNAME=tu_correo@gmail.com
MAIL_PASSWORD=tu_contraseña_o_app_password
MAIL_FROM=tu_correo@gmail.com
```
##  Pasos para correr el 

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```
### 2.  Instalar dependencias
```bash
pip install -r requirements.txt
```
### 3.  Crear el archivo .env
```bash
MAIL_USERNAME=tu_correo@gmail.com
MAIL_PASSWORD=tu_contraseña_o_app_password
MAIL_FROM=tu_correo@gmail.com

```
### 4.  Ejecutar el servidor
```bash
uvicorn main:app --reload
```
##  Notas adicionales
- El CORS debe estar habilitado si consumís esta API desde un frontend externo (por ejemplo, React).

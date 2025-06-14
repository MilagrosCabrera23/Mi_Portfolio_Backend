from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routes import projects

app = FastAPI()

# Permitir que React (u otras apps externas) accedan a esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción se pone tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# CORS, rutas, etc...   

# Servir carpeta de imágenes
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")

# Agregar las rutas desde el archivo proyectos.py
app.include_router(projects.router)
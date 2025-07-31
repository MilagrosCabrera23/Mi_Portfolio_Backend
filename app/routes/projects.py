# PASO 3: Crear la ruta que devuelve los proyectos, EN DONDE PRIMERO IMPORTAMOS FAST API, Y LUEGO A PROJECTS QUE VIENE DE SCHEMAS 

from fastapi import APIRouter
from app.schemas.projects import Proyecto
from typing import List

router = APIRouter()

proyectos = [
    Proyecto(
        id=1,
        categoria="Backend",
        imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/sistema-reservas.webp",
        titulo="Sist de Reservas para Consultorios Médicos",
        descripcion="API REST para gestionar reservas médicas con autenticación JWT. Permite a pacientes reservar turnos, doctores gestionar horarios y administradores supervisar el sistema completo.", 
        tecnologias="FastAPI,SQLAlchemy, MySQL, JWT, Pydantic,Uvicorn",
        link_github="https://github.com/MilagrosCabrera23/Sistema-de-reservas-para-consultorios-medicos" 
    ), 
     Proyecto(
        id=2,
        categoria="Full Stack",
        imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/thinktopia.webp",
        titulo="Thinktopia - Plataforma de Actividades Academicas",
        descripcion="Este proyecto consiste en la creación de una plataforma web para gestionar y registrar actividades académicas en instituciones educativas.",
        tecnologias="Angular, Django, Html, Css,Boostrap",
        link_github="https://github.com/MilagrosCabrera23/Thinktopia-Plataforma-de-actividades-Academicas" 
    ), 
        Proyecto(
            id=3, 
            categoria="Backend",
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/crud-user.webp",
            titulo="Crud de Usuarios - API REST",
            descripcion="API REST completa para gestión de usuarios con operaciones CRUD, validación de datos con Pydantic y arquitectura modular siguiendo buenas prácticas de producción.",
            tecnologias="FastAPI, MySQL, SQLAlchemy, Pydantic, Uvicorn",
            link_github="https://github.com/Academic-Developers/Thinktopia-Plataforma-de-actividades-Academicas"
        ),
        Proyecto(
            id=4, 
            categoria="Full Stack",
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/blog.webp",
            titulo="Blog Eterna Aprendiz",
            descripcion="Plataforma de blog de aprendizaje.Permite crear, editar y publicar artículos con categorías, comentarios y sistema de búsqueda.",
            tecnologias="Django, HTML, CSS, Bootstrap, MySQL,Python",
            link_github="https://github.com/MilagrosCabrera23/Blog-Eterna-Aprendiz"
        ), 
         Proyecto(
            id=5,   
            categoria="Backend",
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/gestion-inventario.webp",
            titulo="Gestión de Inventario y Stock ",
            descripcion="API REST robusta para control de inventario empresarial con gestión de productos, proveedores, movimientos de stock y reportes. Implementa autenticación, validaciones y arquitectura escalable.",
            tecnologias="Django, Django REST Framework, MySQL, JWT",
            link_github="https://github.com/MilagrosCabrera23/Gestion-de-inventario-y-stock"
        ), 
         Proyecto(
            id=6, 
            categoria="Full Stack",
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/gestion-eventos.webp",
            titulo="App de Gestion de  Gestión de eventos",
            descripcion="Aplicación para organización y gestión de eventos con registro de participantes, control de asistencia y dashboard administrativo.",
            tecnologias="FastAPI, React, MySQL, SQLAlchemy, JWT, Pydantic",
            link_github="https://github.com/MilagrosCabrera23/App-de-gestion-de-eventos"
        ),
         Proyecto(
            id=7, 
            categoria="Backend",
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/convertidor-monedas.webp",
            titulo="API Convertidor de Monedas",
            descripcion="API REST robusta para conversión de divisas en tiempo real con gestión de usuarios. Implementa arquitectura en capas, validación de datos y documentación automática con Swagger.",
            tecnologias="FastAPI, SQLAlchemy, MySQL, Pydantic, Uvicorn, Docker",
            link_github="https://github.com/MilagrosCabrera23/Api-convertidor-de-monedas"
        ), 
        Proyecto(
            id=8, 
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/administrador-tareas.webp",
            categoria="Full Stack",
            titulo="Administrador de tareas",
            descripcion="Aplicación full stack para gestión de tareas con CRUD completo. Frontend en React con diseño responsive y backend API REST con Node.js/Express.",
            tecnologias="React, Vite, Node.js, Express, React Bootstrap, React Router",
            link_github="https://github.com/MilagrosCabrera23/administrador-de-tareas"
        )
]

@router.get("/proyectos", response_model=list[Proyecto])

def obtener_proyectos():
    return proyectos

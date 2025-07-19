# PASO 3: Crear la ruta que devuelve los proyectos, EN DONDE PRIMERO IMPORTAMOS FAST API, Y LUEGO A PROJECTS QUE VIENE DE SCHEMAS 

from fastapi import APIRouter
from app.schemas.projects import Proyecto
from typing import List

router = APIRouter()

proyectos = [
    Proyecto(
        id=1,
        categoria="Desarrollo Web",
        imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/arg-broker.png",
        titulo=" Arg Broker – Gestión de Inversiones",
        descripcion="Plataforma para gestionar inversiones financieras de forma sencilla. Permite registrarse, comprar y vender acciones, y visualizar el rendimiento del portafolio con gráficos e indicadores", 
        tecnologias="Python, MySql,Patron Dao",
        link_github="https://github.com/MilagrosCabrera23/proyecto_integrador_broker" 
    ), 
     Proyecto(
        id=2,
        categoria="Desarrollo Web",
        imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/ecommerce.png",
        titulo="E-commerce Firebase – Trendy Threads",
        descripcion=" Catálogo de ropa online organizado por categorías, diseñado para  ofrecer una experiencia de compra cómoda y atractiva.",
        tecnologias="React, Firebase, Html, Css, Boostrap React",
        link_github="https://github.com/MilagrosCabrera23/EntregaFinal-React-CabreraMilagros" 
    ), 
        Proyecto(
            id=3, 
            categoria="Desarrollo Web",
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/thinktopia.png",
            titulo="Thintopia - Plataforma de Actividades Academicas",
            descripcion="Este proyecto consiste en la creación de una plataforma web para gestionar y registrar actividades académicas en instituciones educativas.",
            tecnologias="Angular, Django, Html, Css,Boostrap",
            link_github="https://github.com/Academic-Developers/Thinktopia-Plataforma-de-actividades-Academicas"
        ),
        Proyecto(
            id=4, 
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/qr.png",
            categoria="Desarrollo Web",
            titulo="Codificador-Decodificador QR",
            descripcion="Este proyecto es un codificador y decodificador de códigos QR desarrollado en Python. Permite generar códigos QR a partir de texto y leer información desde códigos QR existentes.",
            tecnologias="Python, Streamlit, OpenCV, qrcode",
            link_github="https://github.com/MilagrosCabrera23/Codificador-Decodificador-QR-Python"
        ), 
         Proyecto(
            id=5, 
            imagen="https://milagroscabrera-portfoliobackend.onrender.com/assets/img/acortador.png",
            categoria="Desarrollo Web",
            titulo="Acortador URL",
            descripcion="Esta es una aplicación web simple para acortar URLs utilizando Python y Streamlit. Con esta herramienta, los usuarios pueden ingresar una URL larga y generar una versión corta mediante la API de TinyURL",
            tecnologias="Python,Streamlit, Pyshortener",
            link_github="https://github.com/MilagrosCabrera23/Acortador_URL_Python"
        )
]

@router.get("/proyectos", response_model=list[Proyecto])

def obtener_proyectos():
    return proyectos
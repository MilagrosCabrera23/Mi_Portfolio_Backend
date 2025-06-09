# PASO 3: Crear la ruta que devuelve los proyectos, EN DONDE PRIMERO IMPORTAMOS FAST API, Y LUEGO A PROJECTS QUE VIENE DE SCHEMAS 

from fastapi import APIRouter
from app.schemas.projects import Proyecto
from typing import List

router = APIRouter()

proyectos = [
    Proyecto(
        id=1,
        categoria="Desarrollo Web",
        imagen="http://127.0.0.1:8000/assets/img/arg-broker.png",
        titulo=" Arg Broker – Gestión de Inversiones",
        descripcion="Plataforma para gestionar inversiones financieras de forma sencilla. Permite registrarse, comprar y vender acciones, y visualizar el rendimiento del portafolio con gráficos e indicadores", 
        tecnologias="Python, MySql, Patron DAO",
        link_github="https://github.com/MilagrosCabrera23/proyecto_integrador_broker" 
    ), 
     Proyecto(
        id=2,
        categoria="Desarrollo Web",
        imagen="http://127.0.0.1:8000/assets/img/ecommerce.png",
        titulo="E-commerce Firebase – Trendy Threads",
        descripcion=" Catálogo de ropa online organizado por categorías, diseñado para  ofrecer una experiencia de compra cómoda y atractiva. Incluye carrito de compras, detalles completos de productos y navegación intuitiva.",
        tecnologias="React, Firebase, HTML, CSS, BOOSTRAP REACT",
        link_github="https://github.com/MilagrosCabrera23/EntregaFinal-React-CabreraMilagros" 
    ), 
    Proyecto(
        id=3,
        categoria="IOT",
        imagen="http://127.0.0.1:8000/assets/img/sistema-iot.png",
        titulo="Sistema IoT con Node-RED",
         descripcion="  Dashboard web en tiempo real para visualizar datos de sensores IoT (ESP32), integrados con MySQL. Incluye monitoreo continuo, alertas automáticas ante valores fuera de rango y escalabilidad para agregar nuevos dispositivos.",
         tecnologias="Esp32, Node-RED, MySql, Mqtt",
        link_github="https://github.com/MilagrosCabrera23/Escalado-de-plataforma-Iot-con-visualizacion-de-datos-en-node-red"
        ), 
        Proyecto(
            id=4, 
            categoria="Desarrollo Web",
            imagen="http://127.0.0.1:8000/assets/img/Thinktopia.png",
            titulo="Thintopia - Plataforma de Actividades Academicas",
            descripcion="",
            tecnologias="Angular, Django, HTML, CSS,BOOSTRAP",
            link_github="https://github.com/Academic-Developers/Thinktopia-Plataforma-de-actividades-Academicas"
        ),
        Proyecto(
            id=5, 
            imagen="http://127.0.0.1:8000/assets/img/QR.png",
            categoria="Desarrollo Web",
            titulo="Codificador-Decodificador-QR-Python",
            descripcion="Este proyecto es un codificador y decodificador de códigos QR desarrollado en Python. Permite generar códigos QR a partir de texto y leer información desde códigos QR existentes.",
            tecnologias="Python, Streamlit, OpenCV, qrcode",
            link_github="https://github.com/MilagrosCabrera23/Codificador-Decodificador-QR-Python"
        ), 
        Proyecto(
            id=6, 
            imagen="http://127.0.0.1:8000/assets/img/acortador.png",
            categoria="Desarrollo Web",
            titulo="Acortador_URL_Python",
            descripcion="Esta es una aplicación web simple para acortar URLs utilizando Python y Streamlit. Con esta herramienta, los usuarios pueden ingresar una URL larga y generar una versión corta mediante la API de TinyURL",
            tecnologias="Python,streamlit, Pyshortener",
            link_github="https://github.com/MilagrosCabrera23/Acortador_URL_Python"
        ), 
        Proyecto(
            id=7, 
            imagen="http://127.0.0.1:8000/assets/img/prototipo-iot.png",
            categoria="IOT",
            titulo="Desarrollo de Prototipos IoT con ESP32",
            descripcion="Este repositorio contiene la implementación de dos proyectos IoT desarrollados como parte del curso de la Tecnicatura Superior en Desarrollo de Software del ISPC. Ambos proyectos utilizan la plataforma ESP32 y el simulador Wokwi.",
            tecnologias="",
            link_github="https://github.com/MilagrosCabrera23/Desarrollo-de-Prototipos-IoT-con-ESP32n-Wokwi--Iot"
        )
]

@router.get("/proyectos", response_model=list[Proyecto])

def obtener_proyectos():
    return proyectos
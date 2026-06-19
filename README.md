# FESTIVAL-DEVOPS-2026

[![Validacion Proyecto](https://github.com/kevinmesadelgado-maker/festival-devops-2026/actions/workflows/ci.yml/badge.svg)](https://github.com/kevinmesadelgado-maker/festival-devops-2026/actions/workflows/ci.yml)

## Descripción

Proyecto desarrollado para la actividad de aprendizaje de Git, GitHub, Docker y GitHub Actions para programa DevOps y Contenedores Docker. Incluye una interfaz web básica, un backend en Flask y un workflow de integración continua para validar la estructura del proyecto.

## Tecnologías utilizadas

* HTML5
* CSS3
* JavaScript
* Python
* Flask
* Docker
* Docker Compose
* Git
* GitHub
* GitHub Actions

## Estructura del proyecto

```
FESTIVAL-DEVOPS-2026/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── init.sql
└── README.md
```

## Integración Continua (CI)

Se implementó un workflow de GitHub Actions que se ejecuta automáticamente cuando:

* Se realiza un Push a la rama `main`.
* Se crea un Pull Request hacia la rama `main`.

### Validaciones automáticas

El workflow verifica la existencia de los siguientes archivos:

* `frontend/index.html`
* `frontend/css/style.css`
* `frontend/js/script.js`
* `README.md`

Si alguno de estos archivos no existe, la ejecución falla automáticamente.

## Control de versiones

Se utilizó Git Flow básico mediante las siguientes ramas:

* main
* feature-landing
* feature-backend

## Autor

**Kevin Alexis Mesa Delgado**

Ficha: **3223874**

Programa: **DevOps y Contenedores Docker**

# SmartGastro Web

##  Descripción

SmartGastro Web es un sistema de gestión desarrollado para foodtrucks.

Su objetivo es ayudar a controlar el stock, registrar ventas y asistir en la toma de decisiones mediante información climática obtenida desde una API externa.

El proyecto fue desarrollado como Producto Mínimo Viable (MVP) utilizando Flask, SQLAlchemy y una arquitectura basada en APIs REST.


#  Funcionalidades

* Inicio de sesión seguro
* Contraseñas protegidas con BCrypt
* Autenticación mediante JWT
* Gestión de productos
* Registro de ventas
* Descuento automático de stock
* Dashboard principal
* Integración con OpenWeather
* Operaciones asíncronas utilizando Fetch API
* API REST protegida

#  Tecnologías utilizadas

### Backend

* Python
* Flask
* SQLAlchemy
* SQLite
* Flask-Bcrypt
* PyJWT
* Requests

### Frontend

* HTML5
* CSS3
* Jinja
* JavaScript
* Font Awesome


# Estructura del proyecto

```text
SmartGastro-Web/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
│
├── database/
├── middleware/
├── models/
├── routes/
├── services/
├── static/
├── templates/
└── utils/
```


#  Instalación

## 1. Clonar el proyecto

```bash
git clone https://github.com/AlejandroRibera1987/SmartGastro-Web.git
```


## 2. Crear entorno virtual

### Windows

```bash
python -m venv venv
```

Activar:

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Crear archivo .env

Copiar el archivo:

```text
.env.example
```

como

```text
.env
```

y completar las variables de entorno.


## 5. Ejecutar el proyecto

```bash
python app.py
```

La aplicación estará disponible en:

```text
http://127.0.0.1:5000
```


#  Variables de entorno

```text
Se enviaron por el campus las credenciales corespondientes
```


#  Usuario de prueba

El sistema crea automáticamente un usuario administrador al iniciarse por primera vez.

Usuario:

```text
admin
```

Contraseña:

```text
123456
```

---

# API REST

## Autenticación

```
POST /api/auth/login
POST /api/auth/token
```

## Productos

```
GET /api/productos
POST /api/productos
PUT /api/productos/<id>
DELETE /api/productos/<id>
```

## Ventas

```
GET /api/ventas
POST /api/ventas
```

## Clima

```
GET /api/clima
```

#  Arquitectura

El proyecto implementa una arquitectura por capas:

```text
Cliente

↓

HTML + Jinja

↓

API Flask

↓

Services

↓

Models (SQLAlchemy)

↓

SQLite

↓

API OpenWeather
```

# Capturas del sistema

## Login

![Login](static/img/readme/login.png)

## Dashboard

![Dashboard](static/img/readme/dashboard.png)

## Productos

![Productos](static/img/readme/productos.png)

## Ventas

![Ventas](static/img/readme/ventas.png)

# Pruebas en Postman

## Generación de token JWT

![Postman Token](static/img/readme/postman-token.png)

## Listado de productos desde API

![Postman Productos](static/img/readme/postman-productos.png)

## API de clima

![Postman Clima](static/img/readme/postman-clima.png)


# Metodología de desarrollo

El proyecto fue desarrollado siguiendo una metodología ágil mediante un tablero Kanban en Trello.

Las funcionalidades implementadas corresponden a Historias de Usuario definidas durante la etapa de análisis y fueron desarrolladas de manera incremental.

Tablero Kanban:
https://trello.com/invite/b/69f9fc7d86946c623d2d56a7/ATTI20f0b7a3d8c6ad7fbea461b237cc96e09C672AB6/smartgastro

![Kanban](static/img/readme/kanban.png)

#  Integrantes

* Alejandro Ribera

## Materia

Análisis y Metodología de Sistemas
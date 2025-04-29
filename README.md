# 🌟 Sistema Esencial para Afiliados

## 📌 Descripción

El **Sistema Esencial para Afiliados** es una plataforma completa diseñada para gestionar un programa de afiliados, transacciones, carteras digitales y sistemas de bonificación de puntos. Está construida con **FastAPI**, **SQLModel** y **PostgreSQL**, ofreciendo una API REST eficiente y escalable.

---

## 🚀 Características principales

- 🧑‍🤝‍🧑 **Gestión de clientes**: Registro de clientes normales y afiliados, con generación automática de códigos de afiliado.
- 💼 **Sistema de carteras digitales**: Cada cliente posee su propia cartera para gestionar diferentes activos.
- 💰 **Gestión de activos**: Soporte para activos como puntos, dinero, etc.
- 🔁 **Sistema de transacciones**: Registro completo de movimientos (entrada y salida de activos).
- 🎯 **Sistema de bonificaciones**: Motor configurable para bonificaciones por ventas, rachas, afiliados y logros.
- 📡 **API RESTful**: Endpoints bien definidos para todas las operaciones.

---

## 🧱 Estructura del proyecto

├── .venv/
├── alembic/
├── src/
│   ├── __pycache__/
│   ├── main.py
│   ├── api/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── api_v1.py
│   ├── assets/
│   │   ├── __pycache__/
│   │   ├── enums/
│   │   ├── models/
│   │   ├── bonus_services.py
│   │   ├── routes.py
│   │   └── services.py
│   ├── clients/
│   │   ├── __pycache__/
│   │   ├── enums/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── services.py
│   ├── core/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── db.py
│   ├── sales/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── services.py
│   ├── types/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   └── response_type.py
│   └── wallets/
│       ├── __pycache__/
│       ├── __init__.py
│       ├── models.py
│       ├── routes.py
│       ├── services.py
│       └── main.py
├── .env
├── .gitignore
├── alembic.ini
└── README.md



---

## 🛠️ Tecnologías utilizadas

- ⚡ **FastAPI**: Framework web de alto rendimiento
- 🧬 **SQLModel**: ORM basado en SQLAlchemy y Pydantic
- 🐘 **PostgreSQL**: Base de datos relacional
- 🔎 **Pydantic**: Validación de datos
- 🧪 **Alembic**: Migraciones de base de datos
- 🚀 **Uvicorn**: Servidor ASGI para FastAPI

---

## 🧠 Patrones y conceptos clave

- 🧩 **Patrón Estrategia**: Para intercambiar algoritmos de cálculo de bonificación
- 🧱 **Responsabilidad Única**: Cada servicio tiene una única función
- 📦 **Principio Abierto/Cerrado**: Facilita extender sin modificar código
- 📐 **Separación de preocupaciones**: Separación clara entre modelos, lógica y rutas
- 🔐 **Transacciones atómicas**: Seguridad en operaciones complejas

---

## ▶️ Empezando

### ✅ Requisitos previos

- Python 3.9+
- PostgreSQL
- Git

### ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Thomasrr29/affiliate_system.git
cd affiliate_essential_system

# Crear entorno virtual
python -m venv .venv

# Activar entorno
# En Windows
.venv\Scripts\activate
# En macOS/Linux
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
echo "DATABASE_URL=postgresql+asyncpg://usuario:contraseña@localhost/affiliate_db" > .env

# Ejecutar migraciones
alembic upgrade head

# Iniciar servidor
uvicorn src.main:app --reload
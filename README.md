# 🧘‍♀️ Pilates Finanzas - Asistente Financiero con IA

Un asistente virtual e interactivo de análisis financiero diseñado para estudios de Pilates. La aplicación conecta una base de datos relacional MySQL con un modelo de Inteligencia Artificial (Google Gemini) a través de un backend en Flask, permitiendo a los administradores realizar preguntas en lenguaje natural sobre sus ventas, gastos y rendimiento por sucursal.

---

## 🏗️ Arquitectura de la Solución

El sistema sigue una arquitectura cliente-servidor basada en el patrón MVC (Modelo-Vista-Controlador):

```text
[ Usuario / Navegador ]
        │
        ▼ (Petición HTTP / Fetch JSON)
[ Frontend: HTML5 / CSS3 / JavaScript ]
        │
        ▼ (API REST / POST /api/pregunta)
[ Backend: Flask (Python) ]
   ├── 1. Consulta SQL ───► [ Base de Datos: MySQL ]
   │   (Obtiene ingresos,   (Tablas: clientes,
   │    gastos y métricas)   ingresos, gastos)
   │                       
   └── 2. Contexto + Prompt ───► [ Google Gemini API ]
                                 (Modelo gemini-2.0-flash / 3.5-flash)
        ▲
        └─────── Respuestas generadas con IA ───────┘

Flujo de trabajo:
El usuario envía una pregunta desde la interfaz del chat.

El backend en Flask consulta la base de datos MySQL para extraer un resumen consolidado de las finanzas (totales de ingresos, gastos, clientes y desglose por sucursal).

Flask construye un prompt enriquecido con estos datos reales y se lo envía a la API de Gemini.

La IA procesa la información y devuelve una respuesta contextualizada, analítica y profesional al usuario en pantalla.

🛠️ Tecnologías y Herramientas
Lenguaje principal: Python 3.x

Backend: Flask, Flask-CORS

Base de Datos: MySQL (conectado vía SQLAlchemy y PyMySQL)

Inteligencia Artificial: Google Gemini API (google-generativeai)

Procesamiento de Datos: Pandas

Frontend: HTML5, CSS3, JavaScript (Fetch API)

Control de Versiones y Entorno: Git, GitHub, Python venv, python-dotenv

🚀 Instalación y Configuración Local
Prerrequisitos
Python 3.10 o superior instalado.

Servidor MySQL en ejecución (local) con la base de datos pilatesFinanzas.

Pasos para ejecutar el proyecto
Clonar el repositorio:

Bash
git clone [https://github.com/TU_USUARIO/pilates-finanzas.git](https://github.com/TU_USUARIO/pilatesFinanzas.git)
cd pilatesFinanzas
Crear y activar el entorno virtual:

Bash
python -m venv .venv
# En Windows:
.\.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Configurar variables de entorno (.env):
Crea un archivo llamado .env en la raíz del proyecto y agrega tus credenciales:

Fragmento de código
DB_USER=root
DB_PASS=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=pilates_finanzas
GEMINI_API_KEY=tu_api_key_de_gemini

Iniciar la aplicación:

Bash
python app.py
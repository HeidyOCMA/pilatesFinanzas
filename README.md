# 🧘‍♀️ Pilates Finanzas - Asistente Financiero con IA

Un asistente virtual e interactivo de análisis financiero diseñado para estudios de Pilates. La aplicación conecta una base de datos relacional MySQL con un modelo de Inteligencia Artificial (Google Gemini) en version beta, pero luego se migro al no poder generar una claveapi gratuita, se genero una clave con grok, y se modifio el backend en Flask, permitiendo a los administradores realizar preguntas en lenguaje natural sobre sus ventas, gastos , en siguientes versiones se buscara dashboarad indicadores y mas consultas de ventas, por sucursal y por mes.

---

## 📌 Descripción General del Proyecto
**Pilates Finanzas** es una solución inteligente diseñada para optimizar el análisis financiero de un estudio de Pilates. A través de un agente de IA integrado con la lectura de archivos csv, con los ingresos, costos, ventas, clientes e instructore, los cuales en esta version beta se generaron con python, de un rango de 3 años. Se genero un modulo que guarda los datos de los csv en una base de datos de mysql. La aplicación permite que el CEO realice consultas en lenguaje natural sobre ingresos, gastos,  obteniendo respuestas financieras precisas e instantáneas.

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
   └── 2. Contexto + Prompt ───► [ Groq Cloud API / Llama 3.3)]
                                [versioninicial[Google Gemini API ]]
                                 
        ▲
        └─────── Respuestas generadas con IA ───────┘

## 🏗️ Arquitectura de la Solución

El flujo de trabajo de la aplicación sigue una arquitectura cliente-servidor orientada a servicios de datos e inteligencia artificial:

1. **Frontend (Interfaz Web):** Interfaz sencilla construida con HTML, CSS y JavaScript para la interacción vía chat en tiempo real.
2. **Backend (API con Flask):** Servidor Python que recibe la consulta del usuario, coordina la extracción de datos de la base de datos y gestiona el prompt para el modelo de IA.
3. **Capa de Datos (MySQL + Pandas):** Consultas optimizadas mediante `SQLAlchemy` y `Pandas` para agregar y estructurar métricas clave (totales, ventas por mes/año/sucursal (se sigue trabajando en mejors y agregar consultas que retornen metricas)).
4. **Motor de IA (Groq Cloud API / Llama 3.3):** Modelo de lenguaje gran tamaño (*LLM*) parametrizado con instrucciones financieras estrictas (*system prompt*) para responder con precisión basándose exclusivamente en el contexto de las consultas a la base de datos.
Flujo de trabajo:
El usuario envía una pregunta desde la interfaz del chat.

El backend en Flask consulta la base de datos MySQL para extraer un resumen consolidado de las finanzas (totales de ingresos, gastos, clientes y desglose por sucursal(en proceso)).

Flask construye un prompt enriquecido con estos datos reales y se lo envía a la API.

La IA procesa la información y devuelve una respuesta contextualizada, analítica y profesional al usuario en pantalla.

🛠️ Tecnologías y Herramientas
Lenguaje principal: Python 3.x

Backend: Flask, Flask-CORS

Base de Datos: MySQL (conectado vía SQLAlchemy y PyMySQL)

Inteligencia Artificial: 
Groq Cloud API / Llama 3.3):** Modelo de lenguaje gran tamaño (*LLM*) parametrizado con instrucciones financieras estrictas (*system prompt*) para responder con precisión basándose exclusivamente en el contexto de la base de datos.

Procesamiento de Datos: Pandas

Frontend: HTML5, CSS3, JavaScript (Fetch API)

Control de Versiones y Entorno: Git, GitHub, Python venv, python-dotenv

🚀 Instalación y Configuración Local
Prerrequisitos
Python 3.10 o superior instalado.

Servidor MySQL en ejecución (local) con la base de datos pilatesFinanzas.

## 🚀 Instrucciones para Ejecutar el Proyecto

### Prerrequisitos
* Tener instalado Python 3.10 o superior.
* Servidor MySQL en ejecución con la base de datos de Pilates cargada.
* Cuenta y API Key en [Groq Cloud](https://console.groq.com/).

Pasos para ejecutar el proyecto
Clonar el repositorio:

Bash
# 1. Clonar el repositorio e ingresar a la carpeta
git clone https://github.com/HeidyOCMA/pilatesFinanzas.git
cd pilatesFinanzas

# 2. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

Bash
# En Windows:
.\.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt

Configurar las variables de entorno (.env):
Crea un archivo llamado .env en la raíz del proyecto y añade tus credenciales:

Fragmento de código
DB_USER=root
DB_PASS=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=pilatesFinanzas
GEMINI_API_KEY=tu_api_key_de_gemini
GROQ_API_KEY=tu_nueva_api_key_aqui
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/nombre_base_datos

Iniciar la aplicación:

Bash
python app.py

## 🛠️ Tecnologías y Herramientas Utilizadas

* **Lenguaje Principal:** Python 3.10+
* **Framework Web:** Flask
* **Base de Datos:** MySQL
* **ORM & Manipulación de Datos:** SQLAlchemy, Pandas, PyMySQL
* **Modelo de Inteligencia Artificial:** Llama 3.3 70B via Groq Cloud API
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API / ES6+)
* **Gestión de Variables de Entorno:** `python-dotenv`
* **Control de Versiones:** Git & GitHub

Acceder a la aplicación:
Abre tu navegador web e ingresa a http://localhost:5000 (o el puerto configurado).

##Ejemplos de Preguntas que el Agente Puede Responder
Consultas Generales:

"¿Cuáles son los ingresos totales?"
"¿Cuál es el total de ingresos?"
"¿Cuál es el total de costos?"
"¿A cuánto ascienden los gastos acumulados?"

Filtros por Sucursal y Períodos:
"¿Qué sucursal tuvo mayores ingresos durante el último año?"

Análisis de Clientes:
"¿Cuántos clientes registrados tenemos en total?"

Ejemplos de Respuestas Generadas por el Agente
Ejemplo 1: Consulta de Clientes Principales
Usuario: "¿Quiénes fueron los clientes que más compraron en el año 2023?"

Agente IA:
"En el año 2023, los clientes con mayor monto acumulado de compra en Pilates Finanzas fueron:
María García: $15,400.00 (12 compras)
Carlos López: $12,850.00 (9 compras)

Ana Martínez: $10,200.00 (8 compras)"*

Ejemplo 2: Consulta de Ventas por Período y Sucursal
Usuario: "¿Cuáles el total de ingresos?"

Agente IA:

"El total de ingresos es $106,434,948.00 MXN."
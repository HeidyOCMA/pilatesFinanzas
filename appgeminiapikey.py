import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from sqlalchemy import create_engine, text
from google import genai

#load_dotenv()
load_dotenv(override=True)

app = Flask(__name__)
CORS(app)

# 2. Obtener y validar la API Key
# 2. DEFINIR LA VARIABLE (esta es la línea que falta):
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ALERTA: No se encontró GEMINI_API_KEY en el entorno.")
else:
    print(f"🔑 Clave cargada correctamente en app.py: {api_key[:6]}...")

# 3. Inicializar el cliente con la clave explícita
ai_client = genai.Client(api_key=api_key)

# 1. Conexión a MySQL
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "Rosa.1318")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "pilatesFinanzas")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# 2. Configuración de Gemini AI (Nuevo SDK Oficial)
api_key = os.getenv("GEMINI_API_KEY")
ai_client = genai.Client(api_key=api_key)

def obtener_resumen_base_datos():
    """Consulta la base de datos para darle contexto a la Inteligencia Artificial."""
    try:
        with engine.connect() as conn:
            tot_ingresos = conn.execute(text("SELECT COALESCE(SUM(total), 0) FROM ingresos")).scalar()
            tot_gastos = conn.execute(text("SELECT COALESCE(SUM(costo), 0) FROM gastos")).scalar()
            tot_clientes = conn.execute(text("SELECT COUNT(*) FROM clientes")).scalar()
            
            ventas_sucursal = pd.read_sql("SELECT sucursal, SUM(total) as total FROM ingresos GROUP BY sucursal", conn).to_dict(orient="records")
            gastos_tipo = pd.read_sql("SELECT tipogasto, SUM(costo) as total FROM gastos GROUP BY tipogasto", conn).to_dict(orient="records")
            
        return {
            "total_ingresos": float(tot_ingresos),
            "total_gastos": float(tot_gastos),
            "ganancia_neta": float(tot_ingresos - tot_gastos),
            "total_clientes": tot_clientes,
            "ingresos_por_sucursal": ventas_sucursal,
            "gastos_por_tipo": gastos_tipo
        }
    except Exception as e:
        print(f"Error al consultar la BD: {e}")
        return {}


@app.route("/")
def index():
    """Ruta que sirve la vista HTML principal."""
    return render_template("index.html")


@app.route("/api/pregunta", methods=["POST"])
def responder_pregunta():
    """Endpoint REST al que el Frontend enviará las dudas del usuario."""
    data = request.get_json()
    pregunta_usuario = data.get("pregunta", "").strip()

    if not pregunta_usuario:
        return jsonify({"error": "Por favor escribe una pregunta válida."}), 400

    try:
        resumen_finanzas = obtener_resumen_base_datos()

        prompt_sistema = f"""
        Eres un asistente analista financiero experto para un estudio de Pilates ('Pilates Finanzas').
        
        Datos actualizados de la base de datos MySQL:
        - Total Ingresos: ${resumen_finanzas.get('total_ingresos', 0):,.2f}
        - Total Gastos: ${resumen_finanzas.get('total_gastos', 0):,.2f}
        - Ganancia Neta: ${resumen_finanzas.get('ganancia_neta', 0):,.2f}
        - Clientes Registrados: {resumen_finanzas.get('total_clientes', 0)}
        - Ingresos por Sucursal: {resumen_finanzas.get('ingresos_por_sucursal', [])}
        - Gastos por Tipo: {resumen_finanzas.get('gastos_por_tipo', [])}

        Responde a la consulta del usuario de forma amigable, precisa y profesional.
        Consulta: "{pregunta_usuario}"
        """

        # Nueva llamada oficial con ai_client
        #response = ai_client.models.generate_content(
        #    model="gemini-2.5-flash",
        #    contents=prompt_sistema
        #)

        #response = ai_client.models.generate_content(
        #    model="gemini-2.0-flash",
        #    contents=prompt_sistema
        #)

        #response = ai_client.models.generate_content(
        #    model="gemini-2.0-flash-lite",
        #    contents=prompt_sistema
        #)

        response = ai_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt_sistema
        )

        return jsonify({
            "respuesta": response.text,
            "exito": True
        })

    except Exception as e:
        print(f"Error interno: {e}")
        return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
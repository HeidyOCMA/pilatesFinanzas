import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from sqlalchemy import create_engine, text
from groq import Groq

# 1. Cargar variables de entorno
load_dotenv(override=True)

app = Flask(__name__)
CORS(app)

# 2. Obtener la API Key de Groq (asegurando un valor válido)
api_key = os.getenv("GROQ_API_KEY")

# Si no la encuentra en .env, puedes poner tu clave gsk_... directo aquí entre comillas como respaldo:

# 3. Inicializar el cliente UNA SOLA VEZ
ai_client = Groq(api_key=api_key)

# 4. Conexión a MySQL
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "Rosa.1318")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "pilatesFinanzas")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


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
    data = request.get_json()
    pregunta_usuario = data.get("pregunta", "").strip()

    if not pregunta_usuario:
        return jsonify({"error": "Por favor escribe una pregunta válida."}), 400

    try:
        resumen_finanzas = obtener_resumen_base_datos()
        
        # 🔍 IMPRIME LOS DATOS EN LA TERMINAL PARA VERIFICAR:
        print("--- DATOS OBTENIDOS DE LA BD ---")
        print("Top clientes:", resumen_finanzas.get('top_clientes_por_año'))
        print("Ventas mes/año:", resumen_finanzas.get('ventas_por_mes_año_sucursal'))

        prompt_sistema = f"""
        ROLES E INSTRUCCIONES:
        Eres la Inteligencia Artificial analista financiera EXCLUSIVA del estudio de Pilates ('Pilates Finanzas').
        Tu ÚNICO objetivo es responder preguntas sobre el negocio utilizando los datos financieros provistos a continuación.

        REGLAS STRICTAS:
        1. NUNCA des definiciones teóricas, conceptos de economía generales ni explicaciones de diccionario.
        2. Si te preguntan por "ingresos totales", "gastos", "clientes" o cualquier dato, responde DIRECTAMENTE con las cifras reales de la base de datos de Pilates Finanzas.
        3. Si la información solicitada no está en los datos de abajo, indica amablemente que no dispones de ese dato en el sistema.

        DATOS REALES DEL NEGOCIO (PILATES FINANZAS):
        - Total Ingresos Histórico: ${resumen_finanzas.get('total_ingresos', 0):,.2f}
        - Total Gastos Histórico: ${resumen_finanzas.get('total_gastos', 0):,.2f}
        - Ganancia Neta: ${resumen_finanzas.get('ganancia_neta', 0):,.2f}
        - Clientes Totales Registrados: {resumen_finanzas.get('total_clientes', 0)}
        
        - Ventas Agrupadas por Sucursal: {resumen_finanzas.get('ingresos_por_sucursal', [])}
        - Gastos por Tipo: {resumen_finanzas.get('gastos_por_tipo', [])}
        - Histórico por Año, Mes y Sucursal: {resumen_finanzas.get('ventas_por_mes_año_sucursal', [])}
        - Top Clientes por Año: {resumen_finanzas.get('top_clientes_por_año', [])}
        """
        

        response = ai_client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": pregunta_usuario}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.4
        )

        respuesta_texto = response.choices[0].message.content
        
        # 🔍 IMPRIME LA RESPUESTA DE GROQ:
        print("--- RESPUESTA DE GROQ ---")
        print(respuesta_texto)

        return jsonify({
            "respuesta": respuesta_texto,
            "exito": True
        })

    except Exception as e:
        print(f"❌ Error interno en /api/pregunta: {e}")
        return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)
import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

raw_key = os.getenv("GEMINI_API_KEY")

print("--- DIAGNÓSTICO DE CLAVE ---")
if not raw_key:
    print("❌ ERROR: La variable 'GEMINI_API_KEY' no existe o está vacía en el archivo .env")
else:
    print(f"✅ Variable encontrada.")
    print(f"📌 Longitud total: {len(raw_key)} caracteres")
    print(f"📌 Empieza con: '{raw_key[:8]}'")
    print(f"📌 Termina con: '{raw_key[-4:]}'")
    
    # Probar la clave directamente contra la API
    try:
        client = genai.Client(api_key=raw_key.strip())
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Hola, responde OK"
        )
        print("\n🎉 ¡ÉXITO TOTAL! La clave funciona correctamente.")
        print(f"Respuesta de Gemini: {response.text}")
    except Exception as e:
        print("\n❌ FALLÓ LA PETICIÓN:")
        print(e)
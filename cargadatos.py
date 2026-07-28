
import os
import pandas as pd
from sqlalchemy import create_engine



# Cadena de conexión: mysql+pymysql://usuario:contraseña@localhost:3306/pilates_finanzas
engine = create_engine("mysql+pymysql://root:Rosa.1318@localhost:3306/pilatesFinanzas")

ruta = r"c:\ALURACHALLENGE\\"

try:
    # Crear motor de conexión
    #--engine = create_engine(DATABASE_URL)
    #--print("Conexión con MySQL establecida correctamente.\n")

    # ----------------------------------------------------
    # 2. Definición de Archivos CSV y Tablas Destino
    # ----------------------------------------------------
    # Usa 'r' antes de la ruta si usas rutas absolutas de Windows (ej. r"C:\mis_datos\clientes.csv")
    archivos = {
        "clientes": "clientes.csv",
        "instructores": "instructores.csv",
        "ingresos": "ingresos.csv",
        "gastos": "gastos.csv"
    }

    # ----------------------------------------------------
    # 3. Lectura de CSVs e Inserción Masiva
    # ----------------------------------------------------
    for tabla, ruta in archivos.items():
        if os.path.exists(ruta):
            print(f"Leyendo '{ruta}'...")
            df = pd.read_csv(ruta)
            
            # Si estamos en la tabla instructores y el CSV trae 'id_instructor', la renombramos a 'id'
            if tabla == "instructores" and "id_instructor" in df.columns:
                df = df.rename(columns={"id_instructor": "id"})
            
            # Inserta los datos en MySQL
            df.to_sql(name=tabla, con=engine, if_exists="append", index=False)
            print(f"-> ¡Tabla '{tabla}' cargada exitosamente ({len(df)} registros)!\n")
        else:
            print(f"⚠️ Error: El archivo '{ruta}' no fue encontrado.\n")
except Exception as e:
    print(f"Ocurrió un error durante la conexión o la carga: {e}")
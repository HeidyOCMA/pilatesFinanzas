import random
import datetime
import pandas as pd

# Fijar semilla para reproducibilidad
random.seed(1234)

# ==========================================
# 1. CLIENTES (generadores/clientes.py)
# ==========================================
# Nombres y apellidos para simular el mercado local (México)
NOMBRES_F = ["María", "Ana", "Sofía", "Fernanda", "Valeria", "Camila", "Lucía", "Ximena", "Daniela", "Mariana", "Andrea", "Paula", "Natalia", "Regina", "Renata", "Victoria", "Carolina", "Gabriela", "Laura", "Claudia"]
NOMBRES_M = ["Carlos", "Alejandro", "Mateo", "Santiago", "Diego", "Javier", "Luis", "Fernando", "Rodrigo", "Miguel", "Daniel", "Adrián", "Gabriel", "Pablo", "José", "Juan", "Ricardo", "Eduardo", "Hugo", "Óscar"]
APELLIDOS = ["Hernández", "García", "Martínez", "López", "González", "Pérez", "Rodríguez", "Sánchez", "Ramírez", "Cruz", "Flores", "Gómez", "Morales", "Vázquez", "Jiménez", "Reyes", "Díaz", "Torres", "Gutiérrez", "Mendoza"]

def generar_clientes(cantidad=450):
    clientes = []
    fecha_inicio = datetime.date(2021, 1, 1)
    fecha_fin = datetime.date(2026, 7, 31)
    dias_rango = (fecha_fin - fecha_inicio).days
    
    for i in range(cantidad):
        # En Pilates la proporción suele inclinarse más hacia mujeres (75/25 approx)
        sexo = "F" if random.random() < 0.75 else "M"
        if sexo == "F":
            nombre = f"{random.choice(NOMBRES_F)} {random.choice(APELLIDOS)} {random.choice(APELLIDOS)}"
        else:
            nombre = f"{random.choice(NOMBRES_M)} {random.choice(APELLIDOS)} {random.choice(APELLIDOS)}"
            
        # Fecha de registro aleatoria dentro del rango
        dias_rand = random.randint(0, dias_rango)
        fecha_reg = fecha_inicio + datetime.timedelta(days=dias_rand)
        
        # Sucursal preferida (Cuauhtémoc tiene ligera preferencia)
        sucursal = random.choice(["Cuauhtémoc", "Cuauhtémoc", "San Ángel"])
        
        # Teléfono y email limpios
        telefono = f"55{random.randint(10000000, 99999999)}"
        nombre_clean = nombre.lower().replace(" ", ".").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n")
        email = f"{nombre_clean}{random.randint(10,99)}@gmail.com"
        
        clientes.append({
            "id_cliente": f"C{i+1:04d}",
            "nombre": nombre,
            "sexo": sexo,
            "telefono": telefono,
            "email": email,
            "fecha_registro": fecha_reg.strftime("%Y-%m-%d"),
            "sucursal_preferida": sucursal
        })
    
    return pd.DataFrame(clientes)


# ==========================================
# 2. INSTRUCTORES (generadores/instructores.py)
# ==========================================
def generar_instructores():
    instructores = [
        ["I001", "Carlos Hernández", "Reformer", "2023-01-01"],
        ["I002", "Andrea Pérez", "Chair", "2023-01-01"],
        ["I003", "Fernanda Ruiz", "Cadillac", "2023-01-01"],
        ["I004", "Miguel Torres", "Mat", "2023-01-01"],
        ["I005", "Daniel López", "Reformer", "2023-01-01"],
        ["I006", "Patricia Díaz", "Chair", "2023-01-01"],
        ["I007", "Laura Gómez", "Reformer", "2024-02-15"],
        ["I008", "Jorge Castillo", "Cadillac", "2025-03-01"],
        ["I009", "Mónica Sánchez", "Reformer", "2026-01-10"]
    ]
    
    return pd.DataFrame(
        instructores,
        columns=["id", "nombre", "especialidad", "fecha_ingreso"]
    )


# ==========================================
# EJECUCIÓN Y GUARDADO DE ARCHIVOS
# ==========================================
if __name__ == "__main__":
    df_clientes = generar_clientes(450)
    df_clientes.to_csv("clientes.csv", index=False)

    df_instructores = generar_instructores()
    df_instructores.to_csv("instructores.csv", index=False)

    print("¡Archivos clientes.csv e instructores.csv generados con éxito!")
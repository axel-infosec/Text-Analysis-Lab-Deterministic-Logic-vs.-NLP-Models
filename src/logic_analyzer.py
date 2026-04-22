import pandas as pd
import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona el reporte de texto",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    root.destroy()
    return ruta_archivo

def identificador_palabras(texto):
    return re.findall(r"[\w'-]+", texto.lower())

def contador_manual_eficiente(lista_palabras):
    conteo = {}
    for palabra in lista_palabras:
        # Limpiamos guiones o comillas en los extremos
        palabra_limpia = palabra.strip("-'")
        if not palabra_limpia:
            continue
            
        if palabra_limpia in conteo:
            conteo[palabra_limpia] += 1
        else:
            conteo[palabra_limpia] = 1
    return {"palabra": list(conteo.keys()), "frecuencia": list(conteo.values())}

# --- Flujo Principal ---
ruta = seleccionar_archivo()

if ruta:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        print(f"Procesando de forma determinista: {os.path.basename(ruta)}")
        
        # Procesamiento
        palabras = identificador_palabras(contenido)
        datos_conteo = contador_manual_eficiente(palabras)
        
        # Reporte
        df = pd.DataFrame(datos_conteo)
        df = df.sort_values(by="frecuencia", ascending=False) # Ordenar por importancia
        
        fecha_texto = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"reporte_logica_{fecha_texto}.csv"
        df.to_csv(nombre_archivo, index=False)
        print(f"Éxito. Reporte generado: {nombre_archivo}")

    except Exception as e:
        print(f"Error técnico: {e}")
else:
    print("Operación cancelada por el usuario.")
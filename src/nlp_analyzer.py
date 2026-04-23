import spacy
from collections import Counter
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona el reporte de texto",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    root.destroy()
    return ruta_archivo
nlp = spacy.load("es_core_news_sm")

ruta = seleccionar_archivo()

if ruta:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        print(f"Analizando con IA: {os.path.basename(ruta)}...")

        doc = nlp(contenido)

        palabras_limpias = [t.lemma_.lower() for t in doc if t.is_alpha and not t.is_stop]
        
        frecuencias = Counter(palabras_limpias)
        df = pd.DataFrame(frecuencias.items(), columns=['Palabra', 'Frecuencia'])
        df = df.sort_values(by='Frecuencia', ascending=False)

        print("\n--- Top 10 palabras más frecuentes ---")
        print(df.head(10))
        
        df.to_csv("reporte_ia.csv", index=False)
        print("\nReporte guardado como 'reporte_ia.csv'")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
else:
    print("Operación cancelada.")
# Text-Analysis-Lab-Deterministic-Logic-vs.-NLP-Models
Estudio comparativo de procesamiento de datos: Lógica pura en Python vs. Procesamiento de Lenguaje Natural (NLP) con spaCy.
## Descripción General

Este repositorio es un estudio comparativo de dos paradigmas distintos para el procesamiento de texto y la normalización de datos. Como ingeniero, considero que la eficiencia no siempre significa usar la herramienta más compleja, sino la más adecuada para el problema.

Aquí resuelvo el mismo reto (limpieza de texto y análisis de frecuencia) usando dos enfoques: Lógica Determinista (Hardcoded) y Modelos Probabilísticos de NLP.

## Los 2 enfoques

1. Lógica Determinista (Python Puro)

- Metodología: Utiliza librerías estándar de Python, Expresiones Regulares (Regex) y manipulación manual de cadenas.

- Fortalezas: Extremadamente rápido, sin dependencias externas y 100% predecible.

- Ideal para: Procesamiento de logs técnicos, monitoreo de sistemas (entornos NOC) y escenarios donde la privacidad de los datos impide el uso de modelos externos.

- Característica Clave: Implementa un filtro de "ruido" manual basado en patrones de caracteres para asegurar la integridad de los datos.

2. Modelo con IA (Enfoque NLP)

- Metodología: Utiliza la librería spaCy (Procesamiento de Lenguaje Natural) para el entendimiento lingüístico.

- Fortalezas: Entiende el contexto. Maneja la Lematización (agrupar palabras como "corriendo" y "corrió" en su raíz "correr"), filtra Stopwords (palabras de relleno) e identifica entidades.

- Ideal para: Análisis de sentimiento, detección de fraudes y extracción de valor en datos no estructurados de negocio.

- Característica Clave: Filtrado de alta precisión que distingue entre vocabulario real y caracteres aleatorios (basura o gibberish).

| Característica | Lógica Determinista | Modelo IA (NLP) |
|----------------|---------------------|-----------------|
| Conocimiento del Lenguaje | No (Usa patrones) | Sí (Modelos lingüísticos) |
| Lematización | No (Coincidencia exacta) | Sí (Análisis de raíz) |
| Filtrado de Ruido | Básico (Caracteres especiales) | Avanzado (Semántica y Contexto) |
| Consumo de Recursos | Ultra-ligero | Dependiente del modelo |

## Cómo Ejecutarlo

1. Clona el repositorio.

1. Instala las dependencias para la versión de IA: pip install spacy y python -m spacy download es_core_news_sm.

1. Ejecuta logic_counter.py para la versión rápida.

1. Ejecuta ai_counter.py para la versión inteligente.

## Tecnologías Usadas

Lenguaje: Python 3.x

Librerías Clave: re (Regex), string, spacy (Modelo: es_core_news_sm)

Entornos: Linux / Windows / MacOS
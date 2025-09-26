# Proyecto de Analítica y Aprendizaje por Reforzamiento

Este repositorio contiene una **plantilla estructurada** para análisis de datos productivos, exploración de ROI, generación de datos sintéticos y experimentos con **aprendizaje por reforzamiento (RL)**.  
La idea es mantener un flujo claro desde **ingesta → limpieza → análisis exploratorio → augment → modelado → exportación**.

---

## 📂 Estructura del repositorio

data/
├── raw/ # dataset original
├── processed/ # dataset limpio y transformado
notebooks/
├── EDA_basico.ipynb # Análisis exploratorio inicial
└── Baseline_basico.ipynb # Entrenamiento de baselines (Dummy + kNN)
src/
├── ingesta.py # script de ingesta
├── preprocesamiento.py # script de preprocesamiento
└── modelo_baseline.py # script con modelo Dummy + kNN
logs/ # archivos de logging y métricas
slides/ # presentaciones de resultados
README.md
pyproject.toml
poetry.lock / requirements.txt
.gitignore

---

## 👥 Autor
- **Bruno Alejandro Donayre Donayre** – [brunodonayredonayre@gmail.com] 

---

## 📊 Dataset
- **Fuente:** Conjunto de datos consolidado para investigación aplicada en sistemas productivos  
- **Registros:** más de 7 mil observaciones entre 2020 y 2025  
- **Variables:** productivas, económicas, ambientales y nutricionales (todas normalizadas y estandarizadas para análisis estadístico y de machine learning)  


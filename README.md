# Proyecto de Analítica y Aprendizaje por Reforzamiento

Este repositorio contiene una **plantilla estructurada** para análisis de datos productivos, exploración de ROI, generación de datos sintéticos y experimentos con **aprendizaje por reforzamiento (RL)**.  
La idea es mantener un flujo claro desde **ingesta → limpieza → análisis exploratorio → augment → modelado → exportación**.


---

## 👥 Autor
- **Bruno Alejandro Donayre Donayre** – [brunodonayredonayre@gmail.com] 

---

## 📊 Dataset
- **Fuente:** Conjunto de datos consolidado para investigación aplicada en sistemas productivos  
- **Registros:** más de 7 mil observaciones entre 2020 y 2025  
- **Variables:** productivas, económicas, ambientales y nutricionales (todas normalizadas y estandarizadas para análisis estadístico y de machine learning)  

---

## 📂 Estructura del repositorio

```

notebooks/
├── Test.ipynb # Análisis exploratorio inicial y entrenamiento

logs/ # archivos de logging y métricas
slides/ # presentaciones de resultados
README.md
pyproject.toml
poetry.lock / requirements.txt
.gitignore
```

---

##⚙️ Requisitos

## 📦 Requirements

Este proyecto usa las siguientes dependencias principales:
```
- numpy  
- pandas  
- matplotlib  
- seaborn  
- scipy  
- scikit-learn (`sklearn`)  
- torch  
- stable-baselines3  
- gym  
- boruta  
- pyngrok  
- google  
```
Además de librerías estándar de Python:  
`os`, `json`, `random`, `collections`, `ast`.

👉 Puedes instalarlas con:
```
pip install -r requirements.txt
```

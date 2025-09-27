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

data/
 ├─ processed/                        # datasets limpios y transformados
 │   ├─ df_cruzado.xlsx               # dataset cruzado base
 │   ├─ df_cruzado_roi_filtrado.xlsx  # dataset cruzado filtrado por ROI
 │   ├─ df_imputado_cruzado.xlsx      # dataset cruzado con imputación
 │   └─ df_ruido.xlsx                 # dataset con ruido

notebooks/
 ├─ Test.ipynb                        # análisis exploratorio inicial y entrenamiento (EDA + GAN + RL/Q-Learning)

logs/                                 # archivos de logging y métricas
slides/                               # presentaciones de resultados

outputs/                              # resultados y salidas del modelado
 ├─ KS_comparacion_modelos.png        # comparación gráfica de modelos (curvas KS / métricas)
 ├─ datos_sinteticos_todas_las_semanas.xlsx  # dataset sintético generado con GAN/WGAN
 ├─ ks_results_por_semana.xlsx        # métricas KS calculadas por semana
 ├─ policy_completa_con_rangos.csv    # política derivada con rangos
 ├─ policy_optima.csv                 # política óptima aprendida
 ├─ policy_optima_con_rangos.csv      # política óptima con valores por rango
 ├─ policy_optima_legible.csv         # versión legible de la política óptima
 ├─ policy_optima_traducida.csv       # política óptima traducida (formato más interpretable)
 ├─ q_table_optima.json               # Q-table en formato JSON
 └─ q_table_optima.pkl                # Q-table en formato pickle (Python)

README.md
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



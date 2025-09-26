# Proyecto de Analítica y Aprendizaje por Reforzamiento en CEAs

Este repositorio contiene una **plantilla estructurada** para análisis de datos productivos, exploración de ROI, generación de datos sintéticos y experimentos con **aprendizaje por reforzamiento (RL)**.  
La idea es mantener un flujo claro desde **ingesta → limpieza → análisis exploratorio → augment → modelado → exportación**.

---

## 📂 Estructura del repositorio

├── .github/workflows/python-ci.yml # CI: lint + tests
├── .gitignore # Archivos ignorados (data, outputs, etc.)
├── .gitattributes # Configuración para Git LFS
├── .pre-commit-config.yaml # Hooks automáticos (black, ruff, codespell)
├── requirements.txt # Dependencias pip
├── environment.yml # Dependencias conda
├── README.md # Este archivo
├── LICENSE # MIT License
├── notebooks/
│ └── Plantilla_Estudio.ipynb # Notebook principal de análisis
├── src/project/
│ ├── init.py
│ ├── data_utils.py # Funciones para cargar/guardar datos
│ └── eda.py # Funciones básicas de EDA
├── data/
│ ├── raw/ # Datos crudos (ignorado en Git)
│ └── processed/ # Datos procesados (ignorado en Git)
├── outputs/
│ └── .gitkeep # Resultados (gráficos, tablas)
├── docs/ # Documentación extendida
└── tests/
└── test_smoke.py # Test mínimo

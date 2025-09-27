# simulador.py

import streamlit as st
import pandas as pd
import joblib
import os

# Ruta base (ajústala si no usas Colab)
ruta_base = "/content/drive/MyDrive/UNI/tercer ciclo/2.Proyecto_investigacion/Clase_13"

# Cargar la política óptima
#politica_path = os.path.join(ruta_base, "politica_optima.pkl")
try:
    policy_df =  pd.read_csv("/content/drive/MyDrive/UNI/tercer ciclo/2.Proyecto_investigacion/Clase_13/policy_completa_con_rangos.csv")
except Exception as e:
    st.error(f"Error al cargar política: {e}")
    st.stop()

# Encabezado
st.title("Recomendador de Perfil Nutricional Óptimo")
st.markdown("Ajusta tus condiciones ambientales y obtén la mejor acción recomendada para maximizar el ROI, IC y Sobrevivencia.")

# Entrada de usuario
o2 = st.slider("Oxígeno (O2_am)", min_value=3.0, max_value=8.0, step=0.1, value=5.5)
ph = st.slider("pH", min_value=6.5, max_value=9.0, step=0.1, value=7.8)
t_am = st.slider("Temperatura (T_am)", min_value=20.0, max_value=34.0, step=0.5, value=28.0)

# Binning (usa las mismas reglas que en entrenamiento)
def discretizar_estado(o2, ph, t):
    o2_bin = pd.cut([o2], bins=[0, 4.5, 5.5, 7, 10], labels=["muy_bajo", "bajo", "medio", "alto"])[0]
    ph_bin = pd.cut([ph], bins=[0, 6.5, 7.5, 8.5, 10], labels=["ácido", "lig_acido", "neutro", "básico"])[0]
    t_bin = pd.cut([t], bins=[0, 24, 27, 30, 35], labels=["baja", "media", "óptima", "alta"])[0]
    return f"{o2_bin}_{ph_bin}_{t_bin}"

estado_input = discretizar_estado(o2, ph, t_am)

# Mostrar acción recomendada
if estado_input in policy_df['Estado'].values:
    fila = policy_df[policy_df['Estado'] == estado_input].iloc[0]
    st.success("✅ Acción recomendada:")
    st.markdown(f"- **TA (%)**: {fila['TA_bin']}")
    st.markdown(f"- **TC (%)**: {fila['TC_bin']}")
    st.markdown(f"- **Alimento (kg/ha)**: {fila['Alimento_bin']}")
else:
    st.warning("⚠️ Se propone mayor intrenamiento.")

# Mostrar política completa si el usuario quiere
if st.checkbox("📄 Mostrar toda la política"):
    st.dataframe(policy_df)

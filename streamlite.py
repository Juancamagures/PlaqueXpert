import streamlit as st
from apps.placas.main import run_app as run_placas

st.set_page_config(
    page_title="Reconocimiento de Placas",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

run_placas()
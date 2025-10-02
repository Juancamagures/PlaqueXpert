import cv2
import streamlit as st
import numpy as np
import requests
from apps.placas.utils.analizador_placa import AnalizadorDePlacas
import json

analizador_de_placas = AnalizadorDePlacas()

def run_app():
    st.header('🚘 Reconocimiento de Placas de Vehículos')
    st.subheader('Puedes usar cámara o cargar una imagen de prueba')

    option = st.radio(
        "📷 Selecciona el método de entrada",
        ["Captura con cámara", "Subir imagen desde archivo"]
    )

    img = None

    # --- Captura desde cámara ---
    if option == "Captura con cámara":
        if st.button("📸 Capturar imagen desde la cámara"):
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cap.release()

            if ret:
                img = frame.copy()
            else:
                st.error("❌ No se pudo capturar imagen desde la cámara")

    # --- Subir archivo ---
    elif option == "Subir imagen desde archivo":
        uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, 1)  # Carga con OpenCV (BGR)

    # --- Procesamiento ---
    if img is not None:
        resultado = analizador_de_placas.procesar_imagen(img)

        placa = resultado["placa"]
        imagenplaca = resultado["imagenplaca"]
        imagenContornos = resultado["imagenContornos"]
        resultadosOCR = resultado["resultadosOCR"]
        bfilter = resultado["bfilter"]
        edged = resultado["edged"]
        output_array = resultado["output_array"]

        c1, c2 = st.columns(2)
        c1.subheader("🔬 Proceso")
        c2.subheader("✅ Resultado")

        with c1:
            c3, c4 = st.columns(2)
            c3.write("Imagen original")
            c3.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            c4.write("Imagen con fondo eliminado")
            c4.image(cv2.cvtColor(output_array, cv2.COLOR_BGR2RGB))
            c3.write("Imagen en escala de grises")
            c3.image(cv2.cvtColor(bfilter, cv2.COLOR_BGR2RGB))
            c4.write("Imagen con bordes")
            c4.image(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

        if placa and placa != "NO DETECTADA":
            c1.write("Imagen con la placa detectada")

            if imagenContornos is not None:
                c1.image(imagenContornos)

            with c2:
                c3, c4 = st.columns([5, 2])
                c4.write("Placa procesada")
                if imagenplaca is not None:
                    c4.image(imagenplaca)
                c4.metric("Placa", placa)

                try:
                    url = "http://localhost:8000/placas/api/vehiculos/"
                    params = {"placa": placa}
                    response = requests.get(url, params = params)

                    if response.status_code == 200:
                        data = response.json()
                        st.success(f"✅ Datos del vehículo encontrados:\n{json.dumps(data[0], indent=4)}")
                    else:
                        st.error(f"❌ Error al guardar vehículo: {response.text}")

                except Exception as e:
                    st.error(f"❌ Error al conectar con el backend: {str(e)}")


            c2.write("Textos detectados con OCR")
            c2.dataframe(resultadosOCR, use_container_width=True)

        else:
            c2.error("No se ha encontrado placas de vehículos en la imagen")
            if resultadosOCR:
                c2.write("🔎 Textos detectados con OCR")
                c2.dataframe(resultadosOCR, use_container_width=True)
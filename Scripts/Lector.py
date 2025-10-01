import requests
import streamlit as st
import cv2
import numpy as np
import easyocr
import imutils
import rembg
from PIL import Image
import os
from datetime import datetime

st.set_page_config(
    page_title="Reconocimiento de placas de vehículos",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

def obtenerPlaca(location, img, gray):
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    imagenContornos = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]
    imagenplaca = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    reader = easyocr.Reader(['es'])
    result = reader.readtext(cropped_image)
    placa = result[0][-2] if result else None
    return placa, imagenplaca, imagenContornos

def enviar_a_backend(placa):
    url = "http://127.0.0.1:8000/placas/registrar_placa/"  # tu endpoint de Django
    data = {"placa": placa}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()  # devuelve la respuesta del backend
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

st.header('Reconocimiento de placas de Vehículos por Cámara')
st.subheader('Versión adaptada con entrada desde la cámara web')

# Botón para capturar imagen
capturar = st.button("Capturar imagen desde la cámara")

if capturar:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        img = frame.copy()
        c1, c2 = st.columns(2)
        output_array = rembg.remove(img)
        output_image = Image.fromarray(output_array)

        c1.subheader("Proceso")
        c2.subheader("Resultado")

        with c1:
            c3, c4 = st.columns(2)
            c3.write("Imagen capturada")
            c3.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            c4.write("Imagen con fondo eliminado")
            c4.image(cv2.cvtColor(output_array, cv2.COLOR_BGR2RGB))

            gray = cv2.cvtColor(output_array, cv2.COLOR_BGR2GRAY)
            bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
            c3.write("Imagen en escala de grises")
            c3.image(cv2.cvtColor(bfilter, cv2.COLOR_BGR2RGB))

            reader = easyocr.Reader(['es'])
            result = reader.readtext(gray)
            resultadosOCR = [x[1] for x in result if len(x[1]) > 4]

            if resultadosOCR:
                placa_detectada = resultadosOCR[0].upper().strip()
                placa_detectada = placa_detectada.replace(" ", "")
                st.write("🚗 Placa detectada:", placa_detectada)
                resultado_backend = enviar_a_backend(placa_detectada)
                st.write("📋 Respuesta del backend:")
                st.json(resultado_backend)
            else:
                st.error("No se detectó ninguna placa en la imagen")



            edged = cv2.Canny(bfilter, 30, 200)
            c4.write("Imagen con bordes")
            c4.image(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

        # Contornos
        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        location = None
        placa = None

        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                placa, imagenplaca, imagenContornos = obtenerPlaca(location, img, gray)
                if placa and len(placa) > 5:
                    break

        # ✅ Si no se encontró placa por contornos, usar primer resultado OCR
        if not placa and resultadosOCR:
            placa = resultadosOCR[0]
            imagenplaca = gray  # alternativa: output_array
            imagenContornos = output_array

        if placa:
            c1.write("Imagen con la placa detectada")
            c1.image(imagenContornos)
            with c2:
                c3, c4 = st.columns([5, 2])
                c4.write("Placa procesada")
                c4.image(imagenplaca)
                text = placa
                # Dibujar rectángulo solo si se tiene location (por contornos)
                if location is not None:
                    res = cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0, 255, 0), 3)
                else:
                    res = img
                c4.metric("Placa", text)
                c3.image(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

                # 🟩 Guardar la placa en archivo txt
                carpeta = "C:\\PlaqueXpert"
                os.makedirs(carpeta, exist_ok=True)
                nombre_archivo = f"placa_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
                ruta_archivo = os.path.join(carpeta, nombre_archivo)
                with open(ruta_archivo, "w") as f:
                    f.write(text)

            c2.write("Textos detectados con OCR")
            c2.dataframe(resultadosOCR, use_container_width=True)
        else:
            c2.error("No se ha encontrado placas de vehículos en la imagen")
            c2.write("Textos detectados con OCR")
            c2.dataframe(resultadosOCR, use_container_width=True)
    else:
        st.error("No se pudo capturar imagen desde la cámara")

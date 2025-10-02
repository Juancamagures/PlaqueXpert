import cv2
import numpy as np
import easyocr
import imutils
import rembg

class AnalizadorDePlacas:
    def __init__(self):
        # Se inicializa solo una vez (más rápido)
        self.reader = easyocr.Reader(['es'])

    def obtenerPlaca(self, location, img, gray):
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0, 255, -1)
        new_image = cv2.bitwise_and(img, img, mask=mask)
        imagenContornos = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)

        (x, y) = np.where(mask == 255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))

        cropped_image = gray[x1:x2+1, y1:y2+1]
        imagenplaca = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

        result = self.reader.readtext(cropped_image)
        placa = result[0][-2] if result else None
        return placa, imagenplaca, imagenContornos

    def procesar_imagen(self, img):
        """
        Procesa una imagen para detectar placa y OCR
        """
        # Quitar fondo
        output_array = rembg.remove(img)
        gray = cv2.cvtColor(output_array, cv2.COLOR_BGR2GRAY)
        bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(bfilter, 30, 200)

        # OCR directo
        result = self.reader.readtext(gray)
        resultadosOCR = [x[1] for x in result if len(x[1]) > 4]

        # Contornos
        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        location, placa, imagenplaca, imagenContornos = None, None, None, None

        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                placa, imagenplaca, imagenContornos = self.obtenerPlaca(location, img, gray)
                if placa and len(placa) > 5:
                    break

        # Fallback OCR
        if not placa and resultadosOCR:
            placa = resultadosOCR[0].upper().strip().replace(" ", "")
            imagenplaca = gray
            imagenContornos = output_array

        if not placa:
            placa = "NO DETECTADA"

        return {
            "placa": placa,
            "imagenplaca": imagenplaca,
            "imagenContornos": imagenContornos,
            "resultadosOCR": resultadosOCR,
            "bfilter": bfilter,
            "edged": edged,
            "output_array": output_array
        }
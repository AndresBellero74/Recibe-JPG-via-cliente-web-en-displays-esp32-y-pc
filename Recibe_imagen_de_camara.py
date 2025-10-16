import requests
import cv2
import numpy as np
import time

# 📸 URL de la imagen
url = "http://192.168.0.250/photo.jpg"

while True:
    try:
        # 🔁 Descargar imagen
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            if frame is not None:
                # 🖼 Mostrar imagen
                cv2.imshow("ESP32-CAM Stream", frame)
            else:
                print("⚠️ Error al decodificar imagen")

        else:
            print(f"❌ Error HTTP: {response.status_code}")

    except Exception as e:
        print(f"❌ Error de conexión: {e}")

    # ⏱ Esperar 1 segundo
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

# 🧹 Limpiar
cv2.destroyAllWindows()
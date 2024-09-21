import cv2
from deepface import DeepFace
import os
import logging 

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')

def Recon(foto):
    webcam = cv2.VideoCapture(0)
    modelo = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

    ret, frame = webcam.read()
    if not ret:
        logging.warning("Câmera não encontrada")
        return {"error": "Câmera não encontrada"}

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = modelo.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        temp_face_path = "temp_face.jpg"
        cv2.imwrite(temp_face_path, face)
        logging.info(f"Salvando imagem {temp_face_path}")

        verificar = DeepFace.verify(img1_path=temp_face_path, img2_path=os.path.join("uploads", foto))
        os.remove(temp_face_path)

        return verificar
    
    webcam.release()
    cv2.destroyAllWindows()
    
    return {"error": "Nenhuma face detectada"}

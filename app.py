from fastapi import FastAPI, File, UploadFile
from src.backend.recon import Recon
from src.backend.genai import googleai
from src.backend.voice import falar
import os

app = FastAPI(
    title="API Reconhecimento Facial",
    version="1.0",
    description="Esta API de reconhecimento facial permite verificar se uma foto carregada é a mesma que a capturada pela webcam. Ela utiliza algoritmos avançados de reconhecimento facial para comparar e autenticar imagens."
)

@app.post("/upload-imagem")
async def upload_imagem(file: UploadFile = File(...)):
    os.makedirs('uploads', exist_ok=True)

    file_path = f'uploads/{file.filename}'
    with open(file_path, 'wb') as f:
        f.write(await file.read())
    
    rec = Recon(file.filename)

    prompt = f"Faz um relatório da verificação da imagem que eu fiz com opencv e deepface com base a essa informação: {rec}"
    report = googleai(prompt)

    falar()

    return rec

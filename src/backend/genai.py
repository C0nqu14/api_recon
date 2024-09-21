import google.generativeai as genai

def googleai(prompt):
    chave = "AIzaSyDt73YD_Cov48NIfDXXSUhAUIsfd_Fg-RA"
    genai.configure(api_key=chave)

    modelo = genai.GenerativeModel("gemini-1.0-pro")
    chat = modelo.start_chat(history=[])

    with open("voice.txt", 'w') as arquivo:
        arquivo.write(prompt)

    resposta = chat.send_message(prompt)
    return resposta.txt

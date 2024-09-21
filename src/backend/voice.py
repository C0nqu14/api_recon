import gtts
import pygame
import os

def falar():
    pygame.init()

    with open("voice.txt", 'r') as f:
        for linha in f:
            file = gtts.gTTS(linha.strip(), lang="pt-br")
            file.save("voice.mp3")

    if os.path.exists('voice.mp3'):
        pygame.mixer.music.load('voice.mp3')
        pygame.mixer.music.play()
        input("Pressione Enter para continuar...")
    
    pygame.quit()
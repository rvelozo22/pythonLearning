import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\renat\Downloads\Kendrick Lamar - N95.mp3')
pygame.mixer.music.play()

input('Pressione enter para parar a música.')
pygame.mixer.music.stop()

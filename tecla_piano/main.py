import pygame
import random

notas = {"nota1": 'notas/nota_do1.mp3', "nota2": "notas/nota_do2.mp3", "nota3": "notas/nota_fa1.mp3", "nota4": "notas/nota_la1.mp3", "nota5": "notas/nota_mi1.mp3", "nota6": "notas/nota_si1.mp3", "nota7": "notas/nota_si2.mp3", "nota8": "notas/nota_si3.mp3", "nota9": "notas/nota_sol1.mp3"}
nomes_notas = {"nota1": 'Nota Dó Menor', "nota2": "Nota Dó Maior", "nota3": "Nota Fá", "nota4": "Nota Lá", "nota5": "Nota Mi", "nota6": "Nota Sí Menor", "nota7": "Nota sí Média", "nota8": "Nota Sí Maior", "nota9": "Nota Sol"}
pygame.init()
pygame.mixer.init()
def tocar():
   pygame.mixer.music.play()
   
traco = '='*25
print(f'{traco} COMANDOS {traco}')
print(f'OBS: letras maiúsculas ou minúsculas não diferem!')
print(f'Digite PLAY ou P para tocar a nota novamente.\nDigite QUIT ou Q para desligar o programa.')
print(f'Para usar o programa, basta digitar NOTA e o número da nota, como por exemplo, 1 para Dó Menor.')
while True:
    nota_aleatoria = random.choice(list(notas.keys()))
    nota_do = pygame.mixer.music.load(notas[nota_aleatoria])
    pygame.mixer.music.set_volume(0.7)
    tocar()
    print(f'{traco} Adivinhe a nota! {traco}')
    for nota in nomes_notas.items():
       print(f'{nota[0]}: {nota[1]}')
    resposta = input("\nAdivinhe a nota: ").lower()
    
    if resposta == 'play' or resposta == 'p':
       tocar()
       while resposta == 'play' or resposta == 'p':
          tocar()
          resposta = input("\nAdivinhe a nota: ").lower()
    if resposta == nota_aleatoria:
        print(f'\nVocê acertou! a resposta era {nomes_notas[nota_aleatoria]}.')
        continue
    elif resposta == 'quit' or resposta == 'q':
       break
    elif resposta in notas.keys() != nota_aleatoria:
      print(f'\nVocê errou! a resposta era {nomes_notas[nota_aleatoria]}.')
      continue
    else:
       print('\nDigite corretamente!')
     

pygame.quit()
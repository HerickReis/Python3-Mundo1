'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador. 
-O programa deverá escrever na tela se o usúario venceu ou perdeu.'''

from time import sleep # a biblioteca sleep possui funções de temporizadores para o script
from random import randint 
import playsound
n = randint(0 ,5) # o randint irá escolher um número aleatório entre 0 e 5

adivinhacao = int(input('De 0 a 5 qual número voce acha que eu pensei? '))

print('\x1b[30m-=-'*20) #\x1b[30m está aplicando a cor preta ao resultado

print('\x1b[34mAnalisando...') #\x1b[34m está aplicando a cor azul

print('\x1b[30m-=-'*20) #\x1b[30m está aplicando a cor preta ao resultado

sleep(2) # o sleep está adicionando um temporizador de 2 segundos antes da proxima linha ser exibida

if adivinhacao == n: # se o usuário acertar o número que o computador escolheu ele irá ganhar e de brinde terá uma musiquinha :D

    print('\x1b[32mParabéns como você fez isso?\x1b[m ')

    playsound.playsound("fortestourado.mp3")

else: # se o usuário errar o número que o computador escolheu ele irá perder e terá uma musiquinha triste :(
    print(f'\x1b[31mPoxa infelizmente você perdeu o número sorteado foi {n}\x1b[m')
    playsound.playsound("trist3.mp3")

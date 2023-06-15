'''Faça um programa que leia um ângulo qualquer 
e mostre na tela o valor do seno, cosseno e tangente desse ângulo. '''
from math import sin, tan, cos,radians
a = int(input('Qual valor do ângulo? '))
sen = sin(radians(a)) #Projeção do ângulo em pé |
co = cos(radians(a))  #Projeção do ângulo deitado --
ta=tan (radians(a)) 
print(f'O seno de {a}° graus é {sen:.2f}\nO cosseno de {a}° é {co:.2f}\nE a tangente é {ta:.2f} .')
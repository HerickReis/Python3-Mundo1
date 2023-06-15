'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''
from math import hypot
co = float(input('Qual a medida do cateto oposto ? '))
ca = float(input('Qual a medida do cateto adjacente? '))
tan = hypot(co,ca)
print(f'a soma do quadrado dos catetos é : \n{co} Cateto Oposto\n{ca} Cateto Adjacente\nResulta na Tangente de valor: {tan:.3f}')

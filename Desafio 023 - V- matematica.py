'''Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos digitos separados
Ex: 
Digite um número:1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 4'''
n = int(input('Digite um número inteiro positivo: '))
print('Unidade',n %10 )
print('Dezena ',(n//10)%10)
print('Centena',(n//100)%10)
print('Milhar',(n//1000)%10)
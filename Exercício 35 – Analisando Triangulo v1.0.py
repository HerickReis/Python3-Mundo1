'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
a = float(input('Informe o lado "A" do triângulo: '))
b = float(input('Informe o lado "B" do triângulo: '))
c = float(input('Informe o lado "C" do triângulo: '))
if a < b+c and b < a+c and c < a+b:
    print('É um triângulo :D')
else:
    print('Não é um triângulo D:')
'''Escreva um programa que leia a velocidade de um carro. -Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado. 
-A multa vai custar R$7,00 por cada Km acima do limite'''
from time import sleep
carro = int(input('Quantos kilometros está seu carro ? ')) # está pedindo ao usuário que diga a velocidade de seu carro
if not carro :
    print ('\x1b[33mPor favor digite um valor válido !')
    exit()
print('\x1b[33mAnalisando...')
sleep(2)
if carro <= 80 :   # se a velocidade do carro for menor ou igual a 80 exibir a mensagem do print.
    print('\x1b[m32 você está no limite da via :)')

else :    # caso contrário exibir a mensagem abaixo.

    print('\x1b[1;34mO valor da multa é de 7 Reais por km excedido')

    print(f'\x1b[1;31mVocê foi multado em R$: {(carro -80) * 7}') # se o carro ultrapassar o limite de 80km/s o valor de 80 será subtraido, e o que restar, será multiplicado por 7.
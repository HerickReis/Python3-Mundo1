nome = input('Qual seu nome ?: ')
print (f'Olá {nome:-^10} Seja bem vindo ao programa Dobro,triplo e raiz quadrada')
nmr = float(input('Digite um número: '))
print(f'o dobro de {nmr} é {float(nmr)*2:.3} e o triplo é {float(nmr)*3:.4}', end='--> ')
print (f'e a raiz de {nmr} é {float(nmr)**(1/2):.4}')
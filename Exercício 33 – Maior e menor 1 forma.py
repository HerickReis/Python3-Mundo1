''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
'''nmrs = int(input('Digite o primeiro número: '))'''

def maior(n1,n2,n3) : # def é uma palavra chave para definir um função.
    # def está transformando a palavra maior na função maior() que está recebendo os valores n1, n2 e n3.
    
    max = n1 # aqui a variável max está recebendo o valor n1.

    if n2 > max : # se n2 for maior que o valor definido em max ele se tornará o novo valor da variável.
        max = n2

    if n3 > max: # se n3 for maior que o valor anterior da variável max ele se tornará o novo valor va variável.
        max = n3
    return max # return está retornando o valor da variável max.

def menor(n1,n2,n3) :
    # a função menor está recebendo três valores n1, n2 ,n3.

    min = n1 # a variável min está recevendo o valor n1.

    if n2 < min: # se o valor de n2 for menor que min então n2 se tornará o novo valor de min.
        min = n2

    if n3 < min: # se o valor de n3 for menor que min então n3 se tornará o novo valor de min.
        min = n3
    return min # return etá retornando o valor da variável min.

def menu(): # a palavra def está defininfo menu como uma função, que está recebendo o valor das variáveis de entrada n1, n2 ,n3.
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))   # os valores de n1, n2, n3 estão sendo alocados em menu().
    n3 = int(input('Digite o terceiro número: '))

    print('O maior número é: ', maior(n1,n2,n3)) # aqui o print irá exibir os valores dfinidos da função maior.
    print('O menor núemro é: ', menor(n1,n2,n3)) # aqui o print irá exibir os valores definidos da função menor.

menu() # menu irá ser exibido 
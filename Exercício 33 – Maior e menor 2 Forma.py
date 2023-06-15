n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))     # as variáveis n1,n2,n3 está pedindo ao usuário que escreva três valores inteiros.
n3 = int(input('Digite o teceiro número: '))

lista = [n1,n2,n3] # variável lista está com três valores em colchetes que são n1, n2, n3.

print(f'O menor valor é {min(lista)}') # a função min() está mostrando o menor valor da lista.

print(f'O maior valor é {max(lista)}') # a função max() está mostrando o maior valor da lista.

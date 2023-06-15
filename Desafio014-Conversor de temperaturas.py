nome = input('Qual seu nome ? ')

print(f'Olá {nome:-^10}seja bem vindo ao nosso programa de conversão de temperaturas',end='--')
celsius = float(input('Qual a temperatura em C° ? '))

fahrenheit = (celsius * 9/5) + 32
print(f'{nome}, {celsius}C° equivalem a {fahrenheit:.2f}F°')

if celsius >25 :
 print(f'Uau {nome} está relativamente quente em sua cidade O_O')

else :
 print(f'{nome} até que a temperatura está bem tranquila :)')
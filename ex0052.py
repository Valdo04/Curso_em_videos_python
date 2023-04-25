# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
########################################################################################

numero = int(input('Digite o numero: '))

if numero / 1 == numero and numero / numero == 1:
    print(f'O {numero} é um numero primo')
else:
    print(f'O {numero} numero não é um numero primo')
# Desenvolva um programa que leia o primenro termo e a razão de um PA. no final, mostre 
# os 10 primeiros termos dessa progressão.
###################################################################################################3

lista = []
n1= int(input('Digite o primeiro termo:  '))
n3 = int(input('Digite a PA a ultilizar:  '))

for i in range(n1,10, n3 ):
    lista.append(i)


    print(lista[0])
    resultado = (lista[:10])
    print(resultado)
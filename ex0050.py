# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor valor digitado for ímpar desconsidere-o.
##########################################################################################

num_par1 = []

for numeros in range(0 , 6 ):
    num_par = int(input('Digite os numeors'))
    if num_par % 2 == 0:
        num_par1.append(num_par)
resultado = sum(num_par1)

print(num_par1)
print(resultado)


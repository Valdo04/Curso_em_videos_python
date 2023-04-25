# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos 
# de três e que encontram no intervalo de 1 até 500.
################################################################################

soma = 0
for numeros in range(3 , 500, 3):
    soma += numeros
       
    print(numeros)
print(soma)
    

# Refaça o desafio 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.
##################################################################################################33


n1= int(input('Digite o primeiro termo:  '))
n2 = int(input('Razão:  '))
n3 = n1 + (10 -1) * n2
n = 1
r = range(n1, n3 + n2, n2 )
while n != 5: 
   print(f'{r}', end=' -> ')
   print('FIM')

   n += 1
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F"
# Caso esteja errado, peça a digitação novamente até um valor correto.

##############################################################################################3

sexo = 'f'
sexo1 = 'm'
while sexo != 'f' and sexo1 != 'm:':
  sexo = str(input('Digite seu sexo: ')).strip().lower()
  if sexo == sexo or sexo1 == sexo1:
    print('Valido')

  else:
    print('Digite novamente')
 
print(sexo)


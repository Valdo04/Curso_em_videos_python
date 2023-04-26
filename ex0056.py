# Desenvolva um programa que leia nome, idade sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.
#####################################################################################################
lt_masc = {}
soma = 0
maior = 0
for p in range(1, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade:'))
    sexo = int(input('''Digite seu sexo:
    [ 1 ] Masculino:
    [ 2 ] Feminino:
    :'''))
    if sexo == 1:
        lt_masc[nome] = idade
        
     #soma += idade / 4
homem_mais_velho = max(lt_masc, key=lambda k: lt_masc[k])
lt_masc = max(nome)
#print(f'A média de idade do grupo é {soma}')
print(lt_masc[homem_mais_velho])

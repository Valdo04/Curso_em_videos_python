<<<<<<< HEAD
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$ 1000
# c) Qual o nome do produto mais barato.
#########################################################################################

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if repr == 'N':
        break
    print('{:-^40}'.format('FIM DO PROGRAMA'))
    print(f'O total da compra foi R$ {total:.2f}')
    print(f'Temos {totmil} produtos custando mais de R$ 1000,00')
    print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
    
=======
valor_saque = int(input("Digite o valor que deseja sacar: "))

notas_50 = notas_20 = notas_10 = notas_5 = notas_1 = 0

while valor_saque > 0:
    if valor_saque >= 50:
        valor_saque -= 50
        notas_50 += 1
    elif valor_saque >= 20:
        valor_saque -= 20
        notas_20 += 1
    elif valor_saque >= 10:
        valor_saque -= 10
        notas_10 += 1
    elif valor_saque >= 5:
        valor_saque -= 5
        notas_5 += 1
    elif valor_saque >= 1:
        valor_saque -= 1
        notas_1 += 1

print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 1: {notas_1}")
>>>>>>> d8537b9773c3244a60325916fb56e71db99b11ed

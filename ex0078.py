# Faça um progama que leia 5 valores numericos e guarde-os em uma lista.
#No final, mostre qual foi o maior eo menor valor digitado e as suas respectivas posições na lista.
#########################################################################################################
num = list()
max = 0
min = 0

for n in range(5):
    num.append(int(input('Digite um numero: ')))
    for c, v in enumerate(num):
        if v > max:
            max = v
            min = v
            if v < min :
                min = v
        

print(max)
print(min)



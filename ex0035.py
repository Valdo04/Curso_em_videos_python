print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro seguimento'))
r2 = float(input('Segundo seguimento'))
r3 = float(input('Terceiro Seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos NÃO PODEM FORMAR triângulo!')
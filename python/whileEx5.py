num = int(input('Digite um numero: '))

fatorial = 1
i = 1
while(i <= num):
    fatorial *= i
    i += 1
print('O fatorial de', num, 'é', fatorial)
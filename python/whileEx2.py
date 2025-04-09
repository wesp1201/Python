num = int(input('Digite um numero de 1 a 10: '))

mult = 1

while(mult <= 10):
    if(num <= 10):
        print(f'{num} x {mult} = {num * mult}')
    else:
        print('Valor nao correspondente de 1 a 10')
        break
    mult += 1
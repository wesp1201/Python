import math

def main ():
    a_digitacao = float(input('Digite o valor de a: '))
    b_digitacao = float(input('Digite o valor de b: '))
    c_digitacao = float(input('Digite o valor de c: '))
    imprime_raizes = (a_digitacao, b_digitacao, c_digitacao)

def delta (a, b ,c):
    print (b ** 2 - 4 * a * c)

def imprime_raizes (a, b, c):
    d = delta (a, b, c)
    if (d == 0):
        raiz1 = (- b + math.sqrt(d) / (2 * a) )
        print('A unica raiz é: ', raiz1)
    elif(d < 0):
        print('esta equaçao nao possui raizes reais')
    else:
        raiz1 = (- b + math.sqrt(d) / (2 * a) )
        raiz2 = (- b - math.sqrt(d) / (2 * a) )
        print('A primeira raiz é: ', raiz1)
        print('A segunda raiz é: ', raiz2)
        
main()      
 

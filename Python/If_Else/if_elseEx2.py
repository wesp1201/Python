a = True
b = True
c = False
d = 10

if (a == True):
    d = d + 1
else:
    if(b == True):
        if(c == False):
            d = d + 2
        else:
            d = d + 3
            d = d * 4
    d = d + 4
d = d + 5
print('O valor da variável D é:', d)
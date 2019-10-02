lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impar = 0
par = 0

for numero in range(lista):
    if(numero % 2 == 0):
        par += 1
    else:
        impar += 1

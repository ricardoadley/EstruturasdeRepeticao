## Como imprimir matriz de forma "bonitinha" usando for
matriz =  [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
]

for line in matriz:
    str_linha = ''
    for column in line:
        str_linha += '{:>3}'.format(str(column))

    print(str_linha)



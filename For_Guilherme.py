# Imprime elementos de uma lista separados por espaços

lista = [1, 2, 3, 4, 5]

saida = ''
for i in range(len(lista)):
    if i == len(lista) - 1:
        saida += str(lista[i])
    else:
        saida += str(lista[i]) + ' '

print(saida)


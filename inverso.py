#Entrada
palavra = raw_input()

#Associação
palavra_inversa = ""
contador = 0

#Iterações
for i in range(len(palavra) -1, -1, -1):
    palavra_inversa += palavra[i]

for e in range(len(palavra)):
    if palavra[e] == palavra_inversa[e]:
        contador += 1

print "A palavra %s contém %i caractere(s) coincidente(s) com a sua inversa." %(palavra, contador)

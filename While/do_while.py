lista = []

while True:
	novo_valor = int(raw_input("novo valor: "))
	
	lista.append(novo_valor)
	
	if (novo_valor == 0):
		break
		
print lista

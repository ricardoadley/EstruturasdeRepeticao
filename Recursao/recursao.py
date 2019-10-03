def meu_for_recursivo(quantidade_que_vai_rodar, quantos_ja_rodou):
    if (quantidade_que_vai_rodar == quantos_ja_rodou): # Definição do caso base: Caso a quantidade de vezesq que eu rodei, for igual a quantidade que eu quero que meu código rode. A função não vai se invocar.
        print("Ja rodei " + str(quantos_ja_rodou)  + " e vou parar agora")
    else: 
        print("Rodei a minha vez " + str(quantos_ja_rodou))
        meu_for_recursivo(quantidade_que_vai_rodar, quantos_ja_rodou + 1) # Definindo a chamada da função em função dela mesmo.


meu_for_recursivo(10, 0)
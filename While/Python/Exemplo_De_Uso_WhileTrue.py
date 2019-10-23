while True:

    print("Calculadora")
    print("\n1) Adição")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")
    print("5) Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "5":
        break

    elif opcao == "1":

        n1 = float(input("\nDigite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        soma = n1 + n2
        print("\nResultado:", soma, "\n")

    elif opcao == "2":

        n1 = float(input("\nDigite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        subtracao = n1 - n2
        print("\nResultado:", subtracao, "\n")

    elif opcao == "3":

        n1 = float(input("\nDigite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        multiplicacao = n1 * n2
        print("\nResultado:", multiplicacao, "\n")

    elif opcao == "4":

        n1 = float(input("\nDigite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        divisao = n1 / n2
        print("\nResultado:", divisao, "\n")

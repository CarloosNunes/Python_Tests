executar = True

while executar:
    escolhas = ''' 
        [1] ou [+] para Somar
        [2] ou [-] para Subtrair
        [3] ou [/] para Dividir
        [4] ou [*] para Multiplicar
        [5] para Sair'''

    print(escolhas)
    operador = input("Qual sua opção?")

    n1 = int(input("Qual o primeiro Nº?"))
    n2 = int(input("Qual o segundo Nº?"))

    texto_sair = '''
        [1] Não, desejo sair!
        [2] Sim, desejo realizar outro calculo
    '''

    #Soma
    if operador == "1" or operador == "+" or operador == "Somar":
        resultado = n1+n2
        print(f"O resultado é {resultado}.")
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo?")
        if operador == "1":
            executar = False

    #Subtração
    if operador == "2" or operador == "-" or operador == "subtrarir":
        resultado = n1-n2
        print(f"O resultado é: {resultado}")
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo?")
        if operador == "1":
            executar = False
    #Divisão
    if operador == "3" or operador == "/" or "dividir":
        resultado = n1/n2
        print(f"O resultado é {resultado}.")
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo?")
        if operador == "1":
            executar = False
    #Multiplicação
    if operador == "4" or "*" or "multiplicar":
        resultado = n1*n2
        print(f"O resultado é {resultado}.")
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo?")
        if operador == "1":
            executar = False

    if operador == "5":
        executar = False

    #Sair
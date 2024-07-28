import base

def criaAFD():
    print("----> AFD <----\n")

    # o input recebe a entrada do usuario e armazena em estados e o split() formata a string
    estados = input("Informe os estados do AFD: ").split()
    alfabeto = input("\nInforme o alfabeto do AFD: ").split()
    estadoInicial = input("\n Informe o estado inicial do AFD: ")
    estadoFinal = input("\n Informe os estados finais do AFD: ").split()
    transicoes = {} #Inicializa um dicionário vazio para armazenar as transições

    print("\n Agora entre com as transições do seu AFD:\n")

    for estado in estados:
        for simbolo in alfabeto:
            proxEstados = input(f"Transições de {estado} com símbolo {simbolo} (separados por espaço): ").split()
            transicoes[(estado, simbolo)] = proxEstados


    AFD = base.automato(estados, alfabeto, transicoes, estadoInicial, [], estadoFinal)

    return(AFD)
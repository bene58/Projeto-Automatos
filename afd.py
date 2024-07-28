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
            print(f"\t{simbolo}")
            print(f"{estado}\t ---->\t",end="")#end="" aqui deixa sem adicionar uma nova linha no fim
            proxEstado = input("\n Informe o proximo estado: ").split()

        if proxEstado == 0:
            transicoes[(estado, simbolo)] = None
        else:
            #o automato é armazenado
            transicoes[(estado, simbolo)] = proxEstado


    AFD = base.automato(estados, alfabeto, transicoes, estadoInicial, [], estadoFinal)

    return(AFD)
import base

def criaAFN():
    print("----> AFN <----\n")

    # O input recebe a entrada do usuário e armazena em estados e o split() formata a string
    estados = input("Informe os estados do AFN: ").split()
    alfabeto = input("\nInforme o alfabeto do AFN: ").split()
    estadoInicial = input("\nInforme o estado inicial do AFN: ")
    estadosFinais = input("\nInforme os estados finais do AFN: ").split()
    transicoes = {}  # Inicializa um dicionário vazio para armazenar as transições

    print("\nAgora entre com as transições do seu AFN:\n")

    for estado in estados:
        for simbolo in alfabeto:
            proxEstados = input(f"Transições de {estado} com símbolo {simbolo} (separados por espaço): ").split()
            transicoes[(estado, simbolo)] = proxEstados

    AFN = base.automato(estados, alfabeto, transicoes, estadoInicial, [], estadosFinais)

    return AFN

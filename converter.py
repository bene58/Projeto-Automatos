from itertools import combinations as comb
import base

def AFNparaAFD(afn):
    combinacoes = []
    for i in range(1, len(afn.estados) + 1):
        combinacoes_temp = list(comb(afn.estados, i))
        combinacoes.extend(combinacoes_temp)

    delta = afn.transicoes
    alfabeto = afn.alfabeto
    finais = afn.finais
    tabelaDeTransicaoAFD = {}
    
    
    for combinacao in combinacoes:
        combinacao_str = " ".join(combinacao)
        for simbolo in alfabeto:
            listaAux2 = set()
            for elemento in combinacao:
                listaAux1 = delta.get((elemento, simbolo), set())
                listaAux2.update(listaAux1)
            listaAux2_str = " ".join(sorted(listaAux2))
            tabelaDeTransicaoAFD[(combinacao_str, simbolo)] = listaAux2_str
    
    estadosFinais = []
    for combinacao in combinacoes:
        combinacao_str = " ".join(combinacao)
        if any(elemento in finais for elemento in combinacao):
            estadosFinais.append(combinacao_str)

    estadosReduzidos = [afn.inicial]
    for estado, simbolo in tabelaDeTransicaoAFD.keys():
        estado_destino = tabelaDeTransicaoAFD[(estado, simbolo)]
        if estado_destino and estado_destino not in estadosReduzidos:
            estadosReduzidos.append(estado_destino)

    alcancaveis = []
    for estado in estadosReduzidos:
        if estado == afn.inicial:
            alcancaveis.append(estado)
            continue
        for estado_red in estadosReduzidos:
            for simbolo in alfabeto:
                if tabelaDeTransicaoAFD.get((estado_red, simbolo)) == estado:
                    if estado not in alcancaveis:
                        alcancaveis.append(estado)
                        break

    estadosReduzidos = alcancaveis

    finaisReduzidos = [estado for estado in estadosReduzidos if estado in estadosFinais]

    Reduzida_AFD = {}
    for estado in estadosReduzidos:
        for simbolo in alfabeto:
            aux = tabelaDeTransicaoAFD.get((estado, simbolo), "")
            Reduzida_AFD[(estado, simbolo)] = aux

    AFD = base.automato(estadosReduzidos, alfabeto, Reduzida_AFD, afn.inicial, [], finaisReduzidos)
    return AFD
    


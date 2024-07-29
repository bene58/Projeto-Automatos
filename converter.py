from itertools import combinations as comb # aqui gera todas as combinações possíveis de um determinado tamanho a partir de uma lista
import base

def AFNparaAFD(afn):
    combinacoes = []
    for i in range(1, len(afn.estados) + 1):#range gera uma sequencia de numeros q começam em start e terminam em stop
        combinacoes_temp = list(comb(afn.estados, i))#list faz uma lista com as combinações
        combinacoes.extend(combinacoes_temp)#extend ele concatena a temp com a atual

    delta = afn.transicoes#Armazena as transições do AFN
    alfabeto = afn.alfabeto
    finais = afn.finais
    tabelaDeTransicaoAFD = {}
    listaAux1=[]
    listaAux2=[]
    
    for combinacao in combinacoes:
        combinacao_str = " ".join(combinacao)#o join aqui é usado para concatenar com um espaço entre
        for simbolo in alfabeto:
            listaAux2 = set()# set() cria um novo conjunto
            for elemento in combinacao:
                listaAux1 = delta.get((elemento, simbolo), set())#get() retorna o valor associado a uma chave
                listaAux2.update(listaAux1)# Atualiza o conjunto auxiliar com os estados alcançáveis
            listaAux2_str = " ".join(sorted(listaAux2))#sorted() retorna a lista ordenada
            tabelaDeTransicaoAFD[(combinacao_str, simbolo)] = listaAux2_str

 #######################################   
    #a parte da estrelinha na tabela
    estadosFinais = []
    for combinacao in combinacoes:
        combinacao_str = " ".join(combinacao)
        if any(elemento in finais for elemento in combinacao):# any() verifica se existe pelo menos um elemento em uma sequência que satisfaça uma condição
            estadosFinais.append(combinacao_str)#append adiciona o elemento ao final da lista

 #########################################                   
    #tabela reduzida
    estadosReduzidos = [afn.inicial]
    
    #aqui itera sobre o par (estado, simbolo)
    for estado, simbolo in tabelaDeTransicaoAFD.keys():#keys() obtém uma lista de todas as chaves do dicionário
        estado_destino = tabelaDeTransicaoAFD[(estado, simbolo)]
        if estado_destino and estado_destino not in estadosReduzidos:#verifica se não esta vazio e se não esta na lista
            estadosReduzidos.append(estado_destino)

    alcancaveis = []
    for estado in estadosReduzidos:
        if estado == afn.inicial:
            alcancaveis.append(estado)
            continue # esse continue faz com que o loop avance para a próxima iteração
        for estado_red in estadosReduzidos:
            for simbolo in alfabeto:
                if tabelaDeTransicaoAFD.get((estado_red, simbolo)) == estado:
                    if estado not in alcancaveis:
                        alcancaveis.append(estado)
                        break
  
  #aqui ocorre uma atualização de estados Reduzidos para conter os alcançáveis também
    estadosReduzidos = alcancaveis

    #aqui remove estados que voltam para ele mesmo em todas as transições
    estadosReduzidos = [
        estado for estado in estadosReduzidos
        #len retorna o número de elementos
        if len(set(tabelaDeTransicaoAFD.get((estado, simbolo), "") for simbolo in alfabeto)) > 1
        #se for 1 isso significa que todas as transições retornam ao mesmo estado
    ]

    finaisReduzidos = [estado for estado in estadosReduzidos if estado in estadosFinais]#verifica cada estado se esta em finais e se sim é incluido em reduzidos

    Reduzida_AFD = {}
    for estado in estadosReduzidos:
        for simbolo in alfabeto:
            aux = tabelaDeTransicaoAFD.get((estado, simbolo), "")#retorna "" se a chave não for encontrada
            Reduzida_AFD[(estado, simbolo)] = aux

    AFD = base.automato(estadosReduzidos, alfabeto, Reduzida_AFD, afn.inicial, [], finaisReduzidos)
    return AFD
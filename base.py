import networkx as nx
import matplotlib.pyplot as plt

class automato:
    # __init__ é a maneira de se definir um construtor
    def __init__(self, estados, alfabeto, transicoes, inicial, conjuntoAceito, finais):
        self.estados = estados  # é usado para referenciar a instância atual da classe e diferenciar a instancia do parâmetro
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial
        self.conjuntoAceito = conjuntoAceito
        self.finais = finais

    

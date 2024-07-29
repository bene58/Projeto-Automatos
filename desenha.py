from graphviz import Digraph
import random
import os #permite que você realize tarefas como manipulação de arquivos e diretórios

def desenha_automato(aut):
    desenho = Digraph()  # Definindo que a var desenho é do tipo Digraph()
    desenho.attr(rankdir='LR')  # LR significa da esquerda para direita
    desenho.attr('node', shape='circle')  # Definindo os atributos do node (nós)
    
    desenho.node('->', shape='none', width='0', height='0', label='')
    desenho.edge('->', aut.inicial)
    
    for estado_final in aut.finais:
        desenho.node(estado_final, shape='doublecircle', fontsize='15', fontcolor='red')  # Colocando círculo duplo em todos os estados finais
    
    for estado in aut.estados:
        for simbolo in aut.alfabeto:
            destinos = aut.transicoes.get((estado, simbolo), [])
            if not isinstance(destinos, list):
                destinos = [destinos]
            for destino in destinos:
                desenho.edge(estado, destino, label=simbolo)
    
    aleatorio = round((random.random()) * 10, 2)  # Define um número aleatório para nome da imagem gerada
    aleatorio = str(aleatorio).replace(".", "")  # Converte para string e remove pontos
    
    os.makedirs('imagens', exist_ok=True)  # Confere se a pasta imagens existe
    caminho = os.path.join('imagens', 'aut' + aleatorio)  # Cria o caminho para onde o arquivo deve ir e define o nome do arquivo como aut+aleatorio
    
    res = desenho.render(caminho, format='png', cleanup=True)  # Gera a imagem e salva no caminho

    if res:  # Retorno para o usuário da criação da imagem
        print(f"Imagem {('aut' + aleatorio)} gerada com sucesso")
    else:
        print("Erro ao gerar imagem")


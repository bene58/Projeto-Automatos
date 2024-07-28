import afd
import afn
import converter
import desenha
from  base import automato




automatofd=afd.criaAFD()
#automatofd=converter.AFNparaAFD(automatofd)

print("\n")

#print(F"\nAlfabeto: {automatofn.alfabeto}\nEstados: {automatofn.estados}\nEstado Inicial: {automatofn.inicial}\nEstado(s) Final(is): {automatofn.finais}\nTransicoes: {automatofn.transicoes}\nConjunto Aceitacao: {automatofn.conjuntoAceito}\n")

#automatofn.desenhar(nome_arquivo='automato_afn.jpeg')
desenha.desenha_automato(automatofd)
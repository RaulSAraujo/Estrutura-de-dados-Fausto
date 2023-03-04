"""
    ALGORITIMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando dois elementos adjacentes sempre que o segundo
    for MENOR que o primeiro. Efetua tantas passadas quanto
    necessárias, até que, na última passada, nenhuma troca
    seja efetuada

    VERSÃO OTIMIZADA COM ENCOLHIMENTO DO PERCURSO A CADA PASSADA
"""
# Variáveis de estatistica
import sys
from data.nomes_desord import nomes
from time import time
comps = trocas = passadas = 0


def bubble_sort2(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0

    desloc = 1

    # Loop eterno, não sabemos quantas passadas serão necessarias
    while True:
        trocou = False
        passadas += 1

        # Percurso da lista, do primeiro ao PENÚLTIMO
        # elemento, com acesso a cada posição
        for pos in range(len(lista) - desloc):

            comps += 1

            # Se o numero que esta á frente na lista
            # for MENOR do que o que está atrás, TROCA
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True
                trocas += 1

        if not trocou:      # Não houve troca na passada
            break           # Interrompe o loop eterno; acabou

        # Aumenta o deslocamento para diminuir o tamanho da proxima passada
        desloc += 1

###########################################################################


# Teste com um vetor de 10 numeros
nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7]
bubble_sort2(nums)
print("Lista ordenada:", nums)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

pior_caso = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubble_sort2(pior_caso)
print("Lista ordenada (pior caso): ", pior_caso)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

############################################################################

sys.dont_write_bytecode = True

hora_ini = time()
bubble_sort2(nomes)
hora_fim = time()
print("Nomes ordenados: ", nomes)
print(f'Tempo gasto: {round((hora_fim - hora_ini) * 1000, 2)}ms')
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")
print('\n', '-' * 80, '\n', sep='')

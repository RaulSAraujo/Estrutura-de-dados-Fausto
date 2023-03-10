# Lista de números
nums = [9, 21, 33, 12, 0, 18, 24, 30, 15, 6, 3, 27]

"""
    Função que realiza uma busca sequencial em uma lista procurando por val.
    Se val for encontrado, retorna a posição de val.
    Caso contrário, retorna o valor -1
"""


def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]:
            return pos
    # Percorreu toda a lista e não encontrou val: retorna -1
    return -1


# Procurando o valor 15
resultado = busca_sequencial(nums, 15)
print(f"Posição do valor 15 na lista: {resultado}")

# Procurando o valor 20
resultado = busca_sequencial(nums, 20)
print(f"Posição do valor 15 na lista: {resultado}")

# Procurando o valor 33
resultado = busca_sequencial(nums, 33)
print(f"Posição do valor 15 na lista: {resultado}")

from data.nomes_desord import nomes

#Busca pelo nome FAUSTO
resultado = busca_sequencial(nomes, "FAUSTO")
print(f"Posição do nome FAUSTO na lista: {resultado}")





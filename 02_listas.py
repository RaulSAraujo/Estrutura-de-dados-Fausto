# LISTAS EM PYTHON
# Listas são uma forma de armazenar mais de um valor em uma única variável
# Os valores podem ser de tipos diferentes

# Uma lista de números
valores = [2, 3, 5, 7, 9, 11, 'batata', 'tomate', True]


# OPERAÇÕES SOBRE LISTAS
# 1) PERCURSO: significa percorrer a lista do primeiro até o último elemento, fazendo algo com cada um deles.
#   No caso, a seguir, vamos exibir cada um dos elementos separadamente usando print()
for v in valores:
    print(v)

print('\n', '*' * 80, sep='') # Imprime * 80 vezes


# 2) INSERÇÃO DE UM NOVO ELEMENTO NO *FIM* DA LISTA: append()
valores.append('cebola')
print(valores)
valores.append(29)
print(valores)

print('\n', '-' * 80, sep='') # Imprime - 80 vezes


# 3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1º: índice para inserir
#    2º: valor a ser inserido
valores.insert(4, 'chuchu') # Inserindo 'chuchu' no índice 4
print(valores)

valores.insert(0, 'abobrinha') # Inserindo 'abobrinha' na primeira posição
print(valores)

print('\n', '-' * 80, sep='')


# 4) ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECÍFICA
print('Elemento na SÉTIMA posição:', valores[6])
print('Elemento na TERCEIRA posição:', valores[2])
print('Elemento na PRIMEIRA posição:', valores[0])
print('Elemento na ÚLTIMA posição:', valores[-1])
print('Elemento na PENÚLTIMA posição:', valores[-2])

print('\n', '-' * 80, sep='')


# 5) SUBSTITUINDO VALORES EXISTENTES
print('Antes:', valores)
valores[10] = 'cenoura'     # Substituindo o valor da posição 10 (11º elemento)
valores[0] = 'beterraba'    # Substituindo o valor da posição 0 (1º elemento)
valores[-1] = 'alho'        # Substituindo o valor da última posição
print('Depois:', valores)

print('\n', '-' * 80, sep='')

# 6) DETERMINANDO QUANTOS ELEMENTOS HÁ NA LISTA: len()
print("Numero de elementos na lista: ", len(valores))

# Imprimindo o ultimo elemento da lista com a ajuda de len()
print("Ultimo valor da lista:", valores[len(valores) - 1])

print("\n",'-' * 80, sep='')

# 7) REMOVENDO O ULTIMO ELEMENTO DA LISTA: pop()
print("Antes:", valores)
ultimo = valores.pop()
print("Valor removido da lista:",ultimo)
print("Depois:",valores)

print('\n', '-' * 80, sep='')

# 8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parametro
print("Antes",valores)
pos9 = valores.pop(9)
print("Valor removido da posição 9:", pos9)
pos0 = valores.pop(0)
print("Depois:", valores)

print('\n', '-' * 80, sep='')

# 9) REMOVENDO UM ELEMENTO PELO SEU VALOR: remove()
print("Antes:",valores)
valores.remove("batata")
valores.remove(5)
print("Depois>",valores)

print('\n', '-' * 80,sep='')

# Acrescentando mais alguns elementos na lista
valores.append(13)
valores.append(15)
valores.append('milho')
valores.append(17)
valores.append('mandioca')
valores.append(19)


# 10) FATIANDO UMA LISTA
print(valores)

# Cria uma sublista que contém os elementos de 1 até
# a posição 7 (posição 8 NÃO ENTRA)
sublista_7 = valores[1:8]
print("Sublista de 1 a 7:", sublista_7)

# Cria uma sublista que contem os elementos do inicio até a posição 5 (posição 6 NÃO ENTRA)
sublista0_5 = valores[:6]

#Cria uma sublista que contem os elementos da posição 10 até o fim da lista
sublista10_fim = valores[10:]
print('Sublista de 10 até o final:', sublista10_fim)


# range(): função que gera uma faixa de números
# É muito usada em associação com listas

# range() com 1 parâmetro: gera uma faixa que vai
# de 0 (zero) até o valor do parâmetro - 1

for x in range(10):
    print(x)

print("-" * 80)

# range() com 2 parâmetros: gera uma lista começando pelo
# primeiro paramentro (inclusive) até o segundo argumento
# (exclusive, NÃO ENTRA)

for y in range(5,12):
    print(y)

# Range com 3 parâmentros:
# 1: limite inferior (inclusive)
# 2: limite superior (EXCLUSIVE)
# 3: passo (de quanto em quanto a lista vai saltar: PODE SER NEGATIVO)
for z in range(0,22,3): # De 0 a 21 saltando de 3 em 3 
    print(z)

# Range() com passo negativo
for k in range(10,0,-1): #Contagem regressiva de 10 até 1
    print(k)

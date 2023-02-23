# range() com 2 parâmetros: gera uma lista começando pelo
# primeiro paramentro (inclusive) até o segundo argumento
# (exclusive, NÃO ENTRA)

for y in range(5, 12):
    print(y)

# Range com 3 parâmentros:
# 1: limite inferior (inclusive)
# 2: limite superior (EXCLUSIVE)
# 3: passo (de quanto em quanto a lista vai saltar: PODE SER NEGATIVO)
for z in range(0, 22, 3):  # De 0 a 21 saltando de 3 em 3
    print(z)

# Range() com passo negativo
for k in range(10, 0, -1):  # Contagem regressiva de 10 até 1
    print(k)

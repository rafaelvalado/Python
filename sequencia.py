# for
# iterando sobre string
nome = 'rafael'
for letra in nome:
    print(letra)

# iterando sobre lista
lista = [1, 3, 5, 7]
for numero in lista:
    print(numero)

# iterando sobre sequência
for numero in range(0, 10):
    print(numero)

# método enumerate(): cria tuplas com índice de cada elemento
nome = 'Filipe'
for indice in enumerate(nome):
    print(indice)

for indice in enumerate(nome):
    print(indice[0]) # imprime o índice dos elemento

for indice in enumerate(nome):
    print(indice[1]) # imprime o elemento

# while
""" while expressão booleana:
    // execuçao do loop """
# o bloco do while será repetido enquanto a expressão booleana for True.
# ex01
numero = 1
while numero < 10:
    print(numero)
    numero += 1

#saindo de loops com break
 
# ex01
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)

# ex02
while True:
    comando = input('Digite "sair" para sair ')
    if comando == 'sair':
        break

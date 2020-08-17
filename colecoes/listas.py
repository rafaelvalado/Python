"""
>- Listas em python funcionam como vetores/matrizes (arrays) em outras 
liguagens, com a diferença de serem DINÂMICO e também podermos colocar QUALQUER 
tipo de dado.

Em python
- Dinâmico: não possuem tamanho fixo: ou seja, podemos criar a lista e
simplesmente ir adicionando elementos.
- Qualquer tipo de dado: não possuem tipo de dado fixo: ou seja, podemos colocar
qualquer tipo de dado, até mesmo dados misturados.

- As listas são representadas por [ ]
- listas são mutáveis: ou seja, elas podem mudar constatemente.
"""
# podemos facilmente checar se determinado valor está contido na lista
 
lista4 = list(range(11))
 
lista5 = list('Rafael silva')
 
print(4 in lista4)
print('j' in lista5)


# podemos facilmente ordenar uma lista usando a função sort().
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
lista1.sort()
print(lista1)
 
lista2 = list('mlnsaphedgrfjio')
lista2.sort()
print(lista2)

# podemos facilmente contar o numero de ocorrência de um valor.
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
lista2 = ['R', 'a', 'f', 'a', 'e', 'l', ' ', 's', 'i', 'l', 'v', 'a']
 
# com números
num = 17
print(lista1)
print(lista1.count(num))
 
# com strings
print(lista2)
print(lista2.count('a'))

# podemos adicionar elementos em uma lista
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
# Para adicionar elementos em listas, usamos a função append(), extend() e insert().
 
print(lista1)
 
lista1.append(69)
print(lista1)
 
# obs: com append só podemos adicionar um elemento por vez 
# lista1.append(1, 2, 3) # ERRO
 
lista1.append([1, 3, 5]) # coloca uma lista como elemento único em outra lista
print(lista1)
 
lista1.append('Rafael')
print(lista1)
 
if [1, 3, 5] in lista1:
    print('Lista encontrada')
else:
    print('Lista não encontrada')
 
# obs: com extend só podemos adcionar valores iterávéis, não aceita valor único
 
lista1.extend([7, 9, 11])# põe os elementos de um dado dentro de uma lista
print(lista1)
 
lista1.extend('Rafael')
print(lista1)
 
# podemos também adicionar um elemento novo na lista, informando o índice
 
lista1.insert(13, 'Silva')
print(lista1)

# podemos juntar duas listas
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
lista2 = ['R', 'a', 'f', 'a', 'e', 'l', ' ', 's', 'i', 'l', 'v', 'a']
 
lista1 = lista1 + lista2
print(lista1)
 
# ou
 
lista1.extend(lista2)
print(lista1)

# podemos inverter uma lista
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
lista2 = ['R', 'a', 'f', 'a', 'e', 'l', ' ', 's', 'i', 'l', 'v', 'a']
 
# forma 1
 
lista1.reverse()
lista2.reverse()
 
print(lista1)
print(lista2)
 
# forma 2
 
print(lista1[::-1])
print(lista2[::-1])

 
# podemos copiar uma lista
 
# deep copy 
# OBS: caso o valor de uma lista for alterado, não irá interferir na outra lista
 
lista = [2, 4, 6, 8, 10]
nova = lista.copy()
print(lista)
print(nova)
 
lista.append(12)
print(nova)
print(lista)
 
# shallow copy
# OBS: caso o valor de uma lista for alterado, irá interferir na outa lista
 
lista = [2, 4, 6, 8, 10]
nova = lista
print(lista)
print(nova)
 
nova.append(12)
print(nova)
print(lista)

# podemos contar quantos elementos exite dentro da lista usando len()
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
print(len(lista1))

# podemos remover o último elemento de uma lista usando o pop()
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
print(lista1)
lista1.pop()
print(lista1)

# podemos remover um elemento pelo índice
# OBS: os elementos a direita desse ídice serão removidos para esquerda
# OBS: se o índice informado não existir dará erro
 
lista1 = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
print(lista1)
lista1.pop(2)
print(lista1)

# podemos repetir elementos em uma lista
 
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# podemos converter uma string para uma lista
 
# ex01 usando split
 
curso = 'Programação em python: essêncial'
print(curso)
 
curso = curso.split()
print(curso)
 
# OBS: por padrão, o split separda os elementos da lista pelo espaço entre elas
# daí podemos escolher o tipo de separador dentro do parênteses
 
# ex02
 
curso = 'Programação_em_python:_essêncial'
print(curso)
 
curso = curso.split('_')
print(curso)

# podemos converter uma lista em uma string
 
# 'separador'.join(lista)
# podemos escolher o separador entre ''
 
lista = ['Programação', 'em', 'python:', 'essêncial']
print(lista)
 
# ex01
 
curso = ' '.join(lista)
print(curso)
 
# ex02
 
curso = '_'.join(lista)
print(curso)
 
# ex03
 
curso = '$'.join(lista)
print(curso)

# iterando sobre uma lista
 
# ex01 utilizando for
 
lista = [1, 3, 51, 17, 78, 12, 3, 10, 17, 33]
 
soma = 0
 
for elemento in lista:
    print(elemento)
    soma += elemento
print(f'soma = {soma}')
 
# ex02 utlizando while
 
carrinho = []
 
while produto != 'sair':
    print("Adicione produtos no carrinho ou digite 'sair' para sair" )
    produto = input()
    
    if produto != 'sair':
        carrinho.append(produto)
 
for produto in carrinho:
    print(produto)
print(carrinho)

# utilizando variáveis em listas 

num1 = 1
num2 = 3
num3 = 5
num4 = 7
num5 = 9
num6 = 11

numeros = [num1, num2, num3, num4, num5, num6]
print(numeros)

# fazemos acesso aos elementos de froma idexada

# ex01

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# fazemos acesso aos elementos de forma idexada inversa

# ex02

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde

# fazemos acesso aos elementos de froma idexada

# ex01

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# fazemos acesso aos elementos de forma idexada inversa

# ex02

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde

# usando um loop

# ex01

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0 
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1










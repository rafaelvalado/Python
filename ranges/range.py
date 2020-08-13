# Ranges
""" Ranges são utilizados para gerar sequências numéricas, não de forma aleatória mas sim de maneira especificada. """
 
# formas gerais:
 
# froma 01 - range(valor_de_parada); obs: valor_de_parada não inclusivo(início padrão 0, e passo de 1 em 1)
# ex01
 
for num in range(11):
    print(num)

# froma 02 - range(valor_de_início, valor_de_parada); obs-: valor_de_parada não inclusivo-(início_dado_pelo_usuário, passo 1 em 1).
# ex02
 
for num in range(2, 11):
    print(num)

# forma 04 - range(final, parada, passo); obs: parada não inclusivo(início_dado_pelo_usuário, passo_pelo_usuário)
# ex04
 
for num in range(10, -1, -1): # (-1) -> decrementação; faz uma contagem regressiva. Nesse caso,só ocorre o loop s
    print(num)

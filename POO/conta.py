from collections import named tuple
# criando uma classe simples usando namedtuple
Cliente = namedtuple('Cliente', 'nome sobrenome cpf')

class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        self._numero = numero
        self._titular = Cliente()
        self._saldo = saldo
        self._limite = limite

    
    def depositar(self, valor):
        if valor < 0:
            return False
        else:
            self._saldo += valor

    
    def sacar(self, valor):
        if valor < self._saldo:
            return False
        else:
           self._saldo -= valor



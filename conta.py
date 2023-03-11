"""Conta: classe que representa uma conta bancária, com informações como número da conta, nome do titular, saldo etc.
    Banco: classe que representa um banco, com informações como nome do banco, lista de contas etc."""

class Conta():
    def __init__(self, numero, titular, saldo): # construtor
        self.numero = numero 
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor): # método
        self.saldo += valor 
    
    def sacar(self, valor): # método
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
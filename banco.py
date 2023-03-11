from conta import Conta # importa a classe Conta do arquivo conta.py

class Banco():
    def __init__(self, nome): # construtor
        self.nome = nome
        self.contas = []

    def criar_conta(self, numero, titular, saldo = 0):
        conta = Conta(numero, titular, saldo)
        self.contas.append(conta) # adiciona a conta criada na lista de contas do banco

    def buscar_conta(self):

        numero = float(input("Digite o numero da conta: \n")) 
        for conta in self.contas: # percorre a lista de contas do banco
            if conta.numero == numero:# se o número da conta for igual ao número digitado pelo usuário
                print("Conta encontrada!\n")
                return conta 
        
        print("Conta não encontrada!\n") 
        return None # retorna None(que é um valor especial que indica que não há valor)

    def transferir(self, valor, conta_origem, conta_destino):
        
        # primeiro temos que verificar se a conta de origem e de destino existem
        if conta_origem in self.contas and conta_destino in self.contas:
            # agora precisamos verificar se a conta de origem possui saldo suficiente
            if conta_origem.saldo >= valor:
                conta_origem.saldo -= valor
                conta_destino.saldo += valor
                print("Transferência realizada com sucesso!\n")
            else:
                print("Saldo insuficiente!\n")
        else:
            print("Conta de origem ou conta de destino não existem!\n")
    

    def removerConta(self, conta): # método para remover uma conta
        for cadaConta in self.contas: # percorre a lista de contas do banco
            if cadaConta == conta: # se a conta for igual a conta passada como parâmetro
                self.contas.remove(cadaConta) # remove a conta da lista de contas do banco
                print("Conta removida!\n")
                return
        print("Conta não encontrada!\n")


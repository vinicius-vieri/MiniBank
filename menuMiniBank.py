from banco import Banco # importa a classe Banco

minibank = Banco("MiniBank") # nosso banco

# boas vindas
print("################### Bem vindo ao miniBank ###################\n")
print("Escolha uma opção:\n")
print(">>>> 1 - Criar conta\n")
print(">>>> 2 - Buscar conta\n")
print(">>>> 3 - Depositar\n")
print(">>>> 4 - Sacar\n")
print(">>>> 5 - Transferir entre contas\n")
print(">>>> 6 - Remover conta\n")
print(">>>> 7 - Sair\n")

opcao = int(input("Digite a opção desejada: "))

while opcao != 7: # loop para escolher as opções do menu
    if opcao == 1:
        numero = float(input("Digite o numero da conta: "))
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo inicial: "))
        minibank.criar_conta(numero, titular, saldo)

    elif opcao == 2:
        conta = minibank.buscar_conta()
        if(conta): # se a conta existir
            print("Número da conta: ", conta.numero)
            print("\n")
            print("Titular da conta: ", conta.titular)
            print("\n")
            print("Saldo da conta: ", conta.saldo)
            print("\n")

    elif opcao == 3:
        conta = minibank.buscar_conta()
        valor = float(input("Digite o valor a ser depositado: \n"))
        conta.depositar(valor)
        print("Valor depositado!\n")

    elif opcao == 4: 
        conta = minibank.buscar_conta()
        valor = float(input("Digite o valor a ser sacado: \n"))
        conta.sacar(valor)
        print("Valor sacado!\n")

    elif opcao == 5:
        print("Digite as informações da conta de origem:\n")
        conta_origem = minibank.buscar_conta()
        print("Digite as informações da conta de destino:\n")
        conta_destino =  minibank.buscar_conta()
        valor = float(input("Digite o valor a ser transferido: \n"))
        minibank.transferir(valor, conta_origem, conta_destino)

    elif opcao == 6:
        contaApagar = minibank.buscar_conta() 
        minibank.removerConta(contaApagar)  

    else:
        print("Opção inválida")

    print("Escolha uma opção:\n")
    print(">>>> 1 - Criar conta\n")
    print(">>>> 2 - Buscar conta\n")
    print(">>>> 3 - Depositar\n")
    print(">>>> 4 - Sacar\n")
    print(">>>> 5 - Transferir entre contas\n")
    print(">>>> 6 - Remover conta\n")
    print(">>>> 7 - Sair\n")
    opcao = int(input("Digite a opção desejada: "))

print("\nObrigado por utilizar o miniBank!")
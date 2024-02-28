from cliente import Cliente
from conta import Conta

def exibir_menu():
    print("------BANCO-------\n"
          "(1) - Criar conta\n"
          "(2) - Listar contas\n"
          "(3) - Sacar\n"
          "(4) - Depositar\n"
          "(5) - Sair")

list_cliente =[]

while True:
    exibir_menu()
    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")
        while True:
            if not any(cliente.cpf == cpf for cliente in list_cliente):
                break
            print("CPF Incorreto ou ja existente!")
            cpf = float(input("Insira seu CPF NOVAMENTE:"))
        saldo = float(input("Digite seu saldo inicial: "))
        cliente = Cliente(nome, cpf, idade)
        conta = Conta(cliente, saldo)
        cliente.conta = conta
        list_cliente.append(cliente)
        print("Cliente cadastrado com sucesso!\n")

    elif opcao == "2":
        print("Listagem de clientes:")
        if not list_cliente:
            print("Nenhum cliente cadastrado.\n")
        else:
            for cliente in list_cliente:
                print("------------------------------")
                print(f" CPF: {cliente.cpf}\n Nome: {cliente.nome}\n Idade:"
                      f" {cliente.idade}\n Saldo:{cliente.conta.saldo}")
                print("------------------------------")
    elif opcao == "3":
        cpf = input("Digite seu cpf: ")
        for cliente in list_cliente:
            if cliente.cpf == cpf:
                saque_inicial = float(input("Digite o valor: "))
                if cliente.conta is None:
                    print("Cliente não possui uma conta associada.")
                else:
                    cliente.conta.sacar(saque_inicial)
                    print("Saque efetuado com sucesso!")
                break
        else:
            print("-----------------------\n")
            print("Cliente não encontrado!\n")
            print("-----------------------")
    elif opcao == "4":
        cpf_desposito = input("Digite seu cpf: ")
        for cliente in list_cliente:
            if cliente.cpf == cpf_desposito:
                deposito = input("Valor do deposito: ")
                if cliente.conta is None:
                    print("Cliente não possui uma conta associada.")
                else:
                    cliente.conta.depositar(deposito)
                    print("Deposito feito com sucesso!")
                break
        else:
            print("-----------------------\n")
            print("Cliente não encontrado!\n")
            print("-----------------------")
    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.\n")

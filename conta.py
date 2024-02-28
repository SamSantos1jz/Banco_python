

class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = float(saldo)

    def sacar(self, saque):
        if saque > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= saque


    def depositar(self, deposito):
        deposito = float(deposito)
        self.saldo +=deposito



    def consultar_cliente(self):
        return self.cliente, self.saldo







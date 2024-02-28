import conta

class Cliente():

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = int(idade)

    def __str__(self):
        return "Nome: " + self.nome + "\ncpf: "+ str(self.cpf) + "\nIdade: "+ str(self.idade)


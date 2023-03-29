import json

with open("banco.json") as f:
    dados = json.load(f)


class Funcionario:
    def __init__(self,id,nome,cpf,salario,cargo):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._cargo = cargo

class Gerente(Funcionario):
    def __init__(self,id,nome,cpf,salario,cargo,login,senha):
        super().__init__(id,nome,cpf,salario,cargo,login,senha)
        self._login = login
        self._senha = senha
import json

with open("banco.json") as f:
    dados = json.load(f)


class Funcionario:
    def __init__(self,nome,salario,cpf,id,cargo):
        self._nome = nome
        self._salario = salario
        self._cpf = cpf
        self._id = id
        self._cargo = cargo

    def getCpf(self):
        return self._cpf
    def setCpf(self,cpf):
        self._cpf = cpf

    def getID(self):
        return self._id
    def setID(self,id):
        self._id = id

    def getCargo(self):
        return self._cargo
    def setCargo(self,cargo):
        self._cargo = cargo

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome

    def getSalario(self):
        return self._nome
    def setSalario(self,salario):
        self._salario = salario


        
class Gerente(Funcionario):
    def __init__(self, nome, salario,cpf,id,cargo,login,senha):
        super().__init__(nome, salario,cpf,id,cargo,login,senha)
        self._login = login
        self._senha = senha

    def getLogin(self):
        return self._login
    def setLogin(self,login):
        self._login = login

    def getSenha(self):
        return self._senha
    def setSenha(self,senha):
        self._senha = senha

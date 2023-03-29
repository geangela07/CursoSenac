class Empresa:
    def __init__(self,listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios
        self._funcionarioLogado = "Nenhum usuario logado"

    def getListaFuncionarios(self):
        return self._listaFuncionarios
    def setListaFuncionarios(self,listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios

    def getFuncionarioLogado(self):
        return self._funcionarioLogado
    def setFuncionarioLogado(self,funcionarioLogado):
        self._funcionarioLogado = funcionarioLogado

    def loginFuncionario(self,login,senha):
        for funcionario in self._listaFuncionarios:
            if funcionario.getCargo() == "Gerente":
                if funcionario.getLogin() == login:
                    if funcionario.getSenha() == senha:
                        self.setFuncionarioLogado(funcionario)
                        print(f"Logado como {self.getFuncionarioLogado().getNome()}")
                        break

    def imprimirFuncionarios(self):
        print("Metodo de impressão com contador")
        for i in range(len(self._listaFuncionarios)):
            print(f"{i+1} - {self._listaFuncionarios[i]._nome}")

        print("Metodo de impressão percorrendo lista")
        for func in self._listaFuncionarios:
            print(f"{func._id} - {func._nome}")

    def visualizarFuncionario(self,idFuncionario):
        for func in self._listaFuncionarios:
            if str(func.getID) == idFuncionario:
                func.mostrarInformações()
                return "Funcionario Encontrado"

        else:
            print("O ID não existe na lista de funcionarios")


            
        

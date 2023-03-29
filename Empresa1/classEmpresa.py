class Empresa:
    def __init__(self,listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios
        self._funcionariologado = "Nenhum usuario logado"

    def getListaFuncionarios(self):
        return self._listaFuncionarios
    def setListaFuncionarios(self,listaFuncionarios):
        self._listafuncionarios = listaFuncionarios

    def getFuncionarioLogado(self):
        return self._funcionarioLogado
    def setFuncionarioLogado(self,funcionarioLogado):
        self._funcionariologado = funcionarioLogado

    def loginFuncionario(self,login,senha):
        for funcionario in self._listadeFuncionarios:
            if funcionario.getCargo() == "Gerente":
                if funcionario.getLogin() == login:
                    if funcionario.getSenha() == senha:
                        self.setFuncionarioLogado(funcionario)
                        print(f"Logado como {self._funcionariologado.getNome()}")
                        break

    def imprimirFuncionarios(self):
        print(self._listaFuncionarios)
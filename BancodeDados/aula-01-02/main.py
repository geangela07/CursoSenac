from Controle.classConexao import Conexao
from Modelo.classfuncionario import Funcionario
import psycopg2

def mostrarFuncionarios(conexao):

    listaFuncionarios = conexao.consultarBanco('''
    SELECT * FROM "Funcionarios"
    ''')

   

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres","postgres") 
    
    funcionario = Funcionario(None,"Tales","05955150885","2060",idDepartamento="2")
    funcionario.imprimirFuncionario()
    con.manipularBanco(funcionario.inserirFuncionario("Funcionarios"))
    
    
    print(con.consultarBanco('''
    SELECT * FROM "Funcionarios"


    '''))

    con._db.close()

except (Exception,psycopg2.Error) as error:
    print("Ocorreu um erro:",error)


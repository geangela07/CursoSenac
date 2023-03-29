from Controle.classConexao import Conexao
import psycopg2
from Modelo.classOpcoes import Opcoes
from Modelo.classCandidato import Candidato
from Modelo.classAdministrador import Administrador




try:
    con = psycopg2.connect(database="Atendimento",host="localhost",port="5432",user="postgres",password="postgres")

except(Exception,psycopg2.Error) as error:
    print("Ocorreu um erro -",error)

while True:
    try:

        print('''
        1. Inserir Opções
        2. Atendimento
        3. Empresa
        0. Sair
        ''')
        opcoes = input("Escolha uma opção: ")

        match opcoes:

            case "1":
                Opcoes.inserirOpcoes(con)

            case "2":
                print('''
                1. Inserir Candidato
                2. Atualizar Candidato
                3. Excluir Candidato
                0. Sair
                ''')
                opcoesCandidato = input("Escolha uma opção: ")

                match opcoesCandidato:

                    case "1":
                        Candidato.inserirCandidato()
                    case "2":
                        Candidato.atualizarCandidato()
                    case "3":
                        Candidato.excluirCandidato()
                    case "0":
                        con.close()
                        break
                    case _:
                        print("Opção inválida")

                input("Tecle Enter para continuar")


            case "3":
                print('''
                1. Inserir Empresa
                2. Excluir Empresa
                3. Atualizar Empresa
                0. Sair
                ''')
                opcoesEmpresa = input("Escolha uma opção: ")

                match opcoesEmpresa:

                    case "1":
                        Administrador.inserirAdm()
                    case "2":
                        Administrador.excluirAdm()
                    case "3":
                        Administrador.atualizarAdm()
                    case "0":
                        con.close()
                        break
                    case _:
                        print("Opção inválida")
                input("Tecle Enter para continuar")


            case "0":
                con.close()
                break

            case _:
                print("Opção inválida")

        input("Tecle Enter para continuar")

    except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro",error)        
    
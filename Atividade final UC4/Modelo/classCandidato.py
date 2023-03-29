from Controle.classConexao import Conexao
import psycopg2

class Candidato:
    def __init__(self,nome,cpf,documento,telefone,profissao,email,resultado,motivo,escolaridade):
        self._nome = nome
        self._cpf = cpf
        self._documento = documento
        self._telefone = telefone
        self._profissao = profissao
        self._email = email
        self._resultado = resultado
        self._motivo = motivo
        self._escolaridade = escolaridade


    

    def inserirCandidato(self):
        sql = f'''
        INSERT INTO "Atendimento"
        VALUES(default, '{self._nome}', '{self._cpf}','{self._documento}','{self._telefone}','{self._profissao}','{self._email}','{self._resultado}',
        '{self._motivo}','{self._escolaridade}')
        '''
        return sql
    
    def atualizarCandidato():
        try:
            con = psycopg2.connect(database="Atendimento",host="localhost",port="5432",user="postgres",password="postgres")

        except(Exception,psycopg2.Error) as error:
            print("Ocorreu um erro -",error)



        cursor = con.cursor()
        novoCandidato = input("Digite o ID do Canditado que deseja atualizar: ")

        cursor.execute(f'''
        SELECT * FROM "Atendimento"
        WHERE "ID" = {novoCandidato}
        ''')
        print("Candidato escolhido: ")
        resultado = cursor.fetchone()
        print(f'''
            ID - {resultado[0]}
            Nome - {resultado[1]}
            CPF - {resultado[2]}
            Telefone - {resultado[4]}
            ''')
        
        cursor.close()

        cursor = con.cursor()

        novoNome = input("Insira o novo nome do Candidato:")
        novoCPF = input("Insira o novo cpf do Candidato:")

        cursor.execute(f'''
        UPDATE "Atendimento"
        SET "Nome" = '{novoNome}', "CPF" = '{novoCPF}'
        WHERE "ID" = '{novoCandidato}'
        ''')
        con.commit()

        cursor.close()

    def excluirCandidato():
        try:
            con = psycopg2.connect(database="Atendimento",host="localhost",port="5432",user="postgres",password="postgres")

        except(Exception,psycopg2.Error) as error:
            print("Ocorreu um erro -",error)

        cursor = con.cursor()
        apagarCandidato = input("Digite o Id do Candidato que deseja remover: ")

        cursor.execute(f''' 
        DELETE FROM "Atendimento"
        WHERE "ID" = {apagarCandidato}
        ''')

        
        con.commit()
        cursor.close()

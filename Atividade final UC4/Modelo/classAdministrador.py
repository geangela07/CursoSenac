from Controle.classConexao import Conexao
import psycopg2

class Administrador:
    def __init__(self,id,nome,cnpj,telefone,email,endereco):
        self._id = id
        self._nome = nome
        self._cnpj = cnpj
        self._telefone = telefone
        self._email = email
        self._endereco = endereco

    def inserirAdm(self):
        sql = f'''
        INSERT INTO "Empresa"
        VALUES(default, '{self._nome}', '{self._cnpj}','{self._telefone}','{self._email}',{self._endereco}
        )
        '''
        return sql 

    def excluirAdm(self):
        try:
            con = psycopg2.connect(database="Atendimento",host="localhost",port="5432",user="postgres",password="postgres")

        except(Exception,psycopg2.Error) as error:
            print("Ocorreu um erro -",error)

        cursor = con.cursor()
        apagarAdm = input("Digite o Id do Administrador que deseja remover: ")

        cursor.execute(f''' 
        DELETE FROM "Empresa"
        WHERE "ID" = {apagarAdm}
        ''')

        
        con.commit()
        cursor.close()

    def atualizarAdm(self):
        try:
            con = psycopg2.connect(database="Atendimento",host="localhost",port="5432",user="postgres",password="postgres")

        except(Exception,psycopg2.Error) as error:
            print("Ocorreu um erro -",error)



        cursor = con.cursor()
        novoAdm = input("Digite o ID do Empresa que deseja atualizar: ")

        cursor.execute(f'''
        SELECT * FROM "Empresa"
        WHERE "ID" = {novoAdm}
        ''')
        print("Empresa escolhido: ")
        resultado = cursor.fetchone()
        print(f'''
            ID - {resultado[0]}
            Nome - {resultado[1]}
            CNPJ - {resultado[2]}
            Telefone - {resultado[4]}
            ''')
        
        cursor.close()

        cursor = con.cursor()

        novoNome = input("Insira o novo nome da Empresa: ")
        novoCNPJ = input("Insira o novo cnpj da Empresa: ")

        cursor.execute(f'''
        UPDATE "Atendimento"
        SET "Nome" = '{novoNome}', "CNPJ" = '{novoCNPJ}'
        WHERE "ID" = '{novoAdm}'
        ''')
        con.commit()

        cursor.close()

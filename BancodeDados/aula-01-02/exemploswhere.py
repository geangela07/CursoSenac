if __name__=="__main__":
    import psycopg2
    from Controle.classConexao import Conexao

try:
    con = Conexao(parametroDb="Empresa", parametroHost="localhost", parametroPort="5432", parametroUser="postgres", parametroPassword="postgres")

    funcionarios = con.consultarBanco('''
    Select * FROM "Funcionarios"
    ORDER BY "ID" ASC

    ''')

    for funcionario in funcionarios:
        print(f'''
        {funcionario[0]} - {funcionario[1]} - {funcionario[2]} - {funcionario[3]} - {funcionario[4]}
        ''')


    funcionario = con.consultarBanco('''
    SELECT * FROM "Funcionarios"
    WHERE "ID" = 5;
    ''')

    print("Pesquisa por ID igual: ",funcionario)

    funcionario = con.consultarBanco(f'''
    SELECT * FROM "Funcionarios"
    WHERE "Nome" = 'Jonas';
    ''')

    print("Pesquisa por nome igual: ",funcionario)

    print("Pesquisa por salário maior:",con.consultarBanco(f'''
    SELECT * FROM "Funcionarios"
    WHERE "Salário" > '3000'
    ORDER BY "ID" ASC;
    '''))


    print("Pesquisa por Salário menor:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salário" < '5000'
        ORDER BY "ID" ASC; 
        '''))

    print("Pesquisa por nome Maior ou Igual:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" >= 'Jonas'
        ORDER BY "ID" ASC; 
        '''))



   


except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro",error)

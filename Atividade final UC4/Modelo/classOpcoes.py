class Opcoes:
    def __init__(self,ambiente,tipodeatendimento,tipodedocumento,tipodepessoa,atendente,tarefa,resultado,motivo,titulo):
        self._ambiente = ambiente
        self._tipodeatendimento = tipodeatendimento
        self._tipodedocumento = tipodedocumento
        self._tipodepessoa = tipodepessoa
        self._atendente = atendente
        self._tarefa = tarefa
        self._resultado = resultado
        self._motivo = motivo
        self._titulo = titulo

    def inserirOpcoes(self):
        sql = f'''
        INSERT INTO "Opcoes"
        VALUES ('{self._ambiente}', '{self._tipodeatendimento}','{self._tipodedocumento}','{self._tipodepessoa}',
        '{self._atendente}','{self._tarefa}',
        '{self._resultado}','{self._motivo}','{self._titulo}')
        '''    
        return sql
    
    def inserirOpcoes(con):
        cursor = con.cursor()
        ambiente = input("Insira o local de atendimento: ")
        tipodeatendimento = input("Insira o tipo de atendimento: ")
        tipodedocumento = input("Insira o tipo documento de identificação: ")
        tipodepessoa = input("Insira o tipo de pessoa(Fisica ou Jurídica): ")
        atendente = input("Insira o nome do atendente: ")
        tarefa = input("Insira a tarefa: ")
        resultado = input("Insira a conclusão: ")
        motivo = input("Insira o motivo do nao encaminhamento: ")
        titulo = input("Insira a vaga correspondente: ")

        cursor.execute(f'''
        INSERT INTO "Opcoes"
        VALUES ('{ambiente}', '{tipodeatendimento}','{tipodedocumento}',
        '{tipodepessoa}','{atendente}','{tarefa}','{resultado}','{motivo}','{titulo}')
        ''')

        con.commit()

        cursor.close()
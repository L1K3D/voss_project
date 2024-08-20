import pymssql

def conecta_banco_de_dados(servidor, usuario, senha, banco_de_dados, query):

    try:
        conn = pymssql.connect(server=servidor, user=usuario, password=senha, database=banco_de_dados)
        print("Conexao_Realizada_com_sucesso!")

        cursor = conn.cursor()

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

        cursor.close()

    except:
        print("Oi")
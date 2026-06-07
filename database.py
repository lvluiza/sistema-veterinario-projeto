import mysql.connector

def obtemConexao():
    if obtemConexao.conexao == None:
        obtemConexao.conexao = mysql.connector.connect(
            host="172.16.12.14",
            user="BD240226160",
            password="Narho10",
            database="vet_db"
        )

    return obtemConexao.conexao
obtemConexao.conexao = None




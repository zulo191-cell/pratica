import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host="localhost"
    user="root"
    password="452451"
    database="aula"
)

seletor=""

while seletor !=0:
    print("_______menu_______")
    print("1:Cadastro________")
    print("2:Consula Aluno___")
    print("3:Lista dos Alunos")
    print("0:_____sair_______")

    seletor = input("Selecione uma opção")

    if(seletor =="1"):

        cursor = conexao.cursor()

        print("\n____Cadastro Aluno____")
        nome=input("Qual o nome do aluno: ")
        sobrenome=input("Qual o sobrenome do aluno: ")
        data_nascimento= input("Qual a data de nascimento:(DD/MM/AAAA): ")

        data_nascimento_mysql =datetime.strptime(data_nascimento, "%d/%m/%y").strftime("%y/%m/%d")

        sql = "INSERT INTO aluno (nome_aluno, sobrenome_aluno, data_nascimento) Values (%s, %s, %s)"

        valores= (nome, sobrenome, data_nascimento_mysql)

        conexao.commit();

        print("\n Aluno cadastrado com sucesso!\n")
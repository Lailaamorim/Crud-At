#import mysql.connector
import sqlite3
import os
from time import sleep #o metodo sleep faz ele dormir, faz o computador esperar os segundos que estipulamos 
#antes de ele nos responder 

# import cadastroAlunoFuncoes.py

# Conexão com o Banco de Dados SQLite
db_connection = sqlite3.connect('cadastroAluno.db')

# Criação do cursor para interação com o BD
cursor = db_connection.cursor()

# Criar tabelas que serão utilizadas no código -- Só deve ser executado 1 vez
# cursor.execute('''CREATE TABLE aluno
#              (matricula text, nome text, curso text, turma text, np1 real, np2 real, ms real, ex real, mf real)''')
			
# "Commit" para assegurar que a criação da tabela reflita no banco de dados	
db_connection.commit()

# Conexão com o Bando de Dados Mysql
# db_conexao = mysql.connector.connection.MySQLConnection(host='127.0.0.1', user='root', password='', database='cadastroaluno')

# Menu de Alunos

def telaInicial():
    os.system("cls")
    print("\t\tSISTEMA ACADÊMICO\n\n")
    print("\t1. Alunos\n")
    print("\t2. Notas\n")
    print("\t3. Relatorios\n")
    print("\t4. Sair\n")

opcao = 0
while (opcao != 4):
    opcao = 0
    while opcao <= 0 or opcao > 4:
        telaInicial()
        opcao = int(input("\t\tDigite a opção desejada: "))
        if opcao <= 0 or opcao > 4:
            print("\t\tOpção inválida !!!")



    if opcao == 1:
        os.system("cls")
        print("\t\tALUNOS\n\n")
        print("\t   1. Cadastrar")
        print("\t   2. Consultar")
        print("\t   3. Alterar")
        print("\t   4. Excluir\n")
        print("\t   5. Voltar ao menu principal")
        opcao = 0   
        while opcao <= 0 or opcao > 5:
            opcao = int(input("\t\tDigite a opção desejada: "))
            if (opcao <= 0 or opcao > 4):
                print("\t\tOpção inválida !!!")
                pausa = input("\t\n\nPrecione ENTER para continuar...")
            if (opcao == 1):
                matricula = input("Matrícula: ")
                sql = f"SELECT matricula FROM aluno WHERE matricula = '{matricula}'"
                pesqmatricula = cursor.execute(sql)
                matriculaEncontrada = pesqmatricula.fetchone()

                if (matriculaEncontrada == None):
                    nome= input("Digite o nome do aluno(a):  ")
                    curso= input("Digite o curso do aluno(a):  ")
                    turma= input("Digite a turma do aluno(a):  ")
                    sql = "INSERT INTO 'aluno' ('matricula', 'nome', 'curso', 'turma', 'np1', 'np2', 'ms', 'ex', 'mf') VALUES ('"+matricula+"', '"+nome+"', '"+curso+"', '"+turma+"', NULL, NULL, NULL, NULL, NULL)"
                    cursor.execute(sql)
                    db_connection.commit()
                else: 
                    print("\tAluno já cadastrado!!") 

# Consultar aluno
                    
            if opcao == 2:
                matricula = input("Matrícula: ")
                sql =f"SELECT matricula, nome, curso, turma FROM aluno WHERE matricula = '{matricula}'"
                pesqmatricula = cursor.execute(sql)
                matriculaEncontrada = pesqmatricula.fetchone()
                if(matriculaEncontrada == None):
                    if pesqmatricula:
                        print('Matrícula não encontrada!')
                else: 
                    print(matriculaEncontrada)

# Alterar aluno

            if opcao == 3:
                matricula = input("\n\nMatrícula: ")
                sql = f"SELECT matricula, nome, curso, turma FROM aluno WHERE matricula = '{matricula}'"
                pesqmatricula = cursor.execute(sql)
                matriculaEncontrada = pesqmatricula.fetchone()

                if(matriculaEncontrada == None):
                    print('Matrícula não encontrada!')
                else: 
                    nome = input("Digite o novo nome do aluno(a): ")
                    curso = input("Digite o novo curso do aluno(a): ")
                    turma = input("Digite a nova turma do aluno(a): ")
                    sql = f"UPDATE aluno SET nome='{nome}', curso='{curso}', turma='{turma}' where matricula = '{matricula}"
                    cursor.execute(sql)
                    db_connection.commit()
                    print("Cadastro do aluno(a) atualizado com sucesso")

# Excluir aluno

            if opcao == 4:
                opcao = 0 # Corrigir bug que faz com que o programa pare de executar após a exclusão, pois ocorre a condição do while mais externo (opção != 4)
                matricula = input("Matrícula: ")
                sql = f"SELECT matricula, nome, curso, turma FROM aluno WHERE matricula = '{matricula}'"
                pesqmatricula = cursor.execute(sql)
                matriculaEncontrada = pesqmatricula.fetchone()

                if(matriculaEncontrada == None):
                    print('Matrícula não encontrada!')
                else:
                    excluir = input("Deseja realmente excluir (Sim/Não)? ")
                    if excluir == 'Sim':
                        sql = "DELETE FROM aluno where matricula = '"+matricula+"'"
                        print(f"Aluno {matricula} foi excluído !")
                        cursor.execute(sql)
                        db_connection.commit()
#Notas

    elif opcao == 2:
        os.system("cls")
        print("\t\tNOTAS\n\n")
        print("\t   1. Cadastrar notas")
        print("\t   2. Voltar ao menu principal\n")
        opcao = 0   
        while opcao <= 0 or opcao > 2:
            opcao = int(input("\t\tDigite a opção desejada: "))
            if (opcao <= 0 or opcao > 2):
                print("\t\tOpção inválida !!!")
            pausa = input("\t\n\nPrecione ENTER para continuar...")

        if opcao == 1:
            opcao = 0
            matricula = input("Matrícula: ")
            sql = "SELECT matricula FROM aluno WHERE matricula = '"+matricula+"'"
            pesqmatricula = cursor.execute(sql)
            matriculaEncontrada = pesqmatricula.fetchone()
            if (matriculaEncontrada != None):
                np1 = float(input("Digite a nota da NP1: "))
                np2 = float(input("Digite a nota da NP2: "))

            print("Calculando...\n")
            sleep(3)

            ms =float(np1 + np2)/2
            if ms>=6.7:
                if (ms<7):
                    ms=7
                    print("APROVADO")     
            else:
                ex=float(input("Nota do exame: "))
                mf=(ms+ex)/2
                if (mf>=4.7):
                    if (mf<5):
                        mf=5
                        print("APROVADO")
                    else:
                        print("REPROVADO")               

                    sql = "UPDATE aluno SET np1 = '{}', np2 = '{}', ex = '{}' WHERE matricula = {}".format(np1, np2, ex, matricula)

                

                print(f"A nota do aluno(a) da matricula {matricula}, na NP1 foi {np1}, na NP2 foi {np2} e no Exame foi {ex}")
                print(f"A média do aluno foi: {ms}")

                cursor.execute(sql)
                db_connection.commit()
        
		    
# Relatórios
    elif opcao == 3:
        while (opcao != 5):
            opcao = 0   
            while opcao <= 0 or opcao > 4:
                os.system("cls")
                print("\t\tSISTEMA ACADÊMICO\n")
                print("\t\tRELATÓRIOS\n")
                print("\t   1. Lista de todos os alunos")
                print("\t   2. Lista notas dos alunos")
                print("\t   3. Listar situação dos alunos")
                print("\t   4. Voltar ao menu principal\n")
                opcao = int(input("\t\tDigite a opção desejada: "))
                if opcao <= 0 or opcao > 4:
                    print("\t\tOpção inválida !!!")
                    pausa = input("\t\n\nPrecione ENTER para continuar...")
            if opcao == 1:
                os.system("cls")
                sql = "SELECT matricula, nome, curso, turma, np1, np2, ms, ex, mf FROM aluno"
                cursor.execute(sql)
                print("{0:^9} | {1:^25} | {2:^37} | {3:^6} | {4:^5} | {5:^5} | {6:^5} | {7:^5} | {8:^5}".format("MATRICULA", "NOME DO ALUNO", "CURSO", "TURMA", "NP1", "NP2", "MS", "EX", "MF"))
                for (matricula, nome, curso, turma, np1, np2, ms, ex, mf) in cursor:
                    print("{0:^9} | {1:25} | {2:37} | {3:^6} | {4:^5} | {5:^5} | {6:^5} | {7:^5} | {8:^5}".format(matricula, nome, curso, turma, str(np1), str(np2), str(ms), str(ex), str(mf)))
    
            elif opcao == 2:
                print("Coloque seu código aqui!")
            elif opcao == 3:
                print("Coloque seu código aqui!")
            elif opcao == 4:
                continue
            pausa = input("\t\n\nPrecione ENTER para continuar...")
            opcao = 0

    pausa = input("\t\n\nPrecione ENTER para continuar...")
    opcao = 0


db_connection.commit()
cursor.close()
db_connection.close()
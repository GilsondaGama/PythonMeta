import sqlite3
conector = sqlite3.connect("agenda.db")
cursor = conector.cursor()
sql = """delete from contatos where NumContato = ?"""

print("Digite o número do contato para exluir")

Ler = input()
while Ler != "":
    D = Ler.split(",")
    try:
        cursor.execute(sql, D)
        conector.commit()
    except:
        print("{} Dados inválidos".format(D))
    else:
        print(" "*50, "...dados excluidos com sucesso")
    finally:
        print("Digite o número do contato para exluir")
        Ler = input()
cursor.close()
conector.close()


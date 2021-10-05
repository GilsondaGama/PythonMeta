import sqlite3
conector = sqlite3.connect("agenda.db")
cursor = conector.cursor()
sql = """
insert into contatos 
(Nome, Cel, Tel, Email, Aniver) values (?, ?, ?, ?, ?)
"""

print("Digite os dados separados por vírgulas")
print("NumContato, Nome, Cel, Tel, Email, Aniver")

Ler = input()
while Ler != "":
    D = Ler.split(",")
    try:
        cursor.execute(sql, D)
        conector.commit()
    except:
        print("{} Dados inválidos".format(D))
    else:
        print(" "*50, "...dados inseridos com sucesso")
    finally:
        print("Número", "Nome", "Celular", "Telefone", "E-mail", "Aniversário")
        Ler = input()
cursor.close()
conector.close()


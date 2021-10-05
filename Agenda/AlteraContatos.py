import sqlite3
conector = sqlite3.connect("agenda.db")
cursor = conector.cursor()
sql = """update contatos set Cel = ?, Tel = ? 
where NumContato = ?"""

print("Digite os dados separados por vírgulas")
print("Celular, Telefone, Número do Contato")

Ler = input()
while Ler != "":
    D = Ler.split(",")
    try:
        cursor.execute(sql, D)
        conector.commit()
    except:
        print("{} Dados inválidos".format(D))
    else:
        print(" "*50, "...dados alterados com sucesso")
    finally:
        print("Celular, Telefone, Número do Contato")
        Ler = input()
cursor.close()
conector.close()


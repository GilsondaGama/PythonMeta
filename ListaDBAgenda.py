import sqlite3
conector = sqlite3.connect("agenda.db")
cursor = conector.cursor()
cursor.execute("select * from contatos")
dados = cursor.fetchall()
cursor.close()
conector.close()

print("\nConsulta ao Banco de Dados agenda.db \n")
print("Dados da tabela cadastro")
print("-" * 75)
print("{:7} {:20} {:10} {:10} {:10} {:>10} ".format("Número", "Nome", "Celular", "Telefone", "E-mail", "Aniversário"))
print("-" * 75)
for d in dados:
    print("{:<7} {:20} {:>10}".format(d[0], d[1], d[2], d[3], d[4], d[5]))
print("-" * 75)
print("Encontrados {} registros".format(len(dados)))
print("\n\nFim do programa")
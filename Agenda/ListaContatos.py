import sqlite3
conector = sqlite3.connect("agenda.db")
cursor = conector.cursor()
cursor.execute("select * from contatos")
dados = cursor.fetchall()
cursor.close()
conector.close()

print("\nConsulta ao Banco de Dados agenda.db \n")
print("Dados da tabela cadastro")
print("-" * 100)
print("{:7} {:20} {:15} {:15} {:15} {:>15} ".format("Número", "Nome", "Celular", "Telefone", "E-mail", "Aniversário"))
print("-" * 100)
for d in dados:
    print("{:<6} {:20} {:15} {:15} {:15} {:>15}".format(d[0], d[1], d[2], d[3], d[4], d[5]))
print("-" * 100)
print("Encontrados {} registros".format(len(dados)))
print("\n\nFim do programa")
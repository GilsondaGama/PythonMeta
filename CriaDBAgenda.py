import _sqlite3
conexao = _sqlite3.connect("agenda.db")

cursor = conexao.cursor()
cursor.execute("""create table contatos(
NumContato integer NOT NULL PRIMARY KEY autoincrement,
Nome text,
Cel text,
Tel text,
Email text,
Aniver text   
)""")
conexao.commit()
cursor.close()
conexao.close()
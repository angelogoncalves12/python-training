import sqlite3

connection = sqlite3.connect("dados.db")

cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE usuarios(
#     nome TEXT,
#     idade INTEGER
# )
# """)


# cursor.execute(
# "INSERT INTO usuarios VALUES(?, ?)",
#     ("Angelo", 18)
# )


connection.commit()

cursor.execute("SELECT * FROM usuarios") #selecione tudo de usuarios
dados = cursor.fetchall()
print (dados)

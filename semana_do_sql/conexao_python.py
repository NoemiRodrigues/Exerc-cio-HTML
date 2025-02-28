import sqlite3

conexao = sqlite3.connect ('semana_do_sql')

cursor = conexao.cursor()
#cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR (100))')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Laura", 28, "engenharia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Miguel", 15, "física")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Geovana", 20, "física nuclear")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Pedrinho", 34, "administracao")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Natan", 35, "engenharia")')

conexao.commit()

conexao.close
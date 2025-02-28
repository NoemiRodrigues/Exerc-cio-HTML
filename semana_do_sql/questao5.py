import sqlite3

conexao = sqlite3.connect ('semana_do_sql')

cursor = conexao.cursor()
#cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome VARCHAR(100), idade INT, saldo REAL)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Geovana", 28, 158.9)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Felipinho", 50, 999.60)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Ana Luiza", 20, 650)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Luiz", 34, 584.996)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Natan", 19, 52)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, "Carlos Miguel", 46, 9999)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, "Fernanda", 19, 456.978)')


conexao.commit()
conexao.close
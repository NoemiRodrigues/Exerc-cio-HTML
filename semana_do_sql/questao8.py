import sqlite3
conexao = sqlite3.connect ('semana_do_sql')

cursor = conexao.cursor()

''' Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.'''

#cursor. execute ('CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente id INTEGER, produto VARCHAR (100), valor REAL, FOREIGN KEY (id) REFERENCES clientes(id))')
#cursor.execute ('INSERT INTO compras (id, cliente, produto, valor) VALUES (1, "Geovanna", "lápis preto", 1.50 )')
#cursor.execute ('INSERT INTO compras (id, cliente, produto, valor) VALUES (2, "Ana Luiza", "cardigan", 169.99 )')
#cursor.execute ('INSERT INTO compras (id, cliente, produto, valor) VALUES (3, "Felipinho", "Celular motorola", 1500.99 )')
#cursor.execute ('INSERT INTO compras (id, cliente, produto, valor) VALUES (4, "Natan", "Calças cargo", 250.65)')
#cursor.execute ('INSERT INTO compras (id, cliente, produto, valor) VALUES (5, "Luiz", "Mochila Xiaomi", 350 )')
#cursor.execute ('INSERT INTO compras (id, cliente, produto, valor) VALUES (6, "Fernanda", "Coleção de maquaigem", 699.80 )')
#cursor.execute ('INSERT INTO compras (id, cliente, produto, valor) VALUES (7, "Carlos Miguel", "Conjunto de Lego", 799.99 )')

print ("Segue relatório de compras de cada cliente:  ")
compras_cliente= cursor.execute('SELECT cliente, produto, valor FROM compras')
for compras in compras_cliente:
    print (compras)




conexao.commit()

conexao.close


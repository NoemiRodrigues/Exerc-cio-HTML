import sqlite3
conexao = sqlite3.connect ('semana_do_sql')

cursor = conexao.cursor()


#a) Atualize o saldo de um cliente específico.
atualizando_saldo = cursor.execute ("UPDATE clientes SET saldo = 7000 WHERE id =2")
print("Registro atualizado com sucesso.")

print ("__________________________________________________________")   

#b) Remova um cliente pelo seu ID.
cursor.execute ('DELETE FROM clientes WHERE id = 1')
print ("Cliente deletado com sucesso")
conexao.commit()
conexao.close

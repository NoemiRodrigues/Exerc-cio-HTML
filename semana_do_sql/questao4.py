import sqlite3

conexao = sqlite3.connect ('semana_do_sql')
#questao 4, parte a) atualização de idade
cursor = conexao.cursor()
atualizando_idade= cursor.execute('UPDATE alunos SET idade = 28 WHERE id = 5')
conexao.commit()
print("Registro atualizado com sucesso.")

print ("__________________________________________________________")   
#questao 4, parte b) removendo pelo ID
deletando= cursor.execute('DELETE FROM alunos WHERE id= 3')
conexao.commit()
print("Registro deletado com sucesso.")
conexao.close()

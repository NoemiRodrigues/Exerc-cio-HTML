import sqlite3

conexao = sqlite3.connect ('semana_do_sql')
#questao 3, parte a)
cursor = conexao.cursor()
print ("Mostrando todos os alunos ")
visualizando_nossa_tabela = cursor.execute('SELECT * FROM alunos')
for alunos in visualizando_nossa_tabela:
    print (alunos)
print ("__________________________________________________________")   
#questao 3, parte b)
print ("Alunos com idade superior a 20 anos ")
alunos_mais_velhos= cursor.execute('SELECT nome, idade FROM alunos WHERE idade >20')
for alunos in alunos_mais_velhos:
    print (alunos)

print ("__________________________________________________________")   
#questao 3, parte c)
print ("Alunos de engenharia em ordem alfabetica ")
alunos_engenharia = cursor.execute ('SELECT nome FROM alunos WHERE curso = "engenharia" ORDER BY nome ASC')
for alunos in alunos_engenharia:
    print(alunos)
    
print ("__________________________________________________________")   
print("Número total de alunos:")
cursor.execute('SELECT COUNT(*) FROM alunos')
numero_total = cursor.fetchone()[0]
print(f"O número total de alunos é de {numero_total}")
conexao.commit()
conexao.close
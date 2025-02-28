import sqlite3
conexao = sqlite3.connect ('semana_do_sql')

cursor = conexao.cursor()

#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
print ("Clientes com mais de 30 anos:")
clientes_mais_velhos = cursor.execute( 'SELECT nome, idade FROM clientes WHERE idade>30' )
for clientes in clientes_mais_velhos:
    print (clientes)
    
print ("__________________________________________________________")   

    
#b) Calcule o saldo médio dos clientes.
saldo = cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()[0]
print(f"O saldo médio é de {saldo_medio}")

print ("__________________________________________________________")   


#c) Encontre o cliente com o saldo máximo.
print ("Cliente com saldo máximo: ")
cursor.execute("SELECT id, nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)")
cliente_com_saldo_maximo = cursor.fetchall() 
for clientes in cliente_com_saldo_maximo:
    print(clientes)

print ("__________________________________________________________")   

#d) Conte quantos clientes têm saldo acima de 1000.
print ("Clientes com saldo acima de R$ 1.000: ")
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
quantidade_clientes = cursor.fetchone()[0] 
print(f"Número de clientes com saldo acima de R$ 1.000: {quantidade_clientes}")
    
conexao.commit()
conexao.close



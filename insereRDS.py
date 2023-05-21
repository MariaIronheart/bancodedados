from conexao import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
id_tribo = int(input('Digite o id da tribo: '))
nome_tribo = input('Digite o nome da tribo: ')
n_habitantes = input('Digite o número de habitantes: ')
renda_media_mensal = input('Digite a renda média mensal: ')
escolaridade = input('Digite a escolaridade: ')
t_assalariado = input('Possuem trabalho assalariado? (s/n): ')


sql = 'INSERT INTO tribos_brasileiras (id_tribo ,nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado) VALUES (%s,%s,%s,%s,%s,%s)'
val = (id_tribo ,nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado)
cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount , 'registro(s) inserido(s) com sucesso.')

conn.close()

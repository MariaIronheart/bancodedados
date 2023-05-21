from conexao2mariadb import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

id_animal = int(input('Insira o código do animal: '))
raca = input('Digite raca do animal: ')
quantidade = input('Digite a quantidade: ')
risco_extincao = input('Digite se há risco de extinção(sim/nao): ')
area = input('Digite a area que é encontrado: ')


sql = 'INSERT INTO animal (id_animal, raca, quantidade, risco_extincao, area) VALUES (%s,%s,%s,%s,%s)'
val = (id_animal, raca, quantidade, risco_extincao, area)
cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount , 'registro(s) inserido(s) com sucesso.')

conn.close()
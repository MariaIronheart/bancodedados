from conexao2mariadb import conectar
def listar(conn,cursor):
    conn = conectar()
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM animal")
    
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        print(resultado)
    
    cursor.close()
    
    conn.close()
    
def inserir(nid_animal, raca, quantidade, risco_extincao, area):
    conn = conectar()
    cursor = conn.cursor
    
    sql = 'INSERT INTO animal (id_animal, raca, quantidade, risco_extincao, area) VALUES (%s,%s,%s,%s,%s)'
    val = (id_animal, raca, quantidade, risco_extincao, area)
    cursor.execute(sql,val)
    
    conn.commit()
    
    print('Registro inserido com sucesso.')
    
    cursor.close()
    conn.close()
    
def atualizar(id_animal, raca, quantidade, risco_extincao, area):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = 'UPDATE animal SET raca = %s WHERE id_animal = %s'
    val = (id_animal, raca, quantidade, risco_extincao, area)
    cursor.execute(sql,val)
    conn.commit()
    #verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
     print('Nenhum registro atualizado.')
    else: 
     print('Registro atualizado com sucesso.')
    cursor.close()
    conn.close()
    
def deletar(id_animal):
    conn = conectar()
    cursor = conn.cursor
    sql = 'DELETE FROM animal WHERE id_animal = %s'
    val = (id_animal,)
    cursor.execute(sql,val)
    
    conn.commit()
    
    if cursor.rowcount == 0:
     print('Nenhum registro deletado')
    else:
     print('Registro deletado com sucesso')
    cursor.close()
    conn.close()
    
conn = conectar()
cursor = conn.cursor()
while True:
    print('O que você deseja fazer?')
    print('1- Listar animais')
    print('2- Inserir nova raça')
    print('3- Atualizar uma raça')
    print('4- Deletar uma raça')
    print('0- Sair')
    opcao = int(input('Digite o número da opção desejada: '))
    
    if opcao == 1:
        listar(conn, cursor)
     
    elif opcao == 2:
        id_animal = int(input('Insira o código do animal: '))
        raca = input('Digite raca do animal: ')
        quantidade = input('Digite a quantidade: ')
        risco_extincao = input('Digite se há risco de extinção(sim/nao): ')
        area = input('Digite a area que é encontrado: ')
        inserir(id_animal, raca, quantidade, risco_extincao, area)
        
    elif opcao == 3:
        id_animal = int(input('Insira o código do animal: '))
        raca = input('Digite raca do animal: ')
        quantidade = input('Digite a quantidade: ')
        risco_extincao = input('Digite se há risco de extinção(sim/nao): ')
        area = input('Digite a area que é encontrado: ')
        inserir(id_animal, raca, quantidade, risco_extincao, area)
    
    elif opcao == 4:
        id_animal = int(input('Digite o nome da raça que deseja deletar: '))
        deletar(id_animal)
        
    elif opcao == 0:
        break
    
    else:
        print('Opção inválida, digite novamente.')
        
cursor.close()
conn.close()
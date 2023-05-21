from conexao import conectar
def listar(conn,cursor):
    conn = conectar()
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tribos_brasileiras")
    
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        print(resultado)
    
    cursor.close()
    
    conn.close()
    
def inserir(id_tribo, nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado):
    conn = conectar()
    cursor = conn.cursor
    
    sql = 'INSERT INTO tribos_brasileiras (id_tribo ,nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado) VALUES (%s,%s,%s,%s,%s,%s)'
    val = (id_tribo ,nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado)
    cursor.execute(sql,val)
    
    conn.commit()
    
    print('Registro inserido com sucesso.')
    
    cursor.close()
    conn.close()
    
def atualizar(id_tribo,nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado):
    conn = conectar()
    cursor = conn.cursor()
    
    sql = 'UPDATE tribos_brasileiras SET nome_tribo = %s WHERE id_tribo = %s'
    val = (id_tribo, nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado)
    cursor.execute(sql,val)
    conn.commit()
    #verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
     print('Nenhum registro atualizado.')
    else: 
     print('Registro atualizado com sucesso.')
    cursor.close()
    conn.close()
    
def deletar(id_tribo):
    conn = conectar()
    cursor = conn.cursor
    sql = 'DELETE FROM tribos_brasieliras WHERE id_tribo = %s'
    val = (id_tribo,)
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
    print('1- Listar tribos')
    print('2- Inserir nova tribo')
    print('3- Atualizar uma tribo')
    print('4- Deletar uma tribo')
    print('0- Sair')
    opcao = int(input('Digite o número da opção desejada: '))
    
    if opcao == 1:
        listar(conn, cursor)
     
    elif opcao == 2:
        id_tribo = int(input('Digite o id da tribo'))
        nome_tribo = input('Digite o nome da tribo: ')
        n_habitantes = input('Digite o número de habitantes: ')
        renda_media_mensal = input('Digite a renda média mensal: ')
        escolaridade = input('Digite a escolaridade: ')
        t_assalariado = input('Possuem trabalho assalariado? (s/n): ')
        inserir(id_tribo, nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado)
        
    elif opcao == 3:
        id_tribo = int(input('Digite o id da tribo'))
        nome_tribo = input('Digite o nome da tribo: ')
        n_habitantes = input('Digite o número de habitantes: ')
        renda_media_mensal = input('Digite a renda média mensal: ')
        escolaridade = input('Digite a escolaridade: ')
        t_assalariado = input('Possuem trabalho assalariado? (s/n): ')
        atualizar(id_tribo, nome_tribo, n_habitantes, renda_media_mensal, escolaridade, t_assalariado)
    
    elif opcao == 4:
        id_tribo = int(input('Digite o nome da tribo que deseja deletar: '))
        deletar(id_tribo)
        
    elif opcao == 0:
        break
    
    else:
        print('Opção inválida, digite novamente.')

cursor.close()
conn.close()
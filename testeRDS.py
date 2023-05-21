import mysql.connector

config = {
    'user': 'admin',
    'password': 'losing123',
    'host': 'database-1.cp8xbhx2ises.us-east-1.rds.amazonaws.com',
    'database': 'tribos'
}

try:
    conn = mysql.connector.connect(**config)
    print('Execução executada com sucesso')
except mysql.connector.Error as err:
    print(f'Conexão falhou: {err}')
    
cursor = conn.cursor()
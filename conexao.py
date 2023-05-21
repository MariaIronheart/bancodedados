import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host = 'database-1.cp8xbhx2ises.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = 'losing123',
    database = 'tribos'
)

    return mydb
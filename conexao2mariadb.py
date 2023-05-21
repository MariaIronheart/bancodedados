import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host = '18.209.221.73',
    user ='usuarioremoto',
    password = 'minhasenha',
    database = 'animais_africanos'
)

    return mydb
    
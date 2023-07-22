import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Voongra_mysql18'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRMdatabase")

print("All Done!")

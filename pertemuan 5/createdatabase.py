import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE db_penjualan')
print("Berhasil Menambahkan Database")
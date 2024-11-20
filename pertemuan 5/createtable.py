import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_penjualan"
)

mycursor = mydb.cursor()

# membuat sebuah table ke database
mycursor.execute('CREATE TABLE kategori(id int(9) primary key, name varchar(50))')
print("Berhasil Menambahkan Table")

# menampilkan sebuah table pada database
# mycursor.execute('SHOW TABLES')
# for x in mycursor:
#     print(x)
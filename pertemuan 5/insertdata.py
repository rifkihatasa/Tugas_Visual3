import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_penjualan"
)

# mycursor = mydb.cursor()
# sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
# val = ("1","Drinks")
# mycursor.execute(sql, val)

mycursor = mydb.cursor()
sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
val = [("2","Food"),("3","Chiken")]
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "Data Berhasil Ditambahkan")
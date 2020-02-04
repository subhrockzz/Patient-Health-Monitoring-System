import mysql.connector

mydb = mysql.connector.connect(
  host="10.14.79.58",
  user="root",
  passwd="12345",
  database="sq"
)

mycursor = mydb.cursor()

sq = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("subhrajeet", " 21")
mycursor.execute(sq, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


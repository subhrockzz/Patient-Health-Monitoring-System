import socket
import mysql.connector
mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="admin",
        passwd="admin4321",
        database="PATIENT")
mycursor = mydb.cursor()
#mycursor.execute('SELECT Hashkey FROM PERSONAL_INFO WHERE Email = %s', (mail))
# Fetch one record and return result
#hashkey = mycursor.fetchone()
graph_data = open('CI.txt','r').read()
lines = graph_data.split('\n')
for line in lines:
	if len(line) >= 1:
		x=line
for line in lines:
        if len(line) > 1:
            mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="admin",
            passwd="admin4321",
            database="PATIENT")
            mycursor = mydb.cursor()
            PATIENT = "INSERT INTO critical_index (ci) VALUES (%s)"
            val = (x)
            mycursor.execute(PATIENT, val)

            mydb.commit()


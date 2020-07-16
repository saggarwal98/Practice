import mysql.connector
from mysql.connector import Error
db=mysql.connector.connect(user="shubham",password="TCS_Practice",database="Python_Mysql",host="localhost")
try:
    cursor=db.cursor()
    cursor.execute("SELECT NAME,AGE FROM PYTHON_MYSQL")
    rows=cursor.fetchall()
    print("Number of rows:",cursor.rowcount)
    for row in rows:
        print("Name:",row[0])
        print("Age:",row[1])
except mysql.connector.Error:
    print(mysql.connector.Error)
else:
    print("Successfully retrieved values from table")
    if(db.is_connected()):
        db.close()
        cursor.close()
import mysql.connector
from mysql.connector import Error
db=mysql.connector.connect(user="shubham",password="TCS_Practice",database="Python_Mysql",host="localhost")
try:
    cursor=db.cursor()
    x=input("Enter name")
    y=input("Enter age")
    cursor.execute("INSERT INTO PYTHON_MYSQL(NAME,AGE) VALUES(%s,%s)",(x,y))
    # x=input("Enter name")
    # y=input("Enter age")
    # cursor.execute("INSERT INTO PYTHON_MYSQL(NAME,AGE) VALUES('"+x+"','"+y+"')")
    # list1=[("ghi","5"),("jkl","6")]
    # cursor.executemany("INSERT INTO PYTHON_MYSQL(NAME,AGE) VALUES(%s,%s)",list1)
except mysql.connector.Error:
    print(mysql.connector.Error)
else:
    print("Successfully entered values into table")
    if(db.is_connected()):
        db.commit()
        db.close()
        cursor.close()
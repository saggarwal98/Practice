import mysql.connector
from mysql.connector import Error
db=mysql.connector.connect(user='shubham',password='TCS_Practice',database='Python_Mysql',host='localhost')
try:
    cursor=db.cursor()
    print("done before create table")
    cursor.execute("CREATE TABLE PYTHON_MYSQL(ID INT(10) PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(25),AGE INT(10));")
    print("done after create table")
except Error:
    print("Error occured")
    print(Error)
else:
    print("Successfully created table")
    if(db.is_connected()):
        db.commit()
        db.close()
        cursor.close()
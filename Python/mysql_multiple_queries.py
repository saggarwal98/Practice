import mysql.connector
import sys
db=mysql.connector.connect(user='root',password='Shubham@1998',database='mysql_practice',host='localhost')
try:
    cursor=db.cursor()
    a="abcd"
    b="20"
    # cursor.execute("CREATE TABLE IF NOT EXISTS TEMP (ID INT NOT NULL AUTO_INCREMENT,NAME VARCHAR(40),AGE DECIMAL(3,0),PRIMARY KEY(ID));")
    # cursor.execute("ALTER TABLE TEMP AUTO_INCREMENT=100;")
    cursor.execute("INSERT INTO TEMP(NAME,AGE) VALUES(%s,%s)",(a,b))
    cursor.execute("SHOW WARNINGS;")
    rows=cursor.fetchall()
    if len(rows)!=0:
        fn=open("log.txt","w+")
        fn.write(str(rows))
except mysql.connector.errors.ProgrammingError:
    print("Database Offline")
    fn=open("log.txt","w+")
    fn.write(mysql.connector.Error)
except:
    fn=open("log.txt","w+")
    fn.write(str(sys.exc_info()))
if(db.is_connected()):
        db.commit()
        db.close()
        cursor.close()
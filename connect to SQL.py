import mysql.connector
​
connection = mysql.connector.connect(host="localhost" , 
                                     database='mysql',
                                     user='root',
                                     password='password')
cur = connection.cursor(buffered = True)
cur.execute("select user from user")
record = cur.fetchall()
for data in record:
    print(data[0])
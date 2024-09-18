import mysql.connector

'''
db = mysql.connector.connect(host='localhost',user='root',password='')
print(db)

try:
    cursor = db.cursor()
    cursor.execute('create database School_management')
except:
    print('Database could not be created because of duplicate')
'''
db = mysql.connector.connect(host='localhost',user='root',password='',database='aug11python')
print(db)

# USE TRY CATCH
'''
try:
    cursor = db.cursor()
    cursor.execute('CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))')
except:
    print("Table already exists")
'''

'''
# single insert
cursor = db.cursor()
cursor.execute("INSERT INTO customers (name,address) VALUES ('Gorkha','NEPAL')")
db.commit()
'''

'''
#multiple insert
cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ("Johnny", "Highway 50"),
    ("Tom", "Highway 21"),
    ("Dick", "Highway 21"),
    ("Harry", "Highway 21")
]

cursor.executemany(sql, val)

db.commit()
'''

'''
# fetch data from database
mycursor = db.cursor()
mycursor.execute("SELECT * FROM customers")
mycursor.execute("SELECT * FROM customers WHERE name='Ganesh'")
mycursor.execute("SELECT * FROM customers WHERE limit 1")
a = mycursor.fetchall()
for i in a:
    print(i)
'''


# update table on database
mycursor = db.cursor()
mycursor.execute("UPDATE customers SET name='Ganesh' WHERE name='Gorkha'")
db.commit()


# detete data from table on database
mycursor = db.cursor()
mycursor.execute("DELETE FROM customers WHERE name='Ganesh'")
db.commit()





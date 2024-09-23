# program to insert student data into database
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'school_management' 
)
cursor = db.cursor()


records = int(input('How many student records do you want to insert: '))
i = 1
print('____________________')
while i<= records:
    print(f'Student record {i}')
    student_name = input('Enter student name: ')
    student_address = input('Enter student address: ')
    sql = "INSERT INTO students (name, address) VALUES (%s, %s)"
    val = (student_name,student_address)
    cursor.execute(sql, val)
    
    db.commit()
    i += 1
    print('____________________')

print('Data successfully inserted.')




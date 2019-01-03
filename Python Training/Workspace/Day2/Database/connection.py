import sqlite3

connection = sqlite3.connect('C:\\Chinmay\\Database\Info.db')

print(type(connection))
print(connection)

cursor = connection.cursor()

# print(type(cursor))
# print(cursor)
# 
# cursor.execute('SELECT * FROM Employee')
# #print(cursor.fetchall(), '\n\n')
# myList = cursor.fetchall()
# #print(cursor.fetchmany(2))
# 
# for val in myList :
#     print(val)
#     print(val[0], '    ', val[1])

# cursor.execute('INSERT INTO Employee VALUES (?, ?)', (int(input("Enter employeeId: ")), input("Enter EmployeeName: ")))
# connection.commit()   
# print("Record Added")


# cursor.execute('UPDATE Employee SET empName = ? WHERE empId = ?', (input("Enter New employeeName: "), int(input("Enter EmployeeId: "))))
# connection.commit()
# print("Record Updated")

cursor.execute('DELETE FROM Employee WHERE empId = ?', (int(input('Enter EmployeeId to delete: ')),))
connection.commit()
print('Record deleted')
    
fp = open('data.txt')
ans = fp.read(125)

print(type(ans))

print(ans)

fp.seek(0)
mylist = fp.readlines()
for val in mylist:
    print(val, end='')
    
fw = open('newfile.txt', 'w')
fw.write('My name is Chinmay.')
fw.write('\nI am from pune.')

fw.close()
print('\n\n\nData is written.')

# fw1 = open('newfile1.txt', 'a+')
# fw1.write('\n\nMy name is Chinmay.')
# fw1.write('\nI am from pune.')
# fw1.write('\nI live in Chinchwad.')
# fw1.seek(0)
# print(fw1.read())


fw = open('mydata.csv', 'w')
fw.write('ID, Name, Age')
fw.write('\n101, Chinmay, 25')
fw.write('\n102, Suresh, 32')
fw.write('\n103, Ravindra, 30')
print('CSV created')

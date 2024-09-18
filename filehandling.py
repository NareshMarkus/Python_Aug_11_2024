'''
g = open('add.py','r')


f = open('naresh.py','w')
f.write(g.read())

a = open('app.py','r')
b = open('naresh.py','a')
b.write(a.read())

try:
    a = open('earth.py','x') 
except:
    print('File already exists')
'''
# f = open('naresh.py','w+')
# f.write("New content")
# f.seek(0)
# print(f.read())


ff = open('naresh.py','r+')
print(ff.read())
ff.write('Writing new content')
print(ff.read())


#to delete file
import os
os.remove("earth.py")
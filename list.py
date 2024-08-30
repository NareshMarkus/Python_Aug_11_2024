#normal data types
# int,float, str

# inbuilt data types
# list, dict, set, tuple

# list features
# multiple data Store

a=[1,2,4]
#different from array because it supports multiple data types 
b=['Naresh',1,0,1.5]
print(type(a))

print(b[0])
#print last value
print(b[-1])


#returns index error because there is no 5 index
# print(b[5])

#Slicing
teachers = ['Nasir','Irfan','Haris','sheraz','Farhan','Khalil','Haris','Ishan']
print(teachers[1:4])
print(teachers[2:])
print(teachers[:5])
print(teachers[:])

print(len(teachers))

#nested/multiple list
test = [1,2,3,['Naresh','Markus']]
#direct method
print(test[3][0])
#indirect method
x= test[-1]
print(x[-1])

#append(add valiues at last)
teachers.append('Ganesh')
print(teachers)

#empty list
a = []
print("Before append")
print(a)
print('after append')
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print(a)

#list insert
print('insert')
test=[1,2,3,4,5]
print(test)
test.insert(2,'Naresh')
print(test)

#if index is high error is not shown rather the value is inserted at last
test.insert(5467,9)

#multiple insert in same index
test.insert(2,'Naresh')
test.insert(2,'Puja')
test.insert(2,'Sudan')
print(test)

#List concatenation
x = [1,2,3,4,5]
y = [6,7,8,9,10]
print(x+y)



#classword exercise

# z = int(input('Enter a number: '))
# print('user entered ',z)
# list = []
# if(z%2==0):
#     list.append(z)
#     print(z,' is even. So, Added to list')
#     print(list)
# else:
#     print(Z,' id odd. So, Not added to list')
#     print(list)


#List extend
test1 = [1,2,3,4,5,6,7,8,9,10]
test2 = ['a','b','c']
test1.extend(test2)
print(test1)

#delete index from 
del test1[-1]
print(test1)

#deletes list variable and throws error
del test1
#print(test1)


#remove specified item from list
aa = [1,1,1,1,1]
aa.remove(1)
print(aa)

#pop(remove last item from list:opposite of append)
bb = [1,2,3,4,5]
bb.pop()
bb.pop()
print(bb)

#clear: makes the list empty
xx = [1,2,3,4,5]
xx.clear()
print(xx)

#count instances of a variable
xx = [1,2,1,4,1]
print(xx.count(1))







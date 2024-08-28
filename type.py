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





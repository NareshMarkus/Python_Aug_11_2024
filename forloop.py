'''
for i in [1,2,3,4,5]:
    print(i)
    a={}

a=[1,2,3,4,5]
for i in a:
    print(i)   

for i in 'Naresh':
    print(i)
#in is a membership operator
# a = 4 in [1,2,4]
# print(a)

# a = 3 in [1,2,4]
# print(a)

a = range(1,10)
for i in a:
    print(i)

for i in range(1,10,2):
    print(i)

print('_____________________________________________')
for i in range(10):
    print(i)

print('_____________________________________________')
for i in range(10,0,-1):
    print(i)

#classwork
print('_____________________________________________')
a = range(0,3)
x =['Naresh','test','broadway']
for i in a:
    print(x[i])
print('\n')

#alternative
print('_____________________________________________')
x =['suddan','test','broadway']
for i in range(0,len(x)):
    print(x[i])
print('\n')

#assignment(Multiplication table)
x = int(input('Enter the number you want table of: '))
print('\n')
print(f'______Multiplication table of {x}______')
for j in range(1,11):
    print(f'{x} X {j} = {x*j}')


#nested for loop
for i in [1,2]:
    for j in [3,4]:
        print (i,j)

#Exercise
print('_________________________________\n')
a = [2,3,5]
for i in a:
    print(f'Multiplication table of {i}')
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')


a = [1,2,3,4,5]
sum = 0
for i in a:
    sum = sum + i
print(sum)
'''    

x = []
for i in range(4):
    x.append(i)

    print (f'{x[i]} ')
    for j in range(1,6):
        pass
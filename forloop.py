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
x =['suddan','test','broadway']
for i in a:
    print(x[i])

#alternative
print('_____________________________________________')
x =['suddan','test','broadway']
for i in range(0,len(x)):
    print(x[i])

#assignment(table of 2)
for j in range(1,11):
    print(f'2 X {j} = {2*j}')

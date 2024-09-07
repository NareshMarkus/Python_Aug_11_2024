# homework(give user option to input as many input as they want, sort odd and print multiplication table of odd only)
'''
a = int(input('How many numbers do you want to Enter: '))
y = []
print('\n')
print('+++++++++++++++++++++++++++++++++++++++++++++')
for i in range(a):
    b = int(input(f'Enter the number {i+1}: '))
    if(b%2==1):
        y.append(b)
        y.sort()
print('\n')
print('+++++++++++++++++++++++++++++++++++++++++++++')
for j in y:
    print(f'Multiplication table of {j}')
    for k in range(1,11):
        print(f'{j} x {k} = {j*k}')
    print('\n')
'''

'''
# alternative method 
a = int(input('How many numbers do you want: '))
c = []
for i in range(a):
    b = int(input(f'Enter number {i+1}: '))
    c.append(b)


i=0
while(0>=i<a):
    for i in c:
        if(i%2==1):
            print('\n')
            print(f'Multiplication table of {i}')
            for j in range(1,11):
                print(f'{i} x {j} = {i*j}')
            i=i+1
            print('\n')
'''

'''
# teacher solution
a = int(input('How many numbers do you want to Enter: '))
y = []
print('\n')
print('+++++++++++++++++++++++++++++++++++++++++++++')
for i in range(a):
    b = int(input(f'Enter the number {i+1}: '))
    y.append(b)
y.sort()  
print('\n')
print('+++++++++++++++++++++++++++++++++++++++++++++')
for j in y:
    if(j%2!=0):
        print(f'Multiplication table of {j}: ')
        for k in range(1,11):
            print(f'{j} X {k} = {j*k}')
'''
# loop homework1
print("Number Pattern ")
print('')
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")



# loop homework3
print('\n')
print("Character Pattern ")
print('')
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print('*', end=' ')
    print("")

print('')

for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end=' ')
    print("")


# loop homework2
print('\n')
x = int(input('How many natural numbers do you want: '))
sum = 0
for i in range(1,x+1):
    sum = sum + i
    
print(f'The sum of first {x} natural numbers is {sum}')
print('')
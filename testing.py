name = 'Ganesh Amgain'
address = 'Kathmandu'

#My name is Ganesh Amgain and I live in Kathmandu
print('My name is',name,'and I live in',address)
print('My name is '+name+' and I live in '+address)

#fstring
print(f'My name is {name} and I live in {address} {10+4}')


#assignment(table of 2)
print('\n')
print('______Multiplication table of 2______')
for j in range(1,11):
    print(f'2 X {j} = {2*j}')

print('\n')
#Exercise
a = [2,3,5]
for i in a:
    print(f'Multiplication table of {i}')
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')
    print('\n')
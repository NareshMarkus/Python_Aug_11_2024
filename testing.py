name = 'Ganesh Amgain'
address = 'Kathmandu'

#My name is Ganesh Amgain and I live in Kathmandu
print('My name is',name,'and I live in',address)
print('My name is '+name+' and I live in '+address)

#fstring
print(f'My name is {name} and I live in {address} {10+4}')


#assignment(table of 2)
print('______Multiplication table of 2______')
for j in range(1,11):
    print(f'2 X {j} = {2*j}')
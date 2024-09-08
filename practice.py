# loop homework using while loop
# loop homework1
print("Number Pattern ")
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1



# loop homework3
print("Character Pattern ")
i = 5
while i>0:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i -= 1

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

# loop homework 2
print('\n')
x = int(input('How many natural numbers do you want: '))
sum = 0
i=1
while i<=x:
    sum = sum+i
    i += 1 
print(f'The sum of first {x} natural numbers is {sum}')
print('')


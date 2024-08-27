# a = input('Enter first number: ')
# b = input('Enter second number: ')
# x = int(a)
# y = int(b)

# if(x==y): 
#     print('The numbers you entered are equal')
# else:
#     print('The numbers you entered are not equal')



a = input('Enter first number: ')
x = int(a)

if(x%2==0):
    print(a,' is even')
else:
    print(a,' is odd')


# simple if

# gen = "M"
# if(gen=="M"): print('male')
# else: print ('female')

#single line if
gender = "M"
a = "Male" if gender == "M" else "Female"
print(a)
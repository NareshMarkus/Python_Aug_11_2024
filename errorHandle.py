test = 1

try:
    print(test1)
except:
    print('Error')

try:
    print(test1)
except NameError:
    print("Name is not found")


try:
    print(test1)
except NameError as e:
    print(e)
except ZeroDivisionError:
    print('Do not divide by Zero')
except:
    print("ERROR")
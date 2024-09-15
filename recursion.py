'''
def recuring():
    for i in range(1,5):
        print(i)
    recuring()

recuring()
'''


# Factorial using recursive function
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


a = [1,2,[1,2,3,[2,5,7,9],[15,12,17]]]
# returns true or false
a = isinstance(a,list)


num = input('Enter a number: ')
if num.isdigit():
    sum = int(num)+10
    print(sum)
else:
    print('Enter a valid number')

# recuring function to find sum of n natural numbers
def sum_natural(n):
    if n==0:
        return 0
    else:
        return n + sum_natural(n-1)
print(sum_natural(10))


# tri recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
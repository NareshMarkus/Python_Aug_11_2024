'''
# function without arguement
def add():
    a = 2+2
    b = 4+3
    c = []
    for i in range(1,5):
        c.append(i)
    return c
print(add())

# function with arguement
def my_info(name,age):
    print(f'My name is {name}. I am {age} years old.')

my_info('Haris',24)

# function to print the sum of n natural numbers
def natural_sum(n):
    sum = 0
    sum = n/2*(n+1)
    return sum
 
n = int(input('How many natural numbers do you want: '))
print(f'The sum of first {n} natural numbers is {int(natural_sum(n))}.')
'''

'''
#setting default argurement
def online_khabar(title,content,author="Online Khabar"):
    print(title,content,author)
# if author is not provided, default arguement is printed
online_khabar("test-title",'test content')

#keyword arguement
def keyword_arg(name,surname):
    print(name, surname)

keyword_arg(name="Naresh",surname="Markus")

# arbitrary arguement
def test(*data):
    print(data)
test(1,2,4,34,54,23,234)

#arbitrary arguement
def test(*data):
    sum = 0
    for i in data:
        sum = sum + i
    #return sum
    print(f'The sum is {sum}')
test(1,2,4,34,54,23,234)


# arbritary keyword argument
def test1(**data):
    print('Hello')
    print(data)
    print(type(data))
    lst = list(data)
    print(lst)

test1(name='Naresh',surname='Markus',a=3)
'''


# arbitrary positional/keyword argument
def hello(*args,**kwargs):
    print('Positional: ',args)
    print('Keyword: ',kwargs)
    return args,kwargs

print(hello(1,2,3,4,name='naresh'))


# recursive function
def test():
    print('Hello')
    test()

test()

 

'''
class Test():
    name = "Naresh"
    a = 4
    b = 7
obj1 = Test()
print(obj1.name)
obj1.name = "Ganesh"
print(obj1.name)

# class
class Test1():
    name = 'Broadway'
    subject = 'Python'

    # returns string
    def __str__(self) -> str:
        pass

    def teacher(self):
        return f"I am a teacher at {self.name} and I teach {self.subject}."
    
obj = Test1()
print(obj.teacher())
'''

# class with constructor
class Test2():
    a = 2
    b = 3
    # constructor 
    def __init__(self,a,b) -> None:
        print('Hi I am constructor')
        self.a = a
        self.b = b
        pass

    def test(self):
        return self.a
    
obj2 = Test2('Hello','world')
print(obj2.test())



class Math():
    def __init__(self,num1,num2) -> None:
        self.a = num1
        self.b = num2

    def add(self):
        return self.a+self.b
    
    def diff(self):
        return self.a-self.b
    
    def mul(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
    
operation = Math(6,7)
print(operation.add())
print(operation.diff())
print(operation.mul())
print(operation.div())
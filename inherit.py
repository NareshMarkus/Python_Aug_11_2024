'''
class Parent():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b


class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a, b)
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

obj = Child(20,5)
print(obj.add())
print(obj.subtract())
print(obj.mul())
print(obj.div())
'''

'''

- make a 2 class parent and child 
- parent class should have 2 method as well as child
- child class object should access parent class method

'''



class Parent():
    def __init__(self) -> None:
        self.d = 12

    def method1(self):
        return "parent method 1"

    def method2(self):
        return "Parent method 2"

class Child(Parent):
    def __init__(self):
        self.a = 22
        super().__init__()
        

    def method3(self):
        return "child method 1"

    def method4(self):
        return "child method 2"
    
obj = Child()
print(obj.method1())
print(obj.method2())
print(obj.method3())
print(obj.method4())
print(obj.a)
print(obj.d)



# multi-level inheritance
class Parent():
    a = 10

class Child1(Parent):
    c = 12

class Child2(Child1):
    d = 100
    def __init__(self) -> None:
        super().__init__()

obj = Child2()
print(obj.a,obj.c, obj.d)


# multiple inheritance
class Parent1():
    a = 100

class Child11():
    c = 122

class Child22(Parent,Child11):
    d = 150
    def __init__(self) -> None:
        super().__init__()

obj = Child22()
print(obj.a,obj.c, obj.d)


# multiple inheritance example
class Mammal():
    def mammal_info(self):
        print('Mammals can give direct birth')

    def test(self):
        return 12

class WingedAnimal():
    def winged_animal_info(self):
        print('Winged animals can flap')

    def test(self):
        return "Hello"

class Bat(Mammal, WingedAnimal):
    pass

obj1 = Bat()
obj1.mammal_info()
obj1.winged_animal_info()
print(obj1.test())


# classwork
class Prokaryotic():
    def __init__(self,name) -> None:
        self.name = name

    def features(self):
        print(self.name,' do not have well defined nucleus')

class Unicellular():
    def __init__(self,flag) -> None:
        self.flagella = flag
    def feature(self):
        print('They are single celled and have ',self.flagella)

class Bacteria(Prokaryotic,Unicellular):
    def __init__(self, name) -> None:
        super().__init__(self)

a1 = Bacteria()
a1.features()
a1.feature()



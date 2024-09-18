class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Move!')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print('Sail!')

class Plane(Vehicle):
    def move(self):
        print('Fly!')

car1 = Car("Ford", "Mustang")
boat1 = Boat("Boat","Titanic")
plane1 = Plane("Jet",3901)

for x in [car1,boat1,plane1]:
    print(f'brand: {x.brand}')
    print(f'model: {x.model}')
    x.move()
    
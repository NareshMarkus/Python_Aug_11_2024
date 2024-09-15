class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        print(f'brand = {brand}')
        print(f'model = {model}')

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

car1.move()
boat1.move()
plane1.move()
    
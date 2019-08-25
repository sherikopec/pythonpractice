from Vehicle import Vehicle
# from folder.folder.folder.file import class

class Car(Vehicle):

# Pass - handy when writing a program and you don't know what you want a particular thing to do yet

    def __init__(self, num_doors, num_wheels, colour, action):
        super().__init__(num_wheels, colour, action)
        self.num_doors = num_doors


my_car = Car(4, 4, 'blue', 'Brrrm Brrrm!')
my_second_car = Car(5, 4, 'silver', 'Brrrm Brrrm!')
    
print(my_car.colour)
my_car.start_action()
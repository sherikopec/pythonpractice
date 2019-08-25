from Vehicle import Vehicle

class Bicycle(Vehicle):

    def __init__(self, num_wheels, colour, has_bell, action):
        super().__init__(num_wheels, colour, action)
        self.has_bell = has_bell

    def ring_bell(self):
        if self.has_bell:
            print('Ding!')

my_bike = Bicycle(2, 'red', True, 'I am pedalling!')
my_second_bike = Bicycle(3, 'green', False, 'I am pedalling!')

print(my_second_bike.colour)
my_bike.start_action()
my_bike.ring_bell()
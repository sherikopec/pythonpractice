class Vehicle:

    def __init__(self, num_wheels, colour, action):
        self.num_wheels = num_wheels
        self.colour = colour
        self.action = action

    def start_action(self):
        print(self.action)
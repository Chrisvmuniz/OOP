import random


class Insect:

    def __init__(self):
        self.legs = 4
        self.wings = 2
        self.flight = random.randint(1, 10)
                 
     


    def flightLength(self):
        return (self.flight) 



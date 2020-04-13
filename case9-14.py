from random import randint

class Die():
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        self.sides = randint(1,6)
        print(self.sides)

sides_1 = Die()
sides_1.roll_die()
sides_1.roll_die()
sides_1.roll_die()
sides_1.roll_die()
sides_1.roll_die()
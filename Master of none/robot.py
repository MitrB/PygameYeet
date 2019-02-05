import random

robot_number = 0
robot_types = ["hitter", "resource", "medic"]

class robot(object):
    """docstring for robot"""
    energy_max = 4

    def __init__(self, type, energy):
        if not type in robot_types:
            print("ERROR: Robot type is not legit!...", type)

        self.type = type
        self.energy = energy
        self.sprite = str(self.type) + ".png"

        if self.type == "hitter":
            self.attack = 5
            self.defence = 4
            self.special = "push_through"

        elif self.type == "resource":
            self.attack = 3
            self.defence = 2
            self.special = "big_recovery"

        elif self.type == "medic":
            self.attack = 2
            self.defence = 3
            self.special = "last_resort"

    def upgrade(self, attribute, amount):
        if attribute == "attack":
            self.attack += amount
        elif attribute == "defence":
            self.defence += amount
        elif attribute == "energy_max":
            self.energy_max += amount

    def energy_down(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            self.__del__()

    #stat return + .png file
    def energy(self):
        return self.energy
    def attack(self):
        return self.attack
    def defence(self):
        return self.defence
    def sprite(self):
        return self.sprite

    def present(self):
        print(  "type:", self.type,\
                "\n---------",\
                "\nattack:",self.attack,\
                "\ndefence:",self.defence,\
                "\nenergy:",self.energy,\
                "\nspecial:", self.special,\
                "\nsprite:", self.sprite    )

    def __del__(self):
        pass



def robot_generator():
    type = random.choice(robot_types)
    energy = 4

    return (type, energy)

robot_1 = robot(robot_generator()[0], robot_generator()[1])
robot.present(robot_1)

class Hero:
    def __init__(self,charecter, power, helthe):
        self.charecter = charecter
        self.power = power
        self.helthe = 100
    def attack(self):
        print(f'{self.charecter} attacks {self.power} {self.helth} damage')
warror = Hero('Warror', 1, 100)
archer = Hero('Archer', 2, 100)
warror.attack('deragon')



class Creature:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        if self.health - amount < 0:
            pass
        else:
            self.health -= amount
        
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def get_status(self):
        return f"{self.name}: {self.health} HP"
        
class Monster(Creature):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health)
        self.__attack_power = attack_power

    def attack(self, target):
        target.take_damage(self.__attack_power)

    def get_attack_power(self):
        return self.__attack_power




blob = Creature("Bob the Blob", 100)
vlad = Monster("Vlad", 150, 5)
frank = Monster("Frank", 200, 10)

print(frank.health)

print(vlad.health)
frank.attack(vlad)
print(vlad.health)

print(vlad.get_attack_power())
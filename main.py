class Creature:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        if self.health - amount < 0:
            return True
        else:
            return False
        
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





blob = Creature("Bob the Blob", 100)
vlad = Monster("Vlad", 150, 5)

print(f"DEBUG: Attack power = {vlad.get_attack_power()}")
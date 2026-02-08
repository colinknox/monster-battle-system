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

class BossMonster(Monster):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.__enraged = False
        self.original_health = self.health
        self.becomes_enraged = self.original_health * 0.3

    def take_damage(self, amount):
        super().take_damage(amount)

        if self.health < self.becomes_enraged and self.__enraged == False:
            self.__enraged = True
            print(f"{self.name} becomes enraged!")



the_boss = BossMonster("The Boss", 100, 10)

print(the_boss.health)
print(the_boss.take_damage(70))
print(the_boss.health)
# print(the_boss.original_health)
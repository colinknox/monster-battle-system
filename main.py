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
        


blob = Creature("Bob the Blob", 100)

print(blob.health)
print(blob.get_status())

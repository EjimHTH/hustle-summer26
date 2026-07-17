import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        random_damage = random.randint(0, self.max_damage)
        print(random_damage)
        return random_damage


if __name__ == "__main__":
    ability_1 = Ability("Super Speed", 50)
    print(ability_1.name)
    print(ability_1.max_damage)
    ability_1.attack()
    
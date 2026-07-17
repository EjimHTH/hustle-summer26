import random

class Armor:

    def __init__(self, name, max_block):
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        random_block = random.randint(0, self.max_block)
        return random_block
    
if __name__ == "__main__":
    armor_1 = Armor("Really Srong Helmet", 50)
    print(armor_1.name)
    print(armor_1.max_block)
    armor_1.block()
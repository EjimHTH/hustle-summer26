import random
from ability import Ability


class Weapon(Ability):

    def attack(self):
        """This method returns a random value
        between one half to the full attack power of the weapon.
        """

        random_damage = random.randint(
            self.max_damage // 2,
            self.max_damage
        )

        print(random_damage)
        return random_damage


if __name__ == "__main__":
    sword = Weapon("Sword", 100)

    for i in range(5):
        sword.attack()
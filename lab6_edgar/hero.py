import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        total_blocked = self.defend()
        actual_damage = max(damage - total_blocked, 0)
        self.current_health -= actual_damage

        if self.current_health < 0:
            self.current_health = 0

        print(self.current_health)
        return actual_damage

    def battle(self, opponent):

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.current_health > 0 and opponent.current_health > 0:

            # Hero attacks
            damage = self.attack()
            opponent.take_damage(damage)

            if opponent.current_health == 0:
                self.add_kill()
                opponent.add_death()
                print(f"{self.name} won!")
                return

            # Opponent attacks
            damage = opponent.attack()
            self.take_damage(damage)

            if self.current_health == 0:
                opponent.add_kill()
                self.add_death()
                print(f"{opponent.name} won!")
                return


if __name__ == "__main__":

    my_hero = Hero("Spider-Man", 150)
    my_opponent = Hero("Captain America", 350)

    # Give Spider-Man abilities and armor
    my_hero.add_ability(Ability("Web Shooter", 25))
    my_hero.add_ability(Ability("Spidey Sense", 10))
    my_hero.add_ability(Ability("Electric Shock", 50))
    my_hero.add_ability(Ability("Punch", 20))
    my_hero.add_weapon(Weapon("Sword", 40))

    my_hero.add_armor(Armor("Cat Ears", 20))
    my_hero.add_armor(Armor("Cute Necklace", 5))
    my_hero.add_armor(Armor("Hokas", 15))

    # Give Captain America an ability so the battle isn't a draw
    my_opponent.add_ability(Ability("Shield Throw", 30))

    # Battle!
    my_hero.battle(my_opponent)

    print(f"{my_hero.name}: {my_hero.kills} kills, {my_hero.deaths} deaths")
    print(f"{my_opponent.name}: {my_opponent.kills} kills, {my_opponent.deaths} deaths")
import random
from hero import Hero


class Team:

    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.kills = 0
        self.deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def attack(self, other_team):

        living_heroes = self.heroes.copy()
        living_opponents = other_team.heroes.copy()

        while len(living_heroes) > 0 and len(living_opponents) > 0:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.battle(opponent)

            if hero.current_health <= 0:
                living_heroes.remove(hero)

            if opponent.current_health <= 0:
                living_opponents.remove(opponent)

    def revive(self):
        """Restore all heroes to full health."""
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        """Display each hero's battle statistics."""
        for hero in self.heroes:
            print(
                f"{hero.name} - "
                f"Kills: {hero.kills}, "
                f"Deaths: {hero.deaths}, "
                f"Health: {hero.current_health}"
            )


if __name__ == "__main__":

    avengers = Team("Avengers")

    spider_man = Hero("Spider-Man")
    captain_america = Hero("Captain America")
    iron_man = Hero("Iron Man")

    avengers.add_hero(spider_man)
    avengers.add_hero(captain_america)
    avengers.add_hero(iron_man)

    print("Heroes:")
    avengers.view_all_heroes()

    spider_man.current_health = 0
    iron_man.current_health = 25

    print("\nBefore revive:")
    print(spider_man.current_health)
    print(iron_man.current_health)

    avengers.revive()

    print("\nAfter revive:")
    print(spider_man.current_health)
    print(iron_man.current_health)
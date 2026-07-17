from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:

    def __init__(self):
        """Instantiate Arena properties."""
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        """Prompt user for Ability information."""
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")
        return Ability(name, max_damage)

    def create_weapon(self):
        """Prompt user for Weapon information."""
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")
        return Weapon(name, max_damage)

    def create_armor(self):
        """Prompt user for Armor information."""
        name = input("What is the armor name? ")
        max_block = input("What is the max block of the armor? ")
        return Armor(name, max_block)

    def create_hero(self):
        """Create a Hero and allow the user to add abilities, weapons, and armor."""

        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)

        add_item = None

        while add_item != "4":

            add_item = input(
                "\n[1] Add Ability\n"
                "[2] Add Weapon\n"
                "[3] Add Armor\n"
                "[4] Done adding items\n\n"
                "Your choice: "
            )

            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)

            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)

            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)

            elif add_item == "4":
                print("Finished creating hero.")

            else:
                print("Invalid choice.")

        return hero

    def build_team_one(self):
        """Prompt the user to build Team One."""

        team_name = input("Enter Team One's name: ")
        self.team_one = Team(team_name)

        num_members = int(
            input("How many members would you like on Team One?\n")
        )

        for i in range(num_members):
            print(f"\nCreating Hero #{i + 1}")
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        """Prompt the user to build Team Two."""

        team_name = input("Enter Team Two's name: ")
        self.team_two = Team(team_name)

        num_members = int(
            input("How many members would you like on Team Two?\n")
        )

        for i in range(num_members):
            print(f"\nCreating Hero #{i + 1}")
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        """Battle Team One against Team Two."""
        self.team_one.attack(self.team_two)

    def show_stats(self):
        """Print battle statistics."""

        print("\n==============================")
        print("Battle Statistics")
        print("==============================\n")

        print(self.team_one.name + " statistics:")
        self.team_one.stats()

        print()

        print(self.team_two.name + " statistics:")
        self.team_two.stats()

        print()

        # Team One K/D
        team_one_kills = 0
        team_one_deaths = 0

        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths

        if team_one_deaths == 0:
            team_one_deaths = 1

        print(
            self.team_one.name +
            " average K/D: " +
            str(team_one_kills / team_one_deaths)
        )

        # Team Two K/D
        team_two_kills = 0
        team_two_deaths = 0

        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths

        if team_two_deaths == 0:
            team_two_deaths = 1

        print(
            self.team_two.name +
            " average K/D: " +
            str(team_two_kills / team_two_deaths)
        )

        print("\nSurvivors:")

        for hero in self.team_one.heroes:
            if hero.current_health > 0:
                print(hero.name + " survived from " + self.team_one.name)

        for hero in self.team_two.heroes:
            if hero.current_health > 0:
                print(hero.name + " survived from " + self.team_two.name)


if __name__ == "__main__":

    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()

        play_again = input("\nPlay Again? (Y/N): ")

        if play_again.lower() == "n":
            game_is_running = False

        else:
            arena.team_one.revive()
            arena.team_two.revive()
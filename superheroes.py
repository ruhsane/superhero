import random

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        # Set Ability name
        # Set attack strength
        self.name = name
        self.attack_strength = attack_strength


    def attack(self):
        # Return attack value

        # Calculate lowest attack value as an integer.
        lowest_attack_value = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        random_attack_value = random.randint(lowest_attack_value, self.attack_strength)
        # Return attack value between lowest and the full attack.
        return random_attack_value

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name
        # Initialize starting values

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        for ability in self.abilities:
            ability.attack()
            print(ability.name)

class Team:
    def __init__(self, name):
        self.heroes = list()
        self.name = name

    def add_hero(self, hero):
        self.heroes.append(hero)

    def print_heroes(self):
        for hero in self.heroes:
            print(hero.name)

if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
    tele = Ability("ruru", 5)
    gg = Ability("fast", 10)
    flash = Ability("flash", 4)

    hero = Hero("Ruxxxxaaanaaa")
    jinx = Hero("Jinx")

    blue = Team("blue")

    blue.add_hero(hero)
    blue.add_hero(jinx)

    jinx.add_ability(tele)
    jinx.add_ability(gg)
    jinx.add_ability(flash)


    hero.add_ability(tele)
    hero.add_ability(gg)
    hero.attack()

    blue.print_heroes()

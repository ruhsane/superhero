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
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_armor(self, Armor):
        #add armor to the list
        self.armors.append(Armor)

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        if self.health <= 0:
            total_defense = 0
            return total_defense

        total_defense = 0
        for armor in self.armors:
            defense = armor.defend()
            total_defense += defense
        return total_defense

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """
        self.health -= damage_amt

        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        # if name in self.heroes:
        #     self.heroes.remove(name)
        # else:
        #     return 0

        for hero in self.heroes:
            if name == hero.name:
                return self.heroes.remove(hero)

        return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        #[obj1(r), obj2(jinx)]
        # print(self.heroes)
        for hero in self.heroes:
            if name == hero.name:
                return hero

        return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        print("List of heroes in the team: ")
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        team_total_attack_strenth = 0
        for hero in self.heroes:
            if hero.health > 0:
                team_total_attack_strenth += hero.attack()

        number_of_kills = other_team.defend(team_total_attack_strenth)

        for hero in self.heroes:
            hero.add_kill(number_of_kills)

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        team_total_defense = 0
        for hero in self.heroes:
            team_total_defense += hero.defend()

        if damage_amt > team_total_defense:
            dmg_taken = damage_amt - team_total_defense
            return self.deal_damage(dmg_taken)

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        each_hero_damage = damage//len(self.heroes)
        dead_heroes = 0
        for hero in self.heroes:
            hero.take_damage(each_hero_damage)
            if hero.health <= 0:
                dead_heroes += 1
        return dead_heroes

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health


    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """

        for hero in self.heroes:
            print("{}:{}/{}".format(hero.name, hero.kills, hero.deaths))

    # def update_kills(self):
    #     """
    #     This method should update each hero when there is a team kill.
    #     """

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        random_attack_value = random.randint(0, self.attack_strength)
        print(random_attack_value)
        return random_attack_value


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        return random.randint(0, self.defense)


#Implement the above methods. Use your favorite loops with the input() function to build teams based on user input.
class Arena:
    def __init__(self, team_one=Team(input("Team one name? ")), team_two= Team(input("Team two name? ")) ):
        """
        Declare variables
        """
        self.team_one = team_one
        self.team_two = team_two


    def add_new_ability(self, hero):
        continue_adding = True

        while continue_adding == True:

            ability1 = input("Enter an ability name to add to your hero: ")
            hero = Hero(hero)
            hero.add_ability(ability1)
            continue_adding_or_no = input("Do you want to add more abilities to your hero? (enter Yes or No): ")

            if continue_adding_or_no.upper() == "YES":
                continue_adding = True
            elif continue_adding_or_no.upper() == "NO":
                continue_adding = False
            # else:
            #     continue_adding_or_no = input("Please enter yes or no: ")
            #     return add_new_ability

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        continue_adding = True

        while continue_adding == True:
            #add new hero
            hero = Hero(input("Enter a hero name to add to Team 1: "))
            self.team_one.add_hero(hero)
            self.team_one.view_all_heroes()

            #add ability
            self.add_new_ability(hero)

            #ask for more hero
            continue_adding_or_no = input("Do you want to add more heroes? (enter Yes or No): ")

            if continue_adding_or_no.upper() == "YES":
                continue_adding = True
            elif continue_adding_or_no.upper() == "NO":
                continue_adding = False

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        #add new hero
        hero = Hero(input("Enter a hero name to add to Team 2: "))
        # hero.name = input("Enter a hero name to add to Team 2: ")
        self.team_two.add_hero(hero)
        self.team_two.view_all_heroes()

        #add ability
        self.add_new_ability(hero)

        #ask for more hero
        continue_adding_or_no = input("Do you want to add more heroes? (enter Yes or No): ")

        if continue_adding_or_no.upper() == "YES":
            continue_adding = True
        elif continue_adding_or_no.upper() == "NO":
            continue_adding = False

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        battle = True

        if self.team_one.deal_damage == len(self.team_one.heroes) or self.team_two.deal_damage == len(self.team_one.heroes):
            battle = False

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        print("Team One Stats:")
        print(self.team_one.stats())
        print("Team Two Stats:")
        print(self.team_two.stats())

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

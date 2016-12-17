import moves


class Pokemon():
    """create a Pokémon with stats

    name -- the pokémon's name
    hp -- the pokémon's health points
    attack -- the pokémon's attack stat, how much damage it can do
    defense -- not implemented
    """

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.startHp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense


def attack(player, pokemon1, pokemon2):
    """one pokémon attacks another

    choose move to be used
    call move function
    """
    print("\n\tPlayer %s choose move" % player)
    print("\t\t1: Tackle")
    print("\t\t2: Growl")
    choice1 = input("\n")
    if choice1 == "1":
        moves.tackle(pokemon1, pokemon2)
    else:
        moves.growl(pokemon1, pokemon2)


def printStats(pokemon1, pokemon2):
    """print battling pokémon stats"""
    goodName1 = pokemon1.name.ljust(12)
    goodName2 = pokemon2.name.ljust(12)
    goodHp1 = (str(pokemon1.hp) + "/" + str(pokemon1.startHp)).ljust(7)
    goodHp2 = (str(pokemon2.hp) + "/" + str(pokemon2.startHp)).ljust(7)
    goodAtk1 = (str(pokemon1.attack)).ljust(2)
    goodAtk2 = (str(pokemon2.attack)).ljust(2)
    goodDef1 = (str(pokemon1.defense)).ljust(2)
    goodDef2 = (str(pokemon2.defense)).ljust(2)
    print("\n\t+--------------+  +--------------+")
    print("\t| %s |  | %s |" % (goodName1, goodName2))
    print("\t| HP:  %s |  | HP:  %s |" % (goodHp1, goodHp2))
    print("\t| ATK: %s      |  | ATK: %s      |" % (goodAtk1, goodAtk2))
    print("\t| DEF: %s      |  | DEF: %s      |" % (goodDef1, goodDef2))
    print("\t+--------------+  +--------------+")


def turn(pokemon1, pokemon2):
    """manage battle flow

    let both players attack
    check victory conditions
    """
    printStats(pokemon1, pokemon2)
    attack(1, pokemon1, pokemon2)
    if pokemon2.hp <= 0:
        pokemon2.hp = 0
        print("\n\t%s fainted!" % pokemon2.name)
        print("\tPlayer 1 wins!")
        return 1
    printStats(pokemon1, pokemon2)
    attack(2, pokemon2, pokemon1)
    if pokemon1.hp <= 0:
        pokemon1.hp = 0
        print("\n\t%s fainted!" % pokemon1.name)
        print("\tPlayer 2 wins!")
        return 2
    return 0

# Define the different Pokémon
# Store them in the pokedex array
Pikachu = Pokemon("Pikachu", 100, 36, 10)
Bulbasaur = Pokemon("Bulbasaur", 120, 28, 25)
Charmander = Pokemon("Charmander", 80, 40, 8)
Squirtle = Pokemon("Squirtle", 120, 32, 18)
pokedex = [Pikachu, Bulbasaur, Charmander, Squirtle]

print("\n * WELCOME TO POKEMON ASCII EDITION *")

# Choose pokémon
# Manages exceptions in case of invalid input
while True:
    try:
        print("\n\tPlayer 1 choose Pokémon")
        for i in range(len(pokedex)):
            print("\t\t" + str(i + 1) + ": " + pokedex[i].name)
        choice1 = int(input("\n")) - 1
        pokemon1 = pokedex[choice1]
        del pokedex[choice1]
        break
    except (IndexError, ValueError):
        print("\n\tThat was no valid number. Try again...")
while True:
    try:
        print("\n\tPlayer 2 choose Pokémon")
        for i in range(len(pokedex)):
            print("\t\t" + str(i + 1) + ": " + pokedex[i].name)
        choice2 = int(input("\n")) - 1
        pokemon2 = pokedex[choice2]
        break
    except (IndexError, ValueError):
        print("\n\tThat was no valid number. Try again...")

print("\n * LET THE BATTLE BEGIN *")

while turn(pokemon1, pokemon2) == 0:
    pass

exit = input("\n\nPress Enter to exit...")

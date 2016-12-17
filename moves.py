from random import randint


def tackle(pokemon1, pokemon2):
    """lowers hp of enemy pokémon"""
    print("\n\t" + pokemon1.name + " used Tackle!")
    if randint(1, 10) == 10:
        print("\tBut it missed!")
    else:
        damage = randint(int((pokemon1.attack) / 2), pokemon1.attack)
        pokemon2.hp -= damage
        print("\tIt did %s damage!" % damage)


def growl(pokemon1, pokemon2):
    """lowers attack of enemy pokemon"""
    print("\n\t" + pokemon1.name + " used Growl!")
    if randint(1, 20) == 20:
        print("\tBut it missed!")
    else:
        pokemon2.attack = round(pokemon2.attack * 0.75)
        print("\t" + pokemon2.name + "'s attack was reduced by 25%!")

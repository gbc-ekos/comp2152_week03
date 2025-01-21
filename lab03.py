import random
from math import trunc

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print('Available weapons:')
for weapon in weapons:
    print(weapon)

# Inputs

# Input hero strength
combatStrength = -1
while combatStrength == -1:
    try: # try getting value from user
        usrInput = int(input("Choose hero strength (1-6): "))
        if usrInput in diceOptions: # if valid, accept
            combatStrength = usrInput
        else: # otherwise reject
            raise IndexError
    except IndexError: # User provided a number not in range
        print("Please enter a number between 1-6")
        continue
    except ValueError: # User did not provide a number
        print("Please enter a number.")
        continue

#Input monster strength, same process as hero
mCombatStrength = -1
while mCombatStrength == -1:
    try:
        usrInput = int(input("Choose monster strength (1-6): "))
        if usrInput in diceOptions:
            mCombatStrength = usrInput
        else:
            raise IndexError
    except IndexError:
        print("Please enter a number between 1-6")
        continue
    except ValueError:
        print("Please enter a number.")
        continue


# Simulating battle
for j in range(1, 21, 2):
    heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
    heroTotal, monsterTotal = combatStrength + heroRoll, mCombatStrength + monsterRoll
    print(f"Round {j}: Hero({weapons[heroRoll - 1]})={heroTotal}, Monster({weapons[monsterRoll - 1]})={monsterTotal}.",
          "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
    if j == 11:
        print("Battle Truce declared. Game Over!")
        break

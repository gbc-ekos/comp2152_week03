import random
from math import trunc

# Setup
diceOptions = list(range(1, 7))
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']
# print("Available Weapons:", ', '.join(weapons))
print('Available weapons:')
for weapon in weapons:
    print(weapon)

# Inputs
# combatStrength = max(1, min(6, int(input("Hero strength (1-6): "))))
# mCombatStrength = max(1, min(6, int(input("Monster strength (1-6): "))))

combatStrength = -1
while combatStrength == -1:
    try:
        usrInput = int(input("Choose hero strength (1-6): "))
        if usrInput in diceOptions:
            combatStrength = usrInput
        else:
            raise IndexError
    except IndexError:
        print("Please enter a number between 1-6")
        continue
    except ValueError:
        print("Please enter a number.")
        continue

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


# Battle
for j in range(1, 21, 2):
    heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
    heroTotal, monsterTotal = combatStrength + heroRoll, mCombatStrength + monsterRoll
    print(f"Round {j}: Hero({weapons[heroRoll - 1]})={heroTotal}, Monster({weapons[monsterRoll - 1]})={monsterTotal}.",
          "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
    if j == 11:
        print("Battle Truce declared. Game Over!")
        break

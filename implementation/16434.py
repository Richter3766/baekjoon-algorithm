import sys

def adventureTheDungeon(heroCurHealth):
    heroCurAttackDamage = initialHeroAttackDamage
    heroMaxHealth = heroCurHealth

    for isMonster, attackDamage, health in rooms:
        if isMonster == 1:
            heroCurHealth = fightWithMonster(attackDamage, health, heroCurAttackDamage, heroCurHealth)
            if heroCurHealth <= 0:
                return False
        else:
            heroCurAttackDamage, heroCurHealth = drinkPotion(attackDamage, health, heroCurAttackDamage, heroMaxHealth, heroCurHealth)
    return True


def fightWithMonster(monsterAttackDamage, monsterHealth, heroCurAttackDamage, heroCurHealth):
    turn = monsterHealth // heroCurAttackDamage
    turn += 0 if monsterHealth % heroCurAttackDamage > 0 else -1
    heroCurHealth -= monsterAttackDamage * turn

    return heroCurHealth


def drinkPotion(attackDamage, health, heroCurAttackDamage, heroMaxHealth, heroCurHealth):
    heroCurAttackDamage += attackDamage
    heroCurHealth = heroCurHealth + health if heroCurHealth + health <= heroMaxHealth else heroMaxHealth

    return heroCurAttackDamage, heroCurHealth


numOfRooms, initialHeroAttackDamage = map(int, sys.stdin.readline().split())
rooms = [list(map(int, sys.stdin.readline().split())) for i in range(numOfRooms)]

leftHeroHealth = 0
rightHeroHealth = (10 ** 12) * numOfRooms
while True:
    curHeroHealth = (rightHeroHealth + leftHeroHealth) // 2
    if curHeroHealth == leftHeroHealth:
        break

    isClear = adventureTheDungeon(curHeroHealth)
    if isClear:
        rightHeroHealth = curHeroHealth
    else:
        leftHeroHealth = curHeroHealth

print(int(rightHeroHealth))
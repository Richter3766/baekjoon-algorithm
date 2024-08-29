import sys


def monsterInRoom(monsterAttackDamage, monsterHealth):
    global heroCurHealth
    global heroCurAttackDamage

    turn = monsterHealth // heroCurAttackDamage
    leftHealth = monsterHealth % heroCurAttackDamage
    turn += 0 if leftHealth > 0 else -1
    heroCurHealth -= monsterAttackDamage * turn

def whenHeroDie():
    global heroMaxHealth
    global heroCurHealth
    global heroCurAttackDamage
    global roomId

    if heroCurHealth <= 0:
        heroMaxHealth += -heroCurHealth + 1
        heroCurHealth = heroMaxHealth
        heroCurAttackDamage = initialHeroAttackDamage
        roomIdx = -1


def potionInRoom(increaseAttackDamageAmount, health):
    global heroMaxHealth
    global heroCurHealth
    global heroCurAttackDamage

    heroCurAttackDamage += increaseAttackDamageAmount
    heroCurHealth = heroCurHealth + health if heroCurHealth + health <= heroMaxHealth else heroMaxHealth


numOfRooms, initialHeroAttackDamage = map(int, sys.stdin.readline().split())
rooms = [list(map(int, sys.stdin.readline().split())) for i in range(numOfRooms)]

heroMaxHealth = 0
heroCurHealth = 0
heroCurAttackDamage = initialHeroAttackDamage

roomIdx = -1

while roomIdx < numOfRooms:
    roomIdx += 1
    if roomIdx == numOfRooms:
        break
    case, attackDamage, health = rooms[roomIdx]

    if case == 1:
        monsterInRoom(attackDamage, health)
        whenHeroDie()
    else:
        potionInRoom(attackDamage, health)

print(heroMaxHealth)
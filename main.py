from random import randint, choice
from time import sleep
from functions import *

playerHealth = Player.healthCreator()
playerDefence = Player.defenceScore()
print("YOU HAVE: " +str(playerHealth)+ " HP")
print("YOU HAVE: "+str(playerDefence)+ " Defence Score")
enemyAttacks = ["Punch", "kick", "scratch", "pistol"]
alive = True
survived = 0
currentwave = 1
while alive == True:
  enemyHP = Enemy.healthCreator()
  enemyDefence = Enemy.defenceScore()
  inCombat = True
  while inCombat == True:
    print("===== PLAYER ATTACK =====")
    attack = input("You attack with: ")
    print("Roll to hit")
    sleep(1)
    playerRoll = Player.rollToHit()
    print("you rolled: "+str(playerRoll))
    sleep(0.5)
    if enemyDefence > playerRoll:
      print("YOU MISSED")
    else:
      print("Roll damage")
      playerDamage = Player.damage()
      print("You dealt: " +str(playerDamage)+" damage")
      enemyHP = enemyHP - playerDamage
      sleep(0.5)
      print("Enemy has: " +str(enemyHP) + " remaining")
      if enemyHP <= 0:
        inCombat = False
        survived = survived+1
        currentwave = currentwave +1
        print("YOU WIN THIS BATTLE")
        print("New battle generating")
        inCombat = False

    sleep(0.5)
    print("===== ENEMY ATTACK =====")
    print("Enemy attacks you with: " +choice(enemyAttacks))
    sleep(0.5)
    print("roll to hit")
    enemyRoll = Enemy.rollToHit()
    sleep(0.5)
    if playerDefence > enemyRoll:
      print("ENEMY MISSED")
    else:
      print("Roll Damage")
      enemyDamage = Enemy.damage()
      sleep(0.5)
      playerHealth = playerHealth - enemyDamage
      print("ENEMY DEALT: "+str(enemyDamage)+ "damage")
      print("YOU HAVE: "+str(playerHealth)+ " remaining")
      if playerHealth <= 0:
        print("YOU LOSE")
        inCombat = False
        alive = False


print("END OF GAME!")
print("You survived " +str(survived)+"waves")
print("you made it to wave: " +str(currentwave))
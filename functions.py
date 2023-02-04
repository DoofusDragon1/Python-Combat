from random import randint
from time import sleep

#The Player class defines the attributes the player needs to play.
class Player:
  def healthCreator():
    health = randint(30,100)
    return health

  def rollToHit():
    rollToHit = randint(1,20)
    return rollToHit

  def damage():
    damageRoll = randint(1,20)
    if damageRoll >= 18:
      damageRoll = damageRoll * 1.2
    return damageRoll

  def defenceScore():
    score = randint(1,19)
    return score


#the second class defines the Enemies and their stats
#NOTE: these are regenerated each wave
class Enemy:
  def healthCreator():
    health = randint(10,50)
    return health

  def rollToHit():
    roll = randint(1,20)
    return roll

  def damage():
    damageRoll = randint(1,20)
    if damageRoll >= 18:
      damageRoll = damageRoll * 1.2
    return damageRoll

  def defenceScore():
    score = randint(1,19)
    return score
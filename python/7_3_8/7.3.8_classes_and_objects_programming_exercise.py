import sys

class Hero():
  health = 100
  attack_damage = 20
  healing_increase = 50
  
  def drink_potion(self):
      self.health += self.healing_increase
      print("Just healed!")
      print(">> Hero's health is: %s\n" % self.health)

  def attack_monster(self, name): # we pass the monsters instatiated object as a arg
      print("Take that you monster")
      name.health -= self.attack_damage
      print("Monster's health: %s\n" % name.health)
      
      if name.health < 30:
          print("Begone you beast")
          print(">> The monster ran away")
          sys.exit


class Monster():
  health = 100
  attack_damage = 30

  def roar(self):
      print("Roaar")

  def attack_hero(self, name): # we pass the heros instatiated object as a arg
      print("Roarrr x2")
      name.health -= self.attack_damage
      print("Hero's health: %s\n" % name.health)

      if name.health <= 0:
          print("roarrr x3")
          print(">> The hero freaking died yo")
          sys.exit


warrior = Hero()
beast = Monster()

# Start of our story...
print("A monster leaps from its cave and strikes our hero!\n")
beast.attack_hero(warrior)
warrior.attack_monster(beast)
beast.attack_hero(warrior)
warrior.drink_potion()
beast.roar()
warrior.attack_monster(beast)
warrior.attack_monster(beast)
beast.attack_hero(warrior)
warrior.attack_monster(beast)

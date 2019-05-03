from animals.animal import animal
import random

class turtle(animal):
	def __init__(self, x, y, world):
		self.str = 2
		self.init = 1
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Turtle"
		self.color = "dark green"
		self.world = world

	def action(self):
		move = random.randint(0,3)
		if move == 0:
			animal.action(self)

	def collision(self, attacker):
		if attacker.str >= 5 or attacker.name == self.name:
			animal.collision(self, attacker)
		else:
			print(attacker.name + " is too weak to defeat " + self.name)

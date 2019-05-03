from animals.animal import animal
import random

class antelope(animal):
	def __init__(self, x, y, world):
		self.str = 4
		self.init = 4
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Antelope"
		self.color = "brown"
		self.world = world

	def action(self):
		add_x = 0
		add_y = 0
		while 1 > 0:
			add_x = random.randint(-1,1)
			add_y = random.randint(-1,1)
			if add_x + add_y == 1 or add_x + add_y == -1:
				add_x *= 2
				add_y *= 2
				if self.x+add_x >= 0 and self.x+add_x < self.world.map_size and self.y+add_y >= 0 and self.y+add_y < self.world.map_size:
					break
		if not self.world.check(self.x+add_x, self.y+add_y):
			self.world.clear_field(self.x+self.y*self.world.map_size)
			self.x += add_x
			self.y += add_y
			self.age += 1
			self.draw()
		else:
			tmp = self.world.find_victim(self.x+add_x, self.y+add_y)
			tmp.collision(self)

	def collision(self, attacker):
		escape = random.randint(0,1)
		if escape == 0 or attacker.name == self.name:
			animal.collision(self, attacker)
		else:
			tmp_x = attacker.x
			tmp_y = attacker.y
			attacker.x = self.x
			attacker.y = self.y
			self.x = tmp_x
			self.y = tmp_y
			attacker.age += 1
			self.draw()
			attacker.draw()
			print(self.name + " escaped from " + attacker.name)

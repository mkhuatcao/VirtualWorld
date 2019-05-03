from animals.animal import animal
import random

class fox(animal):
	def __init__(self, x, y, world):
		self.str = 3
		self.init = 7
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Fox"
		self.color = "orange"
		self.world = world

	def action(self):
		add_x = 0
		add_y = 0
		while 1 > 0:
			add_x = random.randint(-1,1)
			add_y = random.randint(-1,1)
			if add_x + add_y == 1 or add_x + add_y == -1:
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
			if tmp.str <= self.str:
				tmp.collision(self)

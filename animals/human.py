from animals.animal import animal

class human(animal):
	def __init__(self, x, y, world):
		self.str = 5
		self.init = 4
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Human"
		self.color = "indigo"
		self.world = world

	def action(self):
		add_x = 0
		add_y = 0
		direction = self.world.label.get_text()
		if direction == "UP":
			add_y = -1
		elif direction == "DOWN":
			add_y = 1
		elif direction == "LEFT":
			add_x = -1
		elif direction == "RIGHT":
			add_x = 1
		if not self.world.check(self.x+add_x, self.y+add_y):
			self.world.clear_field(self.x+self.y*self.world.map_size)
			self.x += add_x
			self.y += add_y
			self.age += 1
			self.draw()
		else:
			tmp = self.world.find_victim(self.x+add_x, self.y+add_y)
			if self.world.immortality > 5 and tmp.str > self.str:
				self.age += 1
				print(self.name + " attacked " + tmp.name + " and immortality saved him.")
			else:
				tmp.collision(self)

	def collision(self, attacker):
		if self.world.immortality < 6:
			animal.collision(self, attacker)
		else:
			tmp_x = attacker.x
			tmp_y = attacker.y
			attacker.x = self.x
			attacker.y = self. y
			self.x = tmp_x
			self.y = tmp_y
			attacker.age += 1
			self.draw()
			attacker.draw()
			print(self.name + " is immortal. " + attacker.name + " can't deal with that.")

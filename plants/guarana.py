from plants.plant import plant

class guarana(plant):
	def __init__(self, x, y, world):
		self.str = 0
		self.init = 0
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Guarana"
		self.color = "red"
		self.world = world

	def collision(self, attacker):
		plant.collision(self, attacker)
		attacker.str += 3

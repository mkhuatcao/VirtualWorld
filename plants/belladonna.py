from plants.plant import plant

class belladonna(plant):
	def __init__(self, x, y, world):
		self.str = 99
		self.init = 0
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Belladonna"
		self.color = "black"
		self.world = world

	def collision(self, attacker):
		plant.collision(self, attacker)
		self.world.clear_field(attacker.x+attacker.y*self.world.map_size)
		attacker.ifAlive = False
		attacker.x = -1
		attacker.y = -1
		print(attacker.name + " died beacuse of poisoning")

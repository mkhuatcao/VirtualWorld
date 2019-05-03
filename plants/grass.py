from plants.plant import plant

class grass(plant):
	def __init__(self, x, y, world):
		self.str = 0
		self.init = 0
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Grass"
		self.color = "green"
		self.world = world

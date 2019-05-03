from animals.animal import animal

class sheep(animal):
	def __init__(self, x, y, world):
		self.str = 4
		self.init = 4
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Sheep"
		self.color = "antique white"
		self.world = world

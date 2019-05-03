from animals.animal import animal

class wolf(animal):
	def __init__(self, x, y, world):
		self.str = 9
		self.init = 5
		self.x = x
		self.y = y
		self.age = 0
		self.name = "Wolf"
		self.color = "gray"
		self.world = world

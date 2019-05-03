from plants.plant import plant

class sow_thistle(plant):
	def __init__(self, x, y, world):
		self.str = 0
		self.init = 0
		self.x = x
		self.y = y
		self.age = 0
		self.name = "SowThistle"
		self.color = "yellow"
		self.world = world

	def action(self):
		for i in range(3):
			plant.action(self)
		self.age -= 2

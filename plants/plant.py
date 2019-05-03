from abc import ABCMeta
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import random

class plant:
	__metaclass__ = ABCMeta
	ifAlive = True
	
	def draw(self):
		tmp = self.x + self.y*self.world.map_size
		color_rgba = Gdk.RGBA()
		Gdk.RGBA.parse(color_rgba, self.color)
		self.world.map[tmp].override_background_color(Gtk.StateFlags(0), color_rgba)

	def action(self):
		seed = random.randint(0, 9)
		self.age += 1
		if seed == 0:
			end = False
			i = -1
			while i < 2:
				j = -1
				while j < 2:
					if self.x+j >= 0 and self.x+j < self.world.map_size and self.y+i >= 0 and self.y+i < self.world.map_size:
						if not self.world.check(self.x+j, self.y+i):
							self.world.creat_organism(self.x+j, self.y+i, self.name)
							self.world.count += 1
							self.world.organisms[self.world.count].draw()
							print("New " + self.name)
							end = True
							break
					j += 1
				if end:
					break
				i += 1

	def collision(self, attacker):
		self.world.clear_field(attacker.x+attacker.y*self.world.map_size)
		attacker.x = self.x
		attacker.y = self.y
		attacker.age += 1
		attacker.draw()
		self.ifAlive = False
		self.x = -1
		self.y = -1
		print(attacker.name + " ate " + self.name)

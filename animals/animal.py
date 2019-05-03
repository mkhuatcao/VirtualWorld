from abc import ABCMeta
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import random

class animal:
	__metaclass__ = ABCMeta
	ifAlive = True

	def draw(self):
		tmp = self.x + self.y*self.world.map_size
		color_rgba = Gdk.RGBA()
		Gdk.RGBA.parse(color_rgba, self.color)
		self.world.map[tmp].override_background_color(Gtk.StateFlags(0), color_rgba)

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
			tmp.collision(self)

	def collision(self, attacker):
		if attacker.name == self.name:
			end = False
			i = -1
			while i < 2:
				j = -1
				while j < 2:
					if self.x+j >= 0 and self.x+j < self.world.map_size and self.y+i >= 0 and self.y+i <self.world.map_size:
						if not self.world.check(self.x+j, self.y+i):
							self.world.creat_organism(self.x+j, self.y+i, self.name)
							self.world.count += 1
							self.world.organisms[self.world.count].draw()
							print("New " + self.name)
							end = True
							break
					if attacker.x+j >= 0 and attacker.x+j < self.world.map_size and attacker.y+i >= 0 and attacker.y+i <self.world.map_size:
						if not self.world.check(attacker.x+j, attacker.y+i):
							self.world.creat_organism(attacker.x+j, attacker.y+i, attacker.name)
							self.world.count += 1
							self.world.organisms[self.world.count].draw()
							print("New " + self.name)
							end = True
							break
					j += 1
				if end:
					break
				i += 1
		elif attacker.str >= self.str:
			self.world.clear_field(attacker.x+attacker.y*self.world.map_size)
			attacker.x = self.x
			attacker.y = self.y
			attacker.age += 1
			attacker.draw()
			self.ifAlive = False
			self.x = -1
			self.y = -1
			print(attacker.name + " killed " + self.name)
		else:
			self.world.clear_field(attacker.x+attacker.y*self.world.map_size)
			attacker.ifAlive = False
			attacker.x = -1
			attacker.y = -1
			print(attacker.name + " died while attacking " + self.name)

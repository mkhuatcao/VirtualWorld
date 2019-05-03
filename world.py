#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

import plants
import animals

class world(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Virtual world")
        self.connect("delete-event", Gtk.main_quit)
        self.set_size_request(800, 600)
        self.layout = Gtk.Layout()
        self.add(self.layout)
        self.count = 0
        self.immortality = 0
        self.organisms = []
        self.organisms.append(None)
        self.map = []
        self.white_color = Gdk.RGBA()
        Gdk.RGBA.parse(self.white_color, "white")
        self.map_size = 20

        for i in range(self.map_size):
            for j in range(self.map_size):
                tmp = Gtk.EventBox()
                tmp.set_size_request(25, 25)
                self.layout.put(tmp, 50 + j * 25, 50 + i * 25)
                tmp.override_background_color(Gtk.StateFlags(0), self.white_color)
                tmp.connect("button_press_event", self.add_on_click, j, i)
                self.map.append(tmp)
        button = Gtk.Button("Load")
        button.connect("clicked", self.load)
        button.set_size_request(100, 30)
        self.layout.put(button, 10, 10)
        button = Gtk.Button("Save")
        button.connect("clicked", self.save)
        button.set_size_request(100, 30)
        self.layout.put(button, 140, 10)
        button = Gtk.Button("Next Round")
        button.connect("clicked", self.next_round_pressed)
        button.set_size_request(100, 30)
        self.layout.put(button, 10, 560)
        self.label = Gtk.Label("")
        self.layout.put(self.label, 550, 30)
        self.ult_button = Gtk.Button("Immortality")
        self.ult_button.connect("clicked", self.ultimate)
        self.layout.put(self.ult_button, 600, 10)
        self.connect('key_press_event', self.arrow_pressed)
        self.show_all()

    def main(self):
        Gtk.main()

    def creat_organism(self, x, y, name):
        if name == "Antelope":
            a = animals.antelope(x, y, self)
            self.organisms.append(a)
        elif name == "Belladonna":
            a = plants.belladonna(x, y, self)
            self.organisms.append(a)
        elif name == "Fox":
            a = animals.fox(x, y, self)
            self.organisms.append(a)
        elif name == "Grass":
            a = plants.grass(x, y, self)
            self.organisms.append(a)
        elif name == "Guarana":
            a = plants.guarana(x, y, self)
            self.organisms.append(a)
        elif name == "Human":
            a = animals.human(x, y, self)
            self.organisms.append(a)
        elif name == "Sheep":
            a = animals.sheep(x, y, self)
            self.organisms.append(a)
        elif name == "SowThistle":
            a = plants.sow_thistle(x, y, self)
            self.organisms.append(a)
        elif name == "Turtle":
            a = animals.turtle(x, y, self)
            self.organisms.append(a)
        elif name == "Wolf":
            a = animals.wolf(x, y, self)
            self.organisms.append(a)

    def compare(self, a, b):
        if a.init < b.init:
            return True
        elif a.init == b.init:
            if a.age < b.age:
                return True
        return False

    def heapify(self, i, size):
        lft = i * 2
        rgt = lft + 1
        smallest = None
        if lft <= size and self.compare(self.organisms[lft], self.organisms[i]):
            smallest = lft
        else:
            smallest = i
        if rgt <= size and self.compare(self.organisms[rgt], self.organisms[smallest]):
            smallest = rgt
        if smallest != i:
            tmp = self.organisms[i]
            self.organisms[i] = self.organisms[smallest]
            self.organisms[smallest] = tmp

    def sort(self):
        i = self.count
        while i > 1:
            j = i // 2
            while j > 0:
                self.heapify(j, i)
                j -= 1
            tmp = self.organisms[1]
            self.organisms[1] = self.organisms[i]
            self.organisms[i] = tmp
            i -= 1

    def next_round(self):
        self.sort()
        tmp = self.count
        i = 1
        while i <= tmp:
            if self.organisms[i].ifAlive:
                self.organisms[i].action()
            i += 1
        i = 1
        while i <= self.count:
            if not self.organisms[i].ifAlive:
                del self.organisms[i]
                i -= 1
                self.count -= 1
            i += 1
        if self.immortality == 1:
            self.ult_button.show()
        else:
            self.immortality -= 1

    def next_round_pressed(self, button):
        tmp = self.find_human()
        if tmp == None:
            self.next_round()
        else:
            if self.if_human_move(tmp):
                self.next_round()
            else:
                print("Illegal move with human. Choose different direction.")

    def find_human(self):
        for organism in self.organisms[1:]:
            if organism.name == "Human":
                return organism
        return None

    def if_human_move(self, human):
        add_x = 0
        add_y = 0
        direction = self.label.get_text()
        if direction == "UP":
            add_y = -1
        elif direction == "DOWN":
            add_y = 1
        elif direction == "LEFT":
            add_x = -1
        elif direction == "RIGHT":
            add_x = 1
        else:
            return False
        if human.x + add_x >= 0 and human.x + add_x < self.map_size and human.y + add_y >= 0 and human.y + add_y < self.map_size:
            return True
        else:
            return False

    def check(self, x, y):
        for organism in self.organisms[1:]:
            if organism.x == x and organism.y == y:
                return True
        return False

    def clear_field(self, n):
        self.map[n].override_background_color(Gtk.StateFlags(0), self.white_color)

    def find_victim(self, x, y):
        for organism in self.organisms[1:]:
            if organism.x == x and organism.y == y:
                return organism

    def load(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a file", self, Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            for i in range(self.count, 0, -1):
                x = self.organisms[i].x
                y = self.organisms[i].y
                self.clear_field(x + y * self.map_size)
                del self.organisms[i]
                self.count -= 1
            my_file = open(dialog.get_filename(), "r")
            info = my_file.read()
            info = info.split('\n')
            for item in info:
                if item != "":
                    a = item.split('*')
                    self.creat_organism(int(a[0]), int(a[1]), a[2])
                    self.count += 1
                    self.organisms[self.count].draw()
            my_file.close()
            self.ult_button.show()
            self.immortality = 0
        dialog.destroy()

    def save(self, button):
        dialog = Gtk.FileChooserDialog("Save to", self, Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            my_file = open(dialog.get_filename(), "w")
            for organism in self.organisms[1:]:
                my_file.write(str(organism.x) + "*" + str(organism.y) + "*" + organism.name + "\n")
            my_file.close()
        dialog.destroy()

    def arrow_pressed(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)
        if keyname == "Up":
            self.label.set_text("UP")
        elif keyname == "Right":
            self.label.set_text("RIGHT")
        elif keyname == "Down":
            self.label.set_text("DOWN")
        elif keyname == "Left":
            self.label.set_text("LEFT")

    def ultimate(self, button):
        self.immortality = 10
        button.hide()

    def add_on_click(self, widget, event, x, y):
        if self.check(x,y):
            print("This place is taken choose another")
            return None
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, 0, "Choose organism")
        dialog.add_button("Antelope", 0)
        dialog.add_button("Belladonna", 1)
        dialog.add_button("Fox", 2)
        dialog.add_button("Grass", 3)
        dialog.add_button("Guarana", 4)
        dialog.add_button("Human", 5)
        dialog.add_button("Sheep", 6)
        dialog.add_button("Sow Thistle", 7)
        dialog.add_button("Turtle", 8)
        dialog.add_button("Wolf", 9)
        response = dialog.run()
        if response == 0:
            self.creat_organism(x, y, "Antelope")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 1:
            self.creat_organism(x, y, "Belladonna")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 2:
            self.creat_organism(x, y, "Fox")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 3:
            self.creat_organism(x, y, "Grass")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 4:
            self.creat_organism(x, y, "Guarana")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 5:
            while True:
                try:
                    tmp = self.find_human()
                    if tmp == None:
                        self.creat_organism(x, y, "Human")
                        self.count += 1
                        self.organisms[self.count].draw()
                    else:
                        raise self.human_exists
                    break
                except self.human_exists:
                    print("There is place only for one human there. Please choose something else")
                    break
        elif response == 6:
            self.creat_organism(x, y, "Sheep")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 7:
            self.creat_organism(x, y, "SowThistle")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 8:
            self.creat_organism(x, y, "Turtle")
            self.count += 1
            self.organisms[self.count].draw()
        elif response == 9:
            self.creat_organism(x, y, "Wolf")
            self.count += 1
            self.organisms[self.count].draw()
        dialog.destroy()

    class human_exists(Exception):
        pass


if __name__ == "__main__":
    program = world()
    program.main()

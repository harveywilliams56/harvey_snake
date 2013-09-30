
import time
import curses
from GamingPage import *
from Opponent import *
import curses.wrapper
class GameSelectionPage:
	def __init__(self, screen):
		self.screen = screen
		self.draw_area = DrawArea(screen)

		self.menu_items = 3
		self.menu_ys = [40, 37, 34]
		self.menu_texts = ["1 Snake", "2 Snakes", "Networked"]
		self.game_type = [1, 2, "N"]
		self.current_item = 1
		screen.nodelay(1)

	def draw_menu_text(self):

	      	self.draw_area.draw_str(25, 45, "SELECT GAME TYPE")

	      	text_x = 22

	      	for i in range(self.menu_items):
		 	self.draw_area.draw_str(text_x,self.menu_ys[i], self.menu_texts[i])

	def draw_loop(self):
		while True:

			keys = self.key_list()
			for key in keys:
				if key == curses.KEY_UP:
					self.move_pointer_up()
				if key == curses.KEY_DOWN:
					self.move_pointer_down()
				if key in [ord("\n"), ord(" ")]:
					game_type = self.game_type[self.current_item]
					return Opponent(self.screen, self, game_type)
				if key == ord("r"):
					return None

			self.draw_area.clear()
			
			self.draw_menu_text()
			self.draw_menu_pointer()
			
			self.draw_area.paint_to_screen()

			time.sleep(0.001)

	def move_pointer_down(self): 
		if self.current_item < self.menu_items - 1:
		 	self.current_item += 1

	def move_pointer_up(self): 
		if self.current_item > 0:
		 	self.current_item += -1

	def draw_menu_pointer(self):

		pointer_x = 42
		pointer_text = "<--"

		pointer_y = self.menu_ys[self.current_item]

		self.draw_area.draw_str(pointer_x, pointer_y, pointer_text)

	def key_list(self):
		key_list = []
		switch = True
		while switch:
			key = self.screen.getch()
			if key == curses.ERR:
				switch = False
			else:
				key_list += [key]
		return key_list

#if __name__ == "__main__":
  # curses.wrapper(test_main)

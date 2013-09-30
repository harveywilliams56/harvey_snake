
import time
import curses
from GamingPage import *
from SpeedMenuPage import *
import curses.wrapper
class Opponent:
	def __init__(self, screen, quit_page, nmbr_players):
		self.screen = screen
		self.draw_area = DrawArea(screen)
		self.quit_page = quit_page
		self.nmbr_players = nmbr_players

		self.menu_items = 2
		self.menu_ys = [38,36]
		self.menu_texts = ["Human", "Computer"]
		self.game_type = ["Hum", "Comp"]
		self.current_item = 1
		screen.nodelay(1)

	def draw_menu_text(self):

	      	self.draw_area.draw_str(25, 45, "SELECT OPPONENT")

	      	text_x = 22

	      	for i in range(self.menu_items):
		 	self.draw_area.draw_str(text_x,self.menu_ys[i], self.menu_texts[i])

	def draw_loop(self):
		while self.nmbr_players == 2:

			keys = self.key_list()
			for key in keys:
				if key == curses.KEY_UP:
					self.move_pointer_up()
				if key == curses.KEY_DOWN:
					self.move_pointer_down()
				if key in [ord("\n"), ord(" ")]:
					game_type = self.game_type[self.current_item]
					return SpeedMenuPage(self.screen, self, game_type)
				if key == ord("r"):
					return self.quit_page

			self.draw_area.clear()
			
			self.draw_menu_text()
			self.draw_menu_pointer()
			
			self.draw_area.paint_to_screen()

			time.sleep(0.001)
		return SpeedMenuPage(self.screen, self.quit_page, self.nmbr_players)
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

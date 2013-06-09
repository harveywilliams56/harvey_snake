
import curses.wrapper
import time
from DrawArea import *
from Snake import *
import sys
from Egg import *
from Player import *

class GameLoop:
	def __init__(self, screen):
		self.screen = screen
		self.draw_area = DrawArea(screen)
		self.x = self.draw_area.width / 4
		self.y = self.draw_area.height / 2
		self.d = 3
		self.l = 5
		self.players = []
		self.map0 = {	ord('w') : 3,
				ord('a') : 4,
				ord('s') : 1,
				ord('d') : 2}
		self.map1 = {	curses.KEY_UP : 3,
				curses.KEY_LEFT : 4,
				curses.KEY_DOWN : 1,
				curses.KEY_RIGHT : 2}
		self.player0 = Player(self.x,self.y,self.d, self.l, self.map0,self.draw_area,True)
		self.player1 = Player(9, 9, 1, 5, self.map1, self.draw_area,False)
		self.pause = 1000
		self.player0.add_to_obstacles(self.player0.snake)
		self.player0.add_to_obstacles(self.player1.snake)
		self.player1.add_to_obstacles(self.player0.snake)
		self.player1.add_to_obstacles(self.player1.snake)
		self.egg = Egg(self.draw_area, 9, 9)
		self.player0.add_to_food(self.egg)
		self.player1.add_to_food(self.egg)
	#Get list of keys since last gameloop
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

	def run(self):

		# Make getch() Non-Blocking
		self.screen.nodelay(1)
		while True:

			# Check for user input
			keys = self.key_list()
			dir = self.player0.key_decode(keys)
			self.player0.snake.change_direction(dir)
			dir = self.player1.key_decode(keys)
			self.player1.snake.change_direction(dir)

			# redraw the screen
			self.draw_area.clear()

			self.player0.player_functions()
			self.player1.player_functions()
			self.egg.draw()
			
			self.draw_area.paint_to_screen()
			
			# wait
			time.sleep(0.125)

def test_main(screen):
	
	gameloop = GameLoop(screen)

	gameloop.run()

if __name__ == "__main__":
	curses.wrapper(test_main)

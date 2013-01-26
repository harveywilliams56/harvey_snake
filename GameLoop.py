
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
		self.d = 'u'
		self.l = 5
		self.players = []
		self.map0 = {	ord('w') : 'u',
				ord('a') : 'l',
				ord('s') : 'd',
				ord('d') : 'r'}
		self.map1 = {	ord('u') : 'u',
				ord('h') : 'l',
				ord('j') : 'd',
				ord('k') : 'r'}

		self.player0 = Player(self.x, self.y, self.d, self.l, self.map0,self.draw_area)
		self.player1 = Player(9, 9, 'd', 5, self.map1, self.draw_area)
		self.pause = 1000
		self.player0.add_to_obstacles(self.player0.snake)
		self.player0.add_to_obstacles(self.player1.snake)
		self.player1.add_to_obstacles(self.player0.snake)
		self.player1.add_to_obstacles(self.player1.snake)
		self.egg = Egg(self.draw_area, 9, 9)
		self.player0.add_to_food(self.egg)
		self.player1.add_to_food(self.egg)

	def get_newest_key(self):
		nwstk = curses.ERR
		switch = True
		while switch:
			key = self.screen.getch()
			if key == curses.ERR:
				switch = False
			else:
				nwstk = key
		return nwstk
		
	def run(self):

		# Make getch() Non-Blocking
		self.screen.nodelay(1)
		while True:

			# Check for user input
			key = self.get_newest_key()
			if key != curses.ERR:
				dir = self.player0.key_decode(key)
				self.player0.snake.change_direction(dir)
				dir = self.player1.key_decode(key)
				self.player1.snake.change_direction(dir)


			# update object positions
			
			self.player0.snake.move()
			self.player1.snake.move()

			#collision detection here	
			self.player0.collision_detection()
			self.player1.collision_detection()
			# redraw the screen
			self.draw_area.clear()
			self.player0.draw()
			self.player1.draw()
			self.egg.draw()
			
			self.draw_area.paint_to_screen()
			
			# wait
			time.sleep(0.125)

def test_main(screen):
	
	gameloop = GameLoop(screen)

	gameloop.run()

if __name__ == "__main__":
	curses.wrapper(test_main)

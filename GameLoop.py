
import curses.wrapper
import time
from DrawArea import *
from Snake import *
import sys
from Egg import *

class GameLoop:
	def __init__(self, screen):
		self.screen = screen
		self.draw_area = DrawArea(screen)

		self.snake = Snake(self.draw_area)

		self.pause = 1000

		self.egg = Egg(self.draw_area, 9, 9)
	
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
	def key_decode(self,key):
		
		if key == curses.KEY_UP: dir = 'u'
		elif key == curses.KEY_DOWN: dir = 'd'
		elif key == curses.KEY_LEFT: dir = 'l'
		elif key == curses.KEY_RIGHT: dir = 'r'
		return dir
	
	def run(self):

		score = 0

		# Make getch() Non-Blocking
		self.screen.nodelay(1)
		while True:

			# Check for user input
			key = self.get_newest_key()
			if key != curses.ERR:
				dir = self.key_decode(key)
				self.snake.change_direction(dir)
	
			# Update Object Positions
			self.snake.move()
			
			#Collision detection here	
			if self.snake.has_hit(self.snake):
				while True: pass
			if self.snake.has_hit(self.egg):
				self.egg.teleport()
				score = score + 100
			
			# Redraw The Screen
			self.draw_area.clear()
			self.snake.draw()
			self.egg.draw()
			score_str = "Score: %i" % (score)
			self.draw_area.draw_str(0, self.draw_area.height-1, score_str)
			self.draw_area.paint_to_screen()
			
			# Wait
			#time.sleep(self.pause * 0.0001)
			time.sleep(0.125)
			
			

def test_main(screen):
	
	gameloop = GameLoop(screen)

	gameloop.run()

if __name__ == "__main__":
	curses.wrapper(test_main)

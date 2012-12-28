
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

		self.snakes = []
		self.snakes.append(Snake(self.draw_area))
		self.snakes.append(Snake(self.draw_area))

		for i in range(len(self.snakes)):
			self.reset_snake(i)

		self.decoders = []
		self.decoders.append(self.key_decode1)
		self.decoders.append(self.key_decode)

		self.pause = 1000

		self.egg = Egg(self.draw_area, 9, 9)

	def reset_snake(self, index):
	
		snake = self.snakes[index]

		y = self.draw_area.height / 2	
		l = 4

		if index == 0:
			x = self.draw_area.width / 4
			d = 'u'
		if index == 1:
			x = (self.draw_area.width * 3) / 4
			d = 'd'	
	
		snake.reset(x, y, l, d)
	
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
		dir = None	
		if key == curses.KEY_UP: dir = 'u'
		elif key == curses.KEY_DOWN: dir = 'd'
		elif key == curses.KEY_LEFT: dir = 'l'
		elif key == curses.KEY_RIGHT: dir = 'r'
		return dir

	def key_decode1(self, key):
		dir = None
		if key == ord('w'): dir = 'u'
		elif key == ord('s'): dir = 'd'
		elif key == ord('a'): dir = 'l'
		elif key == ord('d'): dir = 'r'
		return dir
		
	def run(self):

		score = 0
		score1 = 0

		# Make getch() Non-Blocking
		self.screen.nodelay(1)
		while True:

			# Check for user input
			key = self.get_newest_key()
			if key != curses.ERR:
				for i in range(len(self.snakes)):
					func = self.decoders[i]
					dir = func(key)
					if dir != None:
						self.snakes[i].change_direction(dir)
	
			# Update Object Positions
			for s in self.snakes:
				s.move()

			#Collision detection here	
			for s in self.snakes:
				if s.has_hit(self.egg):
					self.egg.teleport()
					s.growth = True	
					index = self.snakes.index(s)
					if index == 0:	
						score = score + 1
					if index == 1:
						score1 = score1 + 1

				for s1 in self.snakes:
					if s.has_hit(s1):
						index = self.snakes.index(s)
						self.reset_snake(index)
		
			# Redraw The Screen
			self.draw_area.clear()
			
			for s in self.snakes:
				s.draw()
			self.egg.draw()
			score_str = "Score: %i" % (score)
			self.draw_area.draw_str(0, self.draw_area.height-1, score_str)
			
			score_str1 = "Score: %i" % (score1)
			self.draw_area.draw_str(self.draw_area.width-len(score_str1),
				self.draw_area.height-1, score_str1)

			self.draw_area.paint_to_screen()
			
			
			# Wait
			#time.sleep(self.pause * 0.0001)
			time.sleep(0.125)
			
			

def test_main(screen):
	
	gameloop = GameLoop(screen)

	gameloop.run()

if __name__ == "__main__":
	curses.wrapper(test_main)

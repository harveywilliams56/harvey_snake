

import curses.wrapper
from DrawArea import *
from Snake import *
from GameLoop import *


class Player: 
	def __init__(self,x,y,d,l,map,draw_area):
		self.draw_area = draw_area
		self.food_list = [] 
		self.obst_list = []
		self.snake = Snake(draw_area, x, y, d, l)
		self.add_to_obstacles(self.snake)
		self.x = x
		self.y = y
		self.d = d
		self.l = l
		self.score = 0
		self.map = map

	
	def key_decode(self,key):
		if key in self.map:
			return self.map[key]
	
	def add_to_food(self,munchies):
		self.food_list.append(munchies)
	def add_to_obstacles(self,obst):
		self.obst_list.append(obst)
	
	def reset_snake(self):
		self.snake.reset(self.x, self.y, self.d, self.l)	
	def collision_detection(self):
		for snack in self.food_list:
			if self.snake.has_hit(snack):
				snack.teleport()
				self.snake.growth = True
				self.score += 1
		for barrier in self.obst_list:
			if self.snake.has_hit(barrier):
				self.reset_snake()
	def draw(self):
		self.snake.draw()
		
		score_str = "Score: %i" % (self.score)
		self.draw_area.draw_str(0, self.draw_area.height-1, score_str)

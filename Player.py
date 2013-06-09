
import curses.wrapper
from DrawArea import *
from Snake import *
from GameLoop import *
from random import randrange
class Player: 
	def __init__(self ,x,y,d,l,map,draw_area,query):
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
		self.query = query
		self.transistor = 2
		self.counter = 0
		self.trigger = 1
	#takes a list of keys
	#return newest revelant key as a direction
	def key_decode(self,keys):
		for key in reversed(keys):
			if key in self.map:
				return self.map[key]
		return ""
	
	def add_to_food(self,munchies):
		self.food_list.append(munchies)
	def add_to_obstacles(self,obst):
		self.obst_list.append(obst)
	
	def reset_snake(self):
		xposition = randrange(self.l ,self.draw_area.width -self.l)
		yposition = randrange(self.l ,self.draw_area.height -self.l)
		 
		self.snake.reset(xposition,yposition , randrange(1,5), self.l)
		self.transistor = 0
		self.score -= 1	

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
		
		if self.query == True:
			score_str = " Left Player = %i " % (self.score)
			self.draw_area.draw_str(1, self.draw_area.height -1, score_str)
		if self.query == False:
			score_str = " Right Player = %i " % (self.score)
			self.draw_area.draw_str(self.draw_area.width -len(score_str) -1, self.draw_area.height -1, score_str)


	def player_functions(self):
		self.trigger = 1
		if self.transistor == 2:
			self.snake.move()
			self.collision_detection()
			self.snake.draw()
			self.draw()
		if self.transistor != 2:
			self.counter = self.counter + 1
			if self.transistor == 0:
				self.trigger = 0
				self.transistor = 1
			if self.trigger == 1:
				if self.transistor == 1:
					self.snake.draw()
					self.draw()
					self.transistor = 0
			if self.counter == 10:
				self.counter = 0
				self.transistor = 2

import random
from DrawArea import DrawArea

class Egg:
	def __init__(self, draw_area, x, y):
		self.draw_area = draw_area

		self.position = (x, y)

		self.visible = True

	def draw(self):
		if self.visible == True:
			self.draw_area.set(self.position[0],self.position[1], 'O')

	def is_a_hit(self, x, y):
		if self.visible == True:
			p_x =  self.position[0]
			p_y =  self.position[1]
	 
			if x == p_x and y == p_y:
				return True
			else:
				return False		
	def position_x(self):
		point = self.position[0]
		return point

	def position_y(self):
		point = self.position[1]
		return point
	def hide(self):
		self.visible = False

	def teleport(self):
		width = self.draw_area.width
		height = self.draw_area.height
		x = random.randint(1,width - 2)
		y = random.randint(1,height - 2)
		self.position=(x,y)

import curses.wrapper
from DrawArea import DrawArea

class Snake:
	def __init__(self, draw_area, x = 0, y = 0, d = 1, l = 2,):
		self.draw_area = draw_area

		self.reset(x, y, d, l)
		self.point_x = x
		self.point_y = y
	def reset(self, x, y, d, l):

		self.point_x = x
		self.point_y = y
		if d not in [3, 1, 4, 2]:
			raise Exception("Invalid direction: %s" % (new_dir))

		self.current_direction = d
		self.checker = d
		self.growth = False

		self.points = []
		for i in range(l-1, -1, -1):
			if d == 3:
				self.points += [(x,y-i)]
			if d == 1:
				self.points += [(x,y+i)]
			if d == 4:
				self.points += [(x+i,y)]
			if d == 2:
				self.points += [(x-i,y)]

	def draw(self):
		n = len(self.points)
		for point in self.points[:n-1]:
			point_x = point[0]
			point_y = point[1]
			self.draw_area.set(point_x, point_y, '*')

		point = self.points[n-1]
		self.draw_area.set(point[0], point[1], '#')

	def has_hit(self, obj):

		my_head = self.points[-1]

		return obj.is_a_hit(my_head[0], my_head[1])

	def is_a_hit(self, x, y):
	
		r = False

		for p in self.points[:-1]:
			p_x = p[0]
			p_y = p[1]
			if x == p_x and y == p_y:
				r = True
				
		return r
	def position_x(self):
		pointx = self.points[-1]
		return pointx[0]
	def position_y(self):
		pointy = self.points[-1]
		return pointy[1]

	def change_direction(self, new_dir):
		if new_dir in [3, 1, 4, 2]:
			if self.checker == 3:
				if new_dir != 1:
					self.current_direction = new_dir
				else:
					new_dir = self.checker
			if self.checker == 1:
				if new_dir != 3:
					self.current_direction = new_dir
				else:
					new_dir = self.checker
			if self.checker == 2:
				if new_dir != 4:
					self.current_direction = new_dir
				else:
					new_dir = self.checker
			if self.checker == 4:
				if new_dir != 2:
					self.current_direction = new_dir
				else:
					new_dir = self.checker
		else:
			return
		self.checker = new_dir
	def direction(self):
		return self.current_direction

	def move(self):
		n = len(self.points)
		old_head = self.points[n-1]

		dir = self.current_direction

		if dir == 2:
			new_head = (old_head[0]+1, old_head[1])
		elif dir == 4:
			new_head = (old_head[0]-1, old_head[1])
		elif dir == 3:
			new_head = (old_head[0], old_head[1]+1)
		elif dir == 1:
			new_head = (old_head[0], old_head[1]-1)

		# new_head = (x, y)
		if new_head[1] >= self.draw_area.height:
			new_head = (new_head[0], 0)
		if new_head[1] <= -1:
			new_head =(new_head[0],
				 self.draw_area.height - 1)
		if new_head[0] >= self.draw_area.width:
			new_head = (0, new_head [1])
		if new_head[0] <= -1:
			new_head = (self.draw_area.width -1, new_head[1])
			
		
		if self.growth == True:
			self.growth = False
		else:
			del self.points[0]

		self.points += [new_head]


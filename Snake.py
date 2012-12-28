
import curses
import curses.wrapper
from DrawArea import DrawArea

class Snake:
	def __init__(self, draw_area, x = 0, y = 0, start_size = 6):
		self.draw_area = draw_area

		self.reset(x, y, start_size, 'u')

	def reset(self, x, y, l, d):

		if d not in ['u', 'd', 'l', 'r']:
			raise Exception("Invalid direction: %s" % (new_dir))

		self.current_direction = d
		self.checker = d
		self.growth = False

		self.points = []
		for i in range(l-1, -1, -1):
			if d == 'u':
				self.points += [(x,y-i)]
			if d == 'd':
				self.points += [(x,y+i)]
			if d == 'l':
				self.points += [(x+i,y)]
			if d == 'r':
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

	def change_direction(self, new_dir):
		if new_dir in ['u', 'd', 'l', 'r']:
			if self.checker == 'u':
				if new_dir != 'd':
					self.current_direction = new_dir
				else:
					new_dir = self.checker
			if self.checker == 'd':
				if new_dir != 'u':
					self.current_direction = new_dir
				else:
					new_dir = self.checker
			if self.checker == 'r':
				if new_dir != 'l':
					self.current_direction = new_dir
				else:
					new_dir = self.checker
			if self.checker == 'l':
				if new_dir != 'r':
					self.current_direction = new_dir
				else:
					new_dir = self.checker
		else:
			raise Exception("Invalid direction: %s" % (new_dir))
		self.checker = new_dir

	def move(self):
		n = len(self.points)
		old_head = self.points[n-1]

		dir = self.current_direction

		if dir == 'r':
			new_head = (old_head[0]+1, old_head[1])
		elif dir == 'l':
			new_head = (old_head[0]-1, old_head[1])
		elif dir == 'u':
			new_head = (old_head[0], old_head[1]+1)
		elif dir == 'd':
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

def test_main(screen):
	
	draw_area = DrawArea(screen)

	snake = Snake(draw_area)

	dir = 'r'
	
	while True:
		draw_area.clear()
		snake.draw()
		draw_area.draw()
		
		key = screen.getch()
		
		if key == curses.KEY_UP: dir = 'u'
		elif key == curses.KEY_DOWN: dir = 'd'
		elif key == curses.KEY_LEFT: dir = 'l'
		elif key == curses.KEY_RIGHT: dir = 'r'
	
		snake.change_direction(dir)	
		snake.move()

if __name__ == "__main__":
	curses.wrapper(test_main)

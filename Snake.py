
import curses
import curses.wrapper
from DrawArea import DrawArea

class Snake:
	def __init__(self, draw_area, x = 5, y = 5):
		self.draw_area = draw_area

		self.current_direction = 'r'
		self.checker = None
		self.points = []
		for i in range(20):
			self.points += [(x+i,y)]

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

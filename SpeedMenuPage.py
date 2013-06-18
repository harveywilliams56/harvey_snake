from DrawArea import *
class SpeedMenuPage:
	def __init__(self, screen):
		self.screen = screen
		self.draw_area = DrawArea(screen)
		self.slow = []
	def draw_loop(self):
		while True:
			self.draw_area.clear()
			self.slow += "Slow"
			self.draw_area.draw_str(50,50,self.slow)
			self.draw_area.paint_to_screen()
			time.sleep(0.1)

from GamingPage import *
from SpeedMenuPage import *
import curses.wrapper
def test_main(screen):
	page = GamingPage(screen)
	#page = SpeedMenuPage(screen)
	#draw_loop returns next page
	#exits by no return value
	while page != None:
		page = page.draw_loop()

if __name__ == "__main__":
	curses.wrapper(test_main)

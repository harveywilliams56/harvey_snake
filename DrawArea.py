
#!/usr/bin/python

import curses
import curses.wrapper

class DrawArea:
   def __init__(self, full_screen):
      screen_height, screen_width = full_screen.getmaxyx()
      self.blank_char = '\0'

      self.width = 70
      self.height = 25

      extra_width = int((screen_width - self.width) * 0.5)
      extra_height = int((screen_height - self.height) * 0.5)

      self.screen = curses.newwin(self.height, self.width,
         extra_height, extra_width)

      curses.curs_set(0)
      self.clear()

   def set(self, x, y, c):

      flipped_y = self.height - y - 1

      self.grid[x][flipped_y] = c

   def clear(self):
      temp = [self.blank_char] * self.height
      self.grid = []
      for x in range(self.width):
         self.grid += [temp[:]]

   def draw_str(self, x, y, s):
      f = open("debug", "a")
      f.truncate()
      f.close()
      flipped_y = self.height - y - 1
      for c in s:
         self.grid[x][flipped_y] = c
         x += 1

   def paint_to_screen(self):

      self.screen.erase()
      self.screen.border()

      for x in range(self.width):
         for y in range(self.height):
            c = self.grid[x][y]
            if c != self.blank_char:
               if x == (self.width-1) and y == (self.height-1):
                  self.screen.addch(y, x - 1, ord(c))
                  ic = self.grid[x-1][y]
                  self.screen.insch(y, x - 1, ord(ic))
               else:
                  self.screen.addch(y, x, ord(c))

      #self.screen.move(self.height - 1, self.width - 1)
      self.screen.refresh()


def test_main(stdscreen):
   
   draw_area = DrawArea(stdscreen)

   # Test Snake
   draw_area.set(3, 8, '*')
   draw_area.set(3, 7, '*')
   draw_area.set(3, 6, '*')
   draw_area.set(3, 5, '*')
   draw_area.set(3, 4, '*')
   draw_area.set(4, 4, '*')
   draw_area.set(5, 4, '*')
   draw_area.set(6, 4, '*')
   draw_area.set(7, 4, '#')

   draw_area.draw()

   # Wait for a keypress before exiting
   stdscreen.getch()
   

if __name__ == "__main__":
   curses.wrapper(test_main)


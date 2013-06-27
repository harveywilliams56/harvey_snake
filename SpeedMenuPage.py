import time
import curses
from DrawArea import *
from GamingPage import *

class SpeedMenuPage:
   def __init__(self, screen):
      self.screen = screen
      self.draw_area = DrawArea(screen)

      self.menu_items = 3
      self.menu_ys = [40, 37, 34]
      self.menu_texts = ["Slow", "Medium", "Fast"]
      self.menu_sleeps = [0.200, 0.125, 0.080]

      self.current_item = 1

   def draw_loop(self):
      while True:

         keys = self.key_list()
         for key in keys:
            if key == curses.KEY_UP:
               self.move_pointer_up()
            if key == curses.KEY_DOWN:
               self.move_pointer_down()
            if key in [ord("\n"), ord(" ")]:
               snake_sleep = self.menu_sleeps[self.current_item]
               return GamingPage(self.screen, snake_sleep, self)
            if key == ord("q"):
               return None

         # redraw the screen
         self.draw_area.clear()

         self.draw_menu_text()
         self.draw_menu_pointer()

         self.draw_area.paint_to_screen()

         time.sleep(0.001)

   def move_pointer_down(self): 
      if self.current_item < self.menu_items - 1:
         self.current_item += 1

   def move_pointer_up(self): 
      if self.current_item > 0:
         self.current_item += -1

   def draw_menu_text(self):

      self.draw_area.draw_str(25, 45, "SELECT SNAKE SPEED")

      text_x = 22

      for i in range(self.menu_items):
         self.draw_area.draw_str(text_x,self.menu_ys[i], self.menu_texts[i])

   def draw_menu_pointer(self):

      pointer_x = 42
      pointer_text = "<--"

      pointer_y = self.menu_ys[self.current_item]

      self.draw_area.draw_str(pointer_x, pointer_y, pointer_text)

   #Get list of keys since last gameloop
   def key_list(self):
      key_list = []
      switch = True
      while switch:
         key = self.screen.getch()
         if key == curses.ERR:
            switch = False
         else:
            key_list += [key]
      return key_list


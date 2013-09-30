

import curses.wrapper
import time
from DrawArea import *
from Snake import *
import sys
from Egg import *
from Player import *

class Old_snake:
   def __init__(self, screen, snake_sleep, quit_page):
      self.screen = screen
      self.snake_sleep = snake_sleep
      self.quit_page = quit_page
      self.draw_area = DrawArea(screen)
      self.players = []
      self.map0 = {  ord('w') : 3,
            ord('a') : 4,
            ord('s') : 1,
            ord('d') : 2}
      self.player0 = Player(self.draw_area.width / 4,self.draw_area.height / 2, 3, 5, self.map0,self.draw_area,True)
      self.player0.add_to_obstacles(self.player0.snake)
      self.egg = Egg(self.draw_area, 9, 9)
      self.player0.add_to_food(self.egg)
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

   def draw_loop(self):

      while True:

         # Check for user input
         keys = self.key_list()
         for key in keys:
            if key == ord("r"):
               return self.quit_page
         dir = self.player0.key_decode(keys)
         self.player0.snake.change_direction(dir)

         # redraw the screen
         self.draw_area.clear()

         self.player0.player_functions()
         self.egg.draw()
         
         self.draw_area.paint_to_screen()
         
         # wait
         time.sleep(self.snake_sleep)


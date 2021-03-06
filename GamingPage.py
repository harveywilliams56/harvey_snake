import curses.wrapper
import time
from DrawArea import *
from Snake import *
import sys
from Egg import *
from Player import *

class GamingPage:
   def __init__(self, screen, snake_sleep, quit_page, game_type):
      self.screen = screen
      self.snake_sleep = snake_sleep
      self.quit_page = quit_page
      self.draw_area = DrawArea(screen)
      self.players = []

      self.map0 = {  curses.KEY_UP : 3,
            curses.KEY_LEFT : 4,
            curses.KEY_DOWN : 1,
            curses.KEY_RIGHT : 2}
      self.player0 = Player(self.draw_area.width / 4,self.draw_area.height / 2, 3, 5, self.map0,self.draw_area,True)
      self.player0.add_to_obstacles(self.player0.snake)
      self.egg = Egg(self.draw_area, 9, 9)
      self.player0.add_to_food(self.egg)


      if game_type != 1:
         self.map1 = {  ord('w') : 3,
               ord('a') : 4,
               ord('s') : 1,
               ord('d') : 2}
         self.player1 = Player(9, 9, 1, 5, self.map1, self.draw_area,False)
         self.player1.add_to_obstacles(self.player0.snake)
         self.player1.add_to_obstacles(self.player1.snake)
         self.player1.add_to_food(self.egg)
         self.player0.add_to_obstacles(self.player1.snake)
      self.game_type = game_type
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

   def AI(self):
      if self.game_type != 1:
         direction = self.player0.snake.direction()
         egg_point_x = self.egg.position_x()
         snake_point_x = self.player0.snake.position_x()
         egg_point_y = self.egg.position_y()
         snake_point_y = self.player0.snake.position_y()
         screen_width = self.draw_area.width
         wall_right = screen_width - snake_point_x + egg_point_x
         plain_left = snake_point_x - egg_point_x
         wall_left = snake_point_x + screen_width - egg_point_x
         plain_right = egg_point_x - snake_point_x
         screen_height = self.draw_area.height
         wall_up = screen_height - snake_point_y + egg_point_y
         plain_down = snake_point_y - egg_point_y
         wall_down = snake_point_y + screen_height - egg_point_y
         plain_up = egg_point_y - snake_point_y
         if direction == 1 or 3:
            if snake_point_x < egg_point_x:
               if plain_right < wall_left:
                  return 2
               else:
                  return 4
            if snake_point_x > egg_point_x:
               if plain_left < wall_right:
                  return 4
               else:
                  return 2
         if direction == 2 or 4:
            if snake_point_y < egg_point_y:
               if plain_up < wall_down:
                  return 3
               else:
                  return 1
            if snake_point_y > egg_point_y:
               if plain_down < wall_up:
                  return 1
               else:
                  return 3
         return direction
   def draw_loop(self):

      while True:

         # Check for user input
         keys = self.key_list()
         for key in keys:
            if key == ord("r"):
               return self.quit_page
         if self.game_type != "Comp":
            dir = self.player0.key_decode(keys)
         elif self.game_type == "Comp":
            dir = self.AI()
         self.player0.snake.change_direction(dir)
         
         self.draw_area.clear()

         if self.game_type != 1:
            dir = self.player1.key_decode(keys)
            self.player1.snake.change_direction(dir)
            self.player1.player_functions()

         self.player0.player_functions()
         self.egg.draw()
         
         self.draw_area.paint_to_screen()
         
         # wait
         time.sleep(self.snake_sleep)


from PPlay.window import *
from menus import MainMenu, DifficultyMenu
from player import Player
from aliens import AlienFleet

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720
  TITLE = 'Space Invaders v1.0.0-alpha'

  def __init__(self):
    self.window = Window(Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
    self.window.set_title(Game.TITLE)

    self.keyboard = self.window.get_keyboard()
    self.mouse = self.window.get_mouse()

    self.menuPool = []

    self.mainMenu = MainMenu(self)
    self.difficultyMenu = DifficultyMenu(self)

    self.menuPool.append(self.mainMenu)
    self.menuPool.append(self.difficultyMenu)

    self.difficulty = 1
    self.inGame = False

  def start(self):
    self.player = Player(self)
    self.aliens = AlienFleet(self, 0, 0, 3, 5)
    self.inGame = True

  def tick(self):
    self.window.set_background_color((0, 0, 0))

    for menu in self.menuPool:
      menu.tick(self.mouse, self.window.delta_time())

    if (self.inGame):
      self.player.tick()
      self.aliens.tick()

      if (self.keyboard.key_pressed('ESC')):
        self.inGame = False
        self.mainMenu.show()

    self.window.update()
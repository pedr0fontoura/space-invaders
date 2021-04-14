from PPlay.window import *
from PPlay.sprite import *
from menus import MainMenu, DifficultyMenu
from player import Player
from aliens import AlienFleet

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720
  TITLE = 'Space Invaders v1.0.0-alpha'

  MAX_LIFE = 3
  LIFE_SPRITE_PATH = 'assets/life.png'
  LIFE_SPRITE_FRAMES = 4

  PRIMARY_COLOR = (154, 217, 65)

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

    self.lifeBar = Sprite(Game.LIFE_SPRITE_PATH, Game.LIFE_SPRITE_FRAMES)
    self.lifeBar.set_sequence(0, 3, False)
    self.lifeBar.set_total_duration(1)

    self.lifeBar.x = Game.WINDOW_WIDTH - self.lifeBar.width - 5
    self.lifeBar.y = 0

    self.life = Game.MAX_LIFE

    self.difficulty = 1
    self.score = 0

    self.inGame = False
    
  def setLife(self, life):
    if (life > 3):
      return

    if (life < 0):
      self.stop()

    self.life = life
    self.lifeBar.update()
    self.lifeBar.set_curr_frame(Game.MAX_LIFE - life)

  def start(self):
    self.life = Game.MAX_LIFE
    self.score = 0
    self.player = Player(self)
    self.aliens = AlienFleet(self, 0, 64, 3, 5)
    self.inGame = True
  
  def stop(self):
    self.inGame = False
    self.mainMenu.show()
  
  def reset(self):
    self.player = Player(self)
    self.aliens = AlienFleet(self, 0, 64, 3, 5)

  def tick(self):
    self.window.set_background_color((0, 0, 0))

    for menu in self.menuPool:
      menu.tick(self.mouse, self.window.delta_time())

    if (self.inGame):
      self.player.tick()
      self.aliens.tick()

      self.lifeBar.draw()
      self.window.draw_text(str(self.score), 5, 5, 20, Game.PRIMARY_COLOR, "Arial", True)
      
      if (self.keyboard.key_pressed('ESC')):
        self.stop()

    self.window.update()
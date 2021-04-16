from PPlay.window import *
from PPlay.sprite import *
from menu import MainMenu, DifficultyMenu
from player import Player
from aliens import AlienFleet

class Game:

  WINDOW_WIDTH = 1280
  WINDOW_HEIGHT = 720
  TITLE = 'Space Invaders v1.0.0-alpha'
  DEBUG = False

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

    if (Game.DEBUG):
      self._frameRate = 0
      self.frameRate = 0
      self.timer = 0

    self.mainMenu = MainMenu(self)
    self.difficultyMenu = DifficultyMenu(self)

    self.menuPool.append(self.mainMenu)
    self.menuPool.append(self.difficultyMenu)

    self.life = Game.MAX_LIFE

    self.difficulty = 1
    self.score = 0

    self.inGame = False

  def createLifeBar(self):
    lifeBar = Sprite(Game.LIFE_SPRITE_PATH, Game.LIFE_SPRITE_FRAMES)
    lifeBar.set_sequence(0, 3, False)
    lifeBar.set_total_duration(1)

    lifeBar.x = Game.WINDOW_WIDTH - lifeBar.width - 5
    lifeBar.y = 0

    return lifeBar
    
  def setLife(self, life):
    if (life > 3):
      return

    if (life < 0):
      self.stop()

    self.life = life
    self.lifeBar.update()
    self.lifeBar.set_curr_frame(Game.MAX_LIFE - life)

  def start(self):
    self.lifeBar = self.createLifeBar()
    self.life = Game.MAX_LIFE
    self.score = 0
    self.player = Player(self)
    self.aliens = AlienFleet(self, 0, 64, 3, 5)
    self.inGame = True
  
  def stop(self):
    self.inGame = False
    self.mainMenu.show()
  
  def reset(self):
    self.player.sprite.x = self.window.width / 2 - self.player.sprite.width / 2

  def tick(self):
    if (Game.DEBUG):
      self._frameRate += 1
      self.timer += self.window.delta_time()

      if (self.timer >= 1):
        self.frameRate = self._frameRate
        self._frameRate = 0
        self.timer = 0

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

    if (Game.DEBUG):
      self.window.draw_text(str(self.frameRate), self.WINDOW_WIDTH - 50, self.WINDOW_HEIGHT - 32, 20, Game.PRIMARY_COLOR, "Arial", True)

    self.window.update()
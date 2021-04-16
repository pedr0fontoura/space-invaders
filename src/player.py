from PPlay.sprite import *

class Player:

  SPRITE_PATH = 'assets/ship.png'

  SHOT_COOLDOWN = 0.5
  SHOT_SPEED = 400

  def __init__(self, game):
    self.game = game

    self.sprite = Sprite(Player.SPRITE_PATH)
    self.sprite.x = self.game.window.width / 2 - self.sprite.width / 2
    self.sprite.y = self.game.window.height - 10 - self.sprite.height

    self.speed = 300 * (1.0 - self.game.difficulty / 10)

    self.shots = []
    self.lastShot = 0
    self.canShot = True

  def shot(self):
    sprite = Sprite('assets/shot.png')
    sprite.x = self.sprite.x + self.sprite.width / 2
    sprite.y = self.sprite.y - sprite.height

    self.shots.append(sprite)

  def tick(self):
    self.lastShot += self.game.window.delta_time()

    if (self.lastShot >= Player.SHOT_COOLDOWN):
      self.canShot = True

    if (self.game.keyboard.key_pressed('A') and self.sprite.x >= 0):
      self.sprite.x -= self.speed * self.game.window.delta_time()

    if (self.game.keyboard.key_pressed('D') and self.sprite.x + self.sprite.width <= self.game.window.width):
      self.sprite.x += self.speed * self.game.window.delta_time()

    if (self.canShot and self.game.keyboard.key_pressed('SPACE')):
      self.canShot = False
      self.lastShot = 0

      self.shot()

    for index, shot in enumerate(self.shots):
      shot.y -= Player.SHOT_SPEED * self.game.window.delta_time()
      shot.draw()
      
      if (shot.y <= 0):
        self.shots.pop(index)

    self.sprite.draw()
      



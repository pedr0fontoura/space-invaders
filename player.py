from PPlay.sprite import *
from state import GameState

class Player:

  SHOT_COOLDOWN = 0.5
  SHOT_SPEED = 200

  def __init__(self, x, y):
    self.sprite = Sprite('assets/ship.png')
    self.sprite.x = x - self.sprite.width / 2
    self.sprite.y = y - self.sprite.height

    self.speed = 300 * GameState.difficulty

    self.shots = []
    self.lastShot = 0
    self.canShot = True

  def shot(self):
    sprite = Sprite('assets/shot.png')
    sprite.x = self.sprite.x + self.sprite.width / 2
    sprite.y = self.sprite.y - sprite.height

    self.shots.append(sprite)

  def handle(self, window, keyboard, deltaTime):
    self.lastShot += deltaTime

    if (self.lastShot >= Player.SHOT_COOLDOWN):
      self.canShot = True

    if (keyboard.key_pressed('A') and self.sprite.x >= 0):
      self.sprite.x -= self.speed * deltaTime

    if (keyboard.key_pressed('D') and self.sprite.x + self.sprite.width <= window.width):
      self.sprite.x += self.speed * deltaTime

    if (self.canShot and keyboard.key_pressed('SPACE')):
      self.canShot = False
      self.lastShot = 0

      self.shot()

    for index, shot in enumerate(self.shots):
      shot.y -= Player.SHOT_SPEED * deltaTime
      shot.draw()
      
      if (shot.y <= 0):
        self.shots.pop(index)

  def draw(self):
    self.sprite.draw()
      



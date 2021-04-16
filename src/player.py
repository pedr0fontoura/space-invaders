from PPlay.sprite import *

class Player:

  SPRITE_PATH = 'assets/ship.png'

  SHOT_COOLDOWN = 0.5
  SHOT_SPEED = 400

  def __init__(self, game):
    self.game = game

    self.sprite = Sprite(Player.SPRITE_PATH, 2)
    self.sprite.set_total_duration(1000)
    self.sprite.pause()
    self.sprite.x = self.game.window.width / 2 - self.sprite.width / 2
    self.sprite.y = self.game.window.height - 10 - self.sprite.height

    self.speed = 300 * (1.0 - self.game.difficulty / 10)

    self.shots = []
    self.lastShot = 0
    self.canShot = True

    self.invincibleTimer = 0
    self.invincible = False

  def shot(self):
    sprite = Sprite('assets/shot.png')
    sprite.x = self.sprite.x + self.sprite.width / 2
    sprite.y = self.sprite.y - sprite.height

    self.shots.append(sprite)
  
  def hitDetection(self):
    if (self.invincible):
      return

    for index, shot in enumerate(self.game.aliens.shots):
      if (shot.y + shot.height < self.sprite.y):
        continue

      if ((shot.x + shot.width < self.sprite.x) or (shot.x > self.sprite.x + self.sprite.width)):
        continue
      
      if (self.sprite.collided(shot)):
        self.game.aliens.shots.pop(index)
        self.invincible = True
        self.game.setLife(self.game.life - 1)
        self.game.reset()
        self.sprite.play()


  def tick(self):
    deltaTime = self.game.window.delta_time()

    self.lastShot += deltaTime

    if (self.invincible):
      self.invincibleTimer += deltaTime

      if (self.invincibleTimer >= 2):
        self.invincible = False
        self.invincibleTimer = 0
        self.sprite.pause()

    if (self.lastShot >= Player.SHOT_COOLDOWN):
      self.canShot = True

    if (self.game.keyboard.key_pressed('A') and self.sprite.x >= 0):
      self.sprite.x -= self.speed * deltaTime

    if (self.game.keyboard.key_pressed('D') and self.sprite.x + self.sprite.width <= self.game.window.width):
      self.sprite.x += self.speed * deltaTime

    if (self.canShot and self.game.keyboard.key_pressed('SPACE')):
      self.canShot = False
      self.lastShot = 0
      self.shot()

    self.hitDetection()

    for index, shot in enumerate(self.shots):
      shot.y -= Player.SHOT_SPEED * deltaTime
      shot.draw()
      
      if (shot.y <= 0):
        self.shots.pop(index)

    self.sprite.draw()
    self.sprite.update()
      



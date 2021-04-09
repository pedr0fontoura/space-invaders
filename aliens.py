from PPlay.sprite import *

class AlienFleet:

  ALIEN_SPRITE_PATH = 'assets/alien.png'

  FLEET_HORIZONTAL_SPEED = 200
  FLEET_VERTICAL_SPEED = 200

  FLEET_DESCENT = 25

  def __init__(self, game, x, y, lines, columns):
    self.game = game

    self.lines = lines
    self.columns = columns

    self.aliens = []

    self.alienWidth = 0
    self.alienHeight = 0

    self.width = 0
    self.height = 0

    self.x = 0
    self.y = 0

    self.dx = 200
    self.dy = 0

    self._dx = self.dx
    self.shouldDescend = False
    self.descentDistance = 0

    for i in range(lines):
      tmpAliens = []

      for j in range(columns):
        sprite = Sprite(AlienFleet.ALIEN_SPRITE_PATH)
        
        if (not self.alienWidth):
          self.alienWidth = sprite.width

        if (not self.alienHeight):
          self.alienHeight = sprite.height

        sprite.x = self.x + self.width
        sprite.y = self.y + self.height

        self.width += self.alienWidth
        
        if (not j == columns - 1):
          self.width += int(self.alienWidth / 3)

        tmpAliens.append(sprite)
      
      if (not i == lines - 1):
        self.height += self.alienHeight + int(self.alienHeight / 3)
        self.width = 0

      self.aliens.append(tmpAliens)

  def descend(self):
    self.shouldDescend = True
    self._dx = self.dx
    self.dx = 0
    self.dy = AlienFleet.FLEET_VERTICAL_SPEED

    
  def tick(self):
    deltaTime = self.game.window.delta_time()

    self.x += self.dx * deltaTime
    self.y += self.dy * deltaTime

    if (self.shouldDescend):
      self.descentDistance += self.dy * deltaTime

      if (self.descentDistance >= AlienFleet.FLEET_DESCENT * self.game.difficulty):
        self.shouldDescend = False
        self.descentDistance = 0
        self.dx = self._dx
        self.dy = 0

    relativeX = self.x
    relativeY = self.y

    for i in range(self.lines):
      
      for j in range(self.columns):
        self.aliens[i][j].x = relativeX
        self.aliens[i][j].y = relativeY

        relativeX += self.alienWidth
        
        if (not j == self.columns - 1):
          relativeX += int(self.alienWidth / 3)

        self.aliens[i][j].draw()

      if (not i == self.lines - 1):
        relativeY += self.alienHeight + int(self.alienHeight / 3)
        relativeX = self.x

    # Left boundary
    if (self.x + self.width >= self.game.window.width):
      self.dx = -self.dx
      self.x = self.game.window.width - self.width - 1
      self.descend()

    # Right boundary
    if (self.x <= 0):
      self.dx = -self.dx
      self.x = 0 + 1
      self.descend()


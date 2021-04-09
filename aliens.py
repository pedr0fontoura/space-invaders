from PPlay.sprite import *

class AlienFleet:

  ALIEN_SPRITE_PATH = 'assets/alien.png'

  FLEET_HORIZONTAL_SPEED = 200
  FLEET_VERTICAL_SPEED = 200

  FLEET_DESCENT = 25

  def __init__(self, game, x, y, rows, columns):
    self.game = game

    self.aliens = []

    self.alienWidth = 0
    self.alienHeight = 0

    self.width = 0
    self.height = 0

    self.x = 0
    self._x = self.x

    self.y = 0
    self._y = self.y

    self.dx = 200
    self._dx = self.dx

    self.dy = 0

    self.shouldDescend = False
    self.descentDistance = 0

    for i in range(rows):
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
      
      if (not i == rows - 1):
        self.height += self.alienHeight + int(self.alienHeight / 3)
        self.width = 0

      self.aliens.append(tmpAliens)

  def descend(self):
    self.shouldDescend = True
    self._dx = self.dx
    self.dx = 0
    self.dy = AlienFleet.FLEET_VERTICAL_SPEED

  def collision(self):
    _rows = []
    _aliens = []
    _shots = []

    for k in range(len(self.game.player.shots)):
      for i in range(len(self.aliens)):
        for j in range(len(self.aliens[i])):
          alien = self.aliens[i][j]

          shot = self.game.player.shots[k]

          if (alien.collided(shot)):
            _aliens.append([i, j])
            _shots.append(k)

            if (len(self.aliens[i]) == 1):
              _rows.append(i)

    for _alien in _aliens:
      self.aliens[_alien[0]].pop(_alien[1])

    for _shot in _shots:
      self.game.player.shots.pop(_shot)

    for _row in _rows:
      self.aliens.pop(_row)

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
    
  def tick(self):
    deltaTime = self.game.window.delta_time()

    self._x = self.x
    self._y = self.y

    self.x += self.dx * deltaTime
    self.y += self.dy * deltaTime

    if (self.shouldDescend):
      self.descentDistance += self.dy * deltaTime

      if (self.descentDistance >= AlienFleet.FLEET_DESCENT * self.game.difficulty):
        self.shouldDescend = False
        self.descentDistance = 0
        self.dx = self._dx
        self.dy = 0

    relativeX = self.x - self._x
    relativeY = self.y - self._y

    for i in range(len(self.aliens)):
      for j in range(len(self.aliens[i])):
        self.aliens[i][j].x = self.aliens[i][j].x + relativeX
        self.aliens[i][j].y = self.aliens[i][j].y + relativeY
        self.aliens[i][j].draw()

    self.collision()


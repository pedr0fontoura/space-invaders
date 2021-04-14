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

    self.x = x
    self.y = y

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
      else:
        self.height += self.alienHeight

      self.aliens.append(tmpAliens)

  def descend(self):
    self.shouldDescend = True
    self._dx = self.dx
    self.dx = 0
    self.dy = AlienFleet.FLEET_VERTICAL_SPEED

  def resize(self):
    if (not len(self.aliens)):
      return

    startX = self.aliens[0][0].x
    startY = self.aliens[0][0].y
    endX = self.aliens[0][0].x + self.aliens[0][0].width
    endY = self.aliens[0][0].y + self.aliens[0][0].height

    for i in range(len(self.aliens)):
        for j in range(len(self.aliens[i])):
          if (self.aliens[i][j].x < startX):
            startX = self.aliens[i][j].x

          if (self.aliens[i][j].y < startY):
            startY = self.aliens[i][j].y

          if (self.aliens[i][j].x + self.aliens[i][j].width > endX):
            endX = self.aliens[i][j].x + self.aliens[i][j].width

          if (self.aliens[i][j].y + self.aliens[i][j].height > endY):
            endY = self.aliens[i][j].y + self.aliens[i][j].height
    
    self.x = startX
    self.y = startY
    self.width = endX - startX
    self.height = endY - startY

  def hitDetection(self):
    _aliens = []
    _shots = []
    _rows = []

    resize = False

    # Detection
    for k in range(len(self.game.player.shots)):
      shot = self.game.player.shots[k]

      if (not ((shot.x >= self.x and shot.x <= self.x + self.width) and (shot.y <= self.y + self.height and shot.y >= self.y))):
        break

      for i in range(len(self.aliens) - 1, -1 , -1):
        shouldBreak = False

        for j in range(len(self.aliens[i])):
          alien = self.aliens[i][j]

          if (alien.collided(shot)):
            _aliens.append([i, j])
            _shots.append(k)
            resize = True

            if (len(self.aliens[i]) == 1):
              _rows.append(i)

            self.game.score += len(self.aliens) - i

            shouldBreak = True
            break

        if (shouldBreak):
          break

    for _alien in _aliens:
      self.aliens[_alien[0]].pop(_alien[1])

    for _shot in _shots:
      self.game.player.shots.pop(_shot)

    for _row in _rows:
      self.aliens.pop(_row)

    if (resize):
      self.resize()

  def tick(self):
    if (not len(self.aliens)):
      self.game.mainMenu.show()
      self.game.stop()
      return

    deltaTime = self.game.window.delta_time()

    self.x += self.dx * deltaTime
    self.y += self.dy * deltaTime

    for i in range(len(self.aliens)):
      for j in range(len(self.aliens[i])):
        self.aliens[i][j].x = self.aliens[i][j].x + self.dx * deltaTime
        self.aliens[i][j].y = self.aliens[i][j].y + self.dy * deltaTime
        self.aliens[i][j].draw()

    self.hitDetection()
    
    if (self.shouldDescend):
      self.descentDistance += self.dy * deltaTime

      if (self.descentDistance >= AlienFleet.FLEET_DESCENT * self.game.difficulty):
        self.shouldDescend = False
        self.descentDistance = 0
        self.dx = self._dx
        self.dy = 0

    elif (self.x <= 0):
      self.dx = -self.dx
      self.x = 0 + 1
      self.descend()

    elif (self.x + self.width >= self.game.window.width):
      self.dx = -self.dx
      self.x = self.game.window.width - self.width - 1
      self.descend()

    if (self.y + self.height >= self.game.player.sprite.y):
      self.game.setLife(self.game.life - 1)
      self.game.reset()

    # Debug fleet x, y, width, height
    if (self.game.DEBUG):
      self.game.window.draw_text('|', self.x, self.y, 20, (255, 0, 0))
      self.game.window.draw_text('```', self.x, self.y, 20, (255, 0, 0))
      self.game.window.draw_text('|', self.x, self.y + self.height -20, 20, (255, 0, 0))
      self.game.window.draw_text(',,,', self.x, self.y + self.height -20, 20, (255, 0, 0))
      self.game.window.draw_text('|', self.x + self.width, self.y, 20, (255, 0, 0))
      self.game.window.draw_text('```', self.x + self.width  - 20, self.y, 20, (255, 0, 0))
      self.game.window.draw_text('|', self.x + self.width, self.y + self.height -20, 20, (255, 0, 0))
      self.game.window.draw_text(',,,', self.x + self.width - 20, self.y + self.height -20, 20, (255, 0, 0))
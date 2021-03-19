from PPlay.sprite import *

MENU_INTERACTION_COOLDOWN = 0.1
MENU_ITEM_PRESSED_COOLDOWN = 0.1

class MenuItem:
  def __init__(self, sprite, action = None):
    self.sprite = Sprite(sprite, 2)
    self.sprite.set_sequence_time(0, 1, 1000, False)

    self.action = action

    self.lastPressed = 0
    self.canBePressed = True

  def handle(self, mouse, deltaTime):
    isMouseOverArea = mouse.is_over_area((self.sprite.x, self.sprite.y), (self.sprite.x + self.sprite.width, self.sprite.y + self.sprite.height))
    isMenuItemPressed = mouse.is_button_pressed(1)
    
    self.lastPressed += deltaTime

    if (self.lastPressed >= MENU_ITEM_PRESSED_COOLDOWN):
      self.canBePressed = True

    if (isMouseOverArea):
      self.sprite.set_curr_frame(1)

      if (isMenuItemPressed and self.canBePressed):
          self.canBePressed = False
          self.lastPressed = 0

          if (self.action):
            self.action()
    else:
      self.sprite.set_curr_frame(0)

  def draw(self):
    self.sprite.draw()
    self.sprite.update()


class Menu:
  def __init__(self, x, y, active = True):
    self.active = active

    self.items = []
    
    self._x = x
    self._y = y

    self.x = x
    self.y = y
    
    self.width = 0
    self.height = 0

    self.timer = 0
    self.safeForInteraction = False

  def centerItems(self):
      menu = self
      for item in menu.items:
        item.sprite.x = menu.x + menu.width / 2 - item.sprite.width / 2

  def center(self):
    self.x = self._x - self.width / 2
    self.centerItems()

  def addItem(self, item):
    if (item.sprite.width > self.width):
      self.width = item.sprite.width

    self.height += item.sprite.height

    item.sprite.y = self.y + self.height + 10

    self.items.append(item)
    self.center()

  def handle(self, mouse, deltaTime):
    if not self.active: return
    
    if not self.safeForInteraction:
      self.timer += deltaTime

      if self.timer >= MENU_INTERACTION_COOLDOWN:
        self.safeForInteraction = True

    for item in self.items:
      if self.safeForInteraction:
        item.handle(mouse, deltaTime)
      item.draw()

  def show(self):
    self.active = True

  def hide(self):
    self.active = False
    self.safeForInteraction = False
    self.timer = 0

  

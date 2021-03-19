from PPlay.window import *
from menu import *
from state import GameState
from player import Player

window = Window(1280, 720)
window.set_title('Space Invaders')
window.set_background_color((0, 0, 0))

keyboard = window.get_keyboard()
mouse = window.get_mouse()

menuX = window.width / 2
menuY = window.height / 2

mainMenu, difficultyMenu = createGameMenu(menuX, menuY)

player = Player(window.width / 2, window.height - 10)

while (True):
  window.set_background_color((0, 0, 0))

  mainMenu.handle(mouse, window.delta_time())
  difficultyMenu.handle(mouse, window.delta_time())

  if (GameState.inGame):
    player.handle(window, keyboard, window.delta_time())
    player.draw()

    if (keyboard.key_pressed('ESC')):
      GameState.inGame = False
      mainMenu.show()

    
    
  window.update()
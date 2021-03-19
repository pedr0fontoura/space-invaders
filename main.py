from PPlay.window import *
from menu import *

window = Window(1280, 720)
window.set_title('Space Invaders')
window.set_background_color((0, 0, 0))

keyboard = window.get_keyboard()
mouse = window.get_mouse()

menuX = window.width / 2
menuY = window.height / 2

inGame = False

mainMenu = Menu(menuX,menuY)
difficultyMenu = Menu(menuX, menuY, False)

def playAction():
  mainMenu.hide()

  global inGame

  inGame = True

playButton = MenuItem('assets/menu/play.png', playAction)

def difficultyAction():
  mainMenu.hide()
  difficultyMenu.show()

difficultyButton = MenuItem('assets/menu/difficulty.png', difficultyAction)

rankingButton = MenuItem('assets/menu/ranking.png')

def exitAction():
  exit(0)

exitButton = MenuItem('assets/menu/Exit.png', exitAction)

mainMenu.addItem(playButton)
mainMenu.addItem(difficultyButton)
mainMenu.addItem(rankingButton)
mainMenu.addItem(exitButton)

easyButton = MenuItem('assets/menu/easy.png')
mediumButton = MenuItem('assets/menu/medium.png')
hardButton = MenuItem('assets/menu/hard.png')

def backAction():
  difficultyMenu.hide()
  mainMenu.show()

backButton = MenuItem('assets/menu/back.png', backAction)

difficultyMenu.addItem(easyButton)
difficultyMenu.addItem(mediumButton)
difficultyMenu.addItem(hardButton)
difficultyMenu.addItem(backButton)

while (True):
  window.set_background_color((0, 0, 0))

  mainMenu.handle(mouse, window.delta_time())
  difficultyMenu.handle(mouse, window.delta_time())

  if (inGame and keyboard.key_pressed('ESC')):
    inGame = False
    mainMenu.show()
    
  window.update()
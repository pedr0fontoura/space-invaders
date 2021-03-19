from lib.menu import MenuItem, Menu
from state import GameState

def createGameMenu(x, y):
  mainMenu = Menu(x, y)
  difficultyMenu = Menu(x, y, False)

  def playAction():
    mainMenu.hide()

    GameState.inGame = True

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

  return mainMenu, difficultyMenu
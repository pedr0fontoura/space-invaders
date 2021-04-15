from lib.menu import MenuItem, Menu

class MainMenu(Menu):

  def __init__(self, game):
    self.game = game
    
    super().__init__(self.game.window.width / 2, self.game.window.height / 2)

    def playAction():
      self.hide()
      self.game.start()

    playButton = MenuItem('assets/menu/play.png', playAction)

    def difficultyAction():
      self.hide()
      self.game.difficultyMenu.show()

    difficultyButton = MenuItem('assets/menu/difficulty.png', difficultyAction)

    rankingButton = MenuItem('assets/menu/ranking.png')

    def exitAction():
      exit(0)

    exitButton = MenuItem('assets/menu/Exit.png', exitAction)

    self.addItem(playButton)
    self.addItem(difficultyButton)
    self.addItem(rankingButton)
    self.addItem(exitButton)
    
class DifficultyMenu(Menu):
  def __init__(self, game):
    self.game = game
    
    super().__init__(self.game.window.width / 2, self.game.window.height / 2, False)

    def easyAction():
      self.game.difficulty = 0

    easyButton = MenuItem('assets/menu/easy.png', easyAction)

    def mediumAction():
      self.game.difficulty = 1

    mediumButton = MenuItem('assets/menu/medium.png', mediumAction)

    def hardAction():
      self.game.difficulty = 2

    hardButton = MenuItem('assets/menu/hard.png', hardAction)

    def backAction():
      self.hide()
      self.game.mainMenu.show()

    backButton = MenuItem('assets/menu/back.png', backAction)

    self.addItem(easyButton)
    self.addItem(mediumButton)
    self.addItem(hardButton)
    self.addItem(backButton)

import os
import sys

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

pplay_dir = os.path.join(vendor_dir, 'pplay')

sys.path.append(vendor_dir)

# Handle PPlay repo structure
sys.path.append(pplay_dir)

from game import Game

game = Game()

while (True):
  game.tick()
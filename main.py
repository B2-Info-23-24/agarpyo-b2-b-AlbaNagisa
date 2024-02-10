import sys
import pygame
import os
from game import Game
from states.splash import Splash
from states.menu import Menu
from states.game_over import GameOver
from states.gameplay import Gameplay

os.environ['TextColor'] = "Black"
os.environ['BackgroundColor'] = "White"
os.environ['FontSize'] = "32"
os.environ['CircleColor'] = "Red"
os.environ["EnnemieColor"] = "Blue"

pygame.init()
pygame.display.set_caption("AgarPyo")
screen = pygame.display.set_mode((1280, 720))
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GameOver(),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()
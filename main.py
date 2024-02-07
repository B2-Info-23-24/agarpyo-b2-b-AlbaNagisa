

import sys
import pygame
from game import Game

from states.splash import Splash
from states.menu import Menu
from states.game_over import GamOver
from states.gameplay import Gameplay


pygame.init()
pygame.display.set_caption("AgarPyo")
screen = pygame.display.set_mode((1080, 720))
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GamOver(),
    
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()
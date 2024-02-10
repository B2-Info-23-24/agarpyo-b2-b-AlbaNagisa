import pygame
from states.gameplay import Gameplay


class GameplayWithMouse(Gameplay):        
    def moving(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos
        pass
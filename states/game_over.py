import pygame

from states.base import Base
import os
import pygame
from states.base import Base
import pygame
import os


class GameOver(Base):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title = self.font.render("Game Over", True, pygame.Color(os.environ['TextColor']))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.instructions = self.font.render("Press Escape to return to the main menu", True, pygame.Color(os.environ['TextColor']))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 50)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)
        
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.next_state = "MENU"
                self.done = True
            
                
    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions, self.instructions_rect)
                
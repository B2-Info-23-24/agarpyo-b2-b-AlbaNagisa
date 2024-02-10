import pygame
from .base import Base


class Splash(Base):
    def __init__(self):
        super().__init__()
        self.title = self.font.render("AgarPyo", True, pygame.Color("red"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0
        
    def update(self, dt):
        self.time_active += dt
        if (self.time_active >= 2500):
            self.done = True 
            
    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.title, self.title_rect)
import pygame


class Base:
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.persist = {}
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(None, 24)
        
        
    def startup(self, persistent):
        self.persist = persistent
        
    def get_event(self, event):
        pass
    def update(self, dt):
        pass
    def draw(self, surface):
        surface.fill((255, 255, 255))
        pass
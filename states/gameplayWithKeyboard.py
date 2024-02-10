import pygame
from states.gameplay import Gameplay

class GameplayWithKeyboard(Gameplay):
    def moving(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed *dt) 
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed *dt)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed *dt, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed *dt, 0)
import math
import pygame

from states.gameplay import Gameplay


class GameplayWithMouse(Gameplay):
    
        
    def moving(self, dt):
        initial_position = pygame.math.Vector2(self.rect.center)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery

        magnitude = math.sqrt(dx**2 + dy**2)

        if magnitude != 0:
            normalized_dx = dx / magnitude
            normalized_dy = dy / magnitude
        else:
            normalized_dx = 0
            normalized_dy = 0
        self.rect.move_ip(normalized_dx * self.speed * dt, normalized_dy * self.speed * dt)

        frame_distance = (pygame.math.Vector2(self.rect.center) - initial_position).length()
        print(frame_distance)
import os
import pygame


class Button:
    def __init__(self, x, y, width, height, text, bg_color=(255,255,255)):
        self.text = text
        self.bg_color = bg_color
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)



    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        surface.blit(self.text, (self.rect.x + (self.width - self.text.get_width()) // 2, self.rect.y + (self.height - self.text.get_height()) // 2))

    def handle_event(self, event, action):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                action()
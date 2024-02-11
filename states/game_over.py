
from classes.button import Button
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
        self.instructions = self.font.render("Press Escape to return to the main menu", True, pygame.Color(os.environ['TextColor']))
        self.selected = 0
        self.text_score = self.font.render("Your score: ", True, pygame.Color(os.environ['TextColor'])) 
        self.buttons = []
        self.options = ["Play Again", "Main Menu"]
    
    def handle_action(self):
        if self.selected == 0:
            self.next_state = "GAMEPLAY"
            self.done = True
        elif self.selected == 1:
            self.next_state = "MENU"
            self.done = True
    
    def startup(self, persistent):
        self.define_buttons()
        self.text_score = self.font.render("Your score: "+str(persistent["score"]), True, pygame.Color(os.environ['TextColor']))
        return super().startup(persistent)
    
    def choose_color(self, index):
        return pygame.Color("White") if index != self.selected else pygame.Color("red") 

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)
          
    def define_buttons(self):
        self.buttons = []
        screen_width, screen_height = pygame.display.get_surface().get_size()
        padding = 10
        for index, option in enumerate(self.options):
            text_render = self.font.render(option, True, os.environ['TextColor'])
            button_width = text_render.get_width() + 2 * padding
            button_height = text_render.get_height() + 2 * padding
            x = screen_width // 2 - button_width // 2
            y = screen_height // 2 - button_height // 2 + index * 50            
            self.buttons.append(Button(x,y,button_width,button_height,text_render, self.choose_color(index)))
            
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.next_state = "MENU"
                self.done = True
                
        for index, button in enumerate(self.buttons):
            if button.is_hovered():
                self.selected = index
            button.handle_event(event, self.handle_action)
            
        self.define_buttons()
            
                
    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.title, self.get_text_position(self.title, -3))
        surface.blit(self.instructions, self.get_text_position(self.instructions, -2))
        surface.blit(self.text_score, self.get_text_position(self.text_score, -1))
        for button in self.buttons:
            button.draw(surface)
                
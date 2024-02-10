import os
import pygame
from classes.button import Button
from states.base import Base

class Menu(Base):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.instructions = "Use arrow keys to navigate and press enter to select an option"
        self.options   = ["Start with keyboard", "Start with mouse", "Quit"]
        self.next_state = "GAMEPLAY"
        self.buttons = []
        
    def choose_color(self, index):
      return pygame.Color("White") if index != self.active_index else pygame.Color("red") 
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)
        
    
    def handle_action(self):
        if self.active_index == 0:
            self.next_state = "GAMEPLAY"
            self.done = True
        elif self.active_index == 1:
            self.next_state = "GAMEPLAY_MOUSE"
            self.done = True
        elif self.active_index == 2:
            self.quit = True
            
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
                
    def startup(self, persistent):
        persistent["ennemy"] = 2
        persistent["food"] = 5
        self.define_buttons()
        super().startup(persistent)
    
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.active_index = 0 if self.active_index <= 0 else self.active_index-1
            elif event.key == pygame.K_DOWN:
                self.active_index = len(self.options)-1 if self.active_index >= len(self.options)-1 else self.active_index+1 
            elif event.key == pygame.K_RETURN:
                self.handle_action()

        for index, button in enumerate(self.buttons):
            if button.is_hovered():
                self.active_index = index
            button.handle_event(event, self.handle_action)
            
        self.define_buttons()
        
        
        
                
        
    def draw(self, surface):
        super().draw(surface)
        text_render_inst = self.font.render(self.instructions, True, pygame.Color("Black"))
        surface.blit(text_render_inst, self.get_text_position(text_render_inst, -1))
        for button in self.buttons:
            button.draw(surface)
        

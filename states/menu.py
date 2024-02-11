import os
import pygame
from classes.button import Button
from states.base import Base

class Menu(Base):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.instructions = "Use arrow keys to navigate and press enter to select an option"
        self.next_state = "GAMEPLAY"
        self.title = pygame.font.Font(None, 50).render("Agarpyo", True, pygame.Color(os.environ['TextColor']))
        self.buttons = []
        self.difficulty = {}
        self.difficulty_show = False
        self.difficulty_selected = 0
        self.difficulty_options = ["Easy", "Medium", "Hard", "Go Back"]
        self.n_food_per_difficulty = [5, 3, 2]
        self.n_ennemy_per_difficulty = [2, 3, 4]
        self.difficulty_number = [2, 3, 4]
        self.options   = ["Start with keyboard", "Start with mouse",f"Difficulty ({self.difficulty_options[self.difficulty_selected]})", "Quit"]
        
        
        
        
    def choose_color(self, index, difficulty=False):
        if difficulty:
            if index == self.difficulty_selected:
                return pygame.Color("Green")
            else:
                if index != self.active_index:
                    return pygame.Color("White")
                else:
                    return pygame.Color("red")
        
        return pygame.Color("White") if index != self.active_index else pygame.Color("red") 
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)
        
    
    def handle_action(self):
        if self.difficulty_show:
            self.difficulty_show = False
            if self.active_index == 3:
                return
            self.difficulty_selected = self.active_index
            self.options  = ["Start with keyboard (directional arrows)", "Start with mouse",f"Difficulty ({self.difficulty_options[self.difficulty_selected]})", "Quit"]
            self.persist["ennemy"] = self.n_ennemy_per_difficulty[self.difficulty_selected]
            self.persist["food"] = self.n_food_per_difficulty[self.difficulty_selected]
            self.persist["difficulty"] = self.difficulty_options[self.difficulty_selected]
            self.persist["difficulty_number"] = self.difficulty_number[self.difficulty_selected]
            
        else:
            if self.active_index == 0:
                self.next_state = "GAMEPLAY"
                self.done = True
            elif self.active_index == 1:
                self.next_state = "GAMEPLAY_MOUSE"
                self.done = True
            elif self.active_index == 2:
                self.difficulty_show = True
            elif self.active_index == 3:
                self.quit = True
            
    def define_buttons(self):
        self.buttons = []
        screen_width, screen_height = pygame.display.get_surface().get_size()
        padding = 10
        for index, option in enumerate(self.difficulty_options if self.difficulty_show else self.options):
            text_render = self.font.render(option, True, os.environ['TextColor'])
            button_width = text_render.get_width() + 2 * padding
            button_height = text_render.get_height() + 2 * padding
            x = screen_width // 2 - button_width // 2
            y = screen_height // 2 - button_height // 2 + index * 50            
            self.buttons.append(Button(x,y,button_width,button_height,text_render, self.choose_color(index, self.difficulty_show)))
                
    def startup(self, persistent):
        self.define_buttons()
        super().startup(persistent)
        self.persist["ennemy"] = self.n_ennemy_per_difficulty[self.difficulty_selected]
        self.persist["food"] = self.n_food_per_difficulty[self.difficulty_selected]
        self.persist["difficulty"] = self.difficulty_options[self.difficulty_selected]
        self.persist["difficulty_number"] = self.difficulty_number[self.difficulty_selected]
    
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
            elif event.key == pygame.K_ESCAPE:
                if self.difficulty_show:
                    self.difficulty_show = False
            elif event.key == pygame.K_p:
                self.next_state = "GAMEPLAY"
                self.done = True
            elif event.key == pygame.K_q:
                self.quit = True
                
        for index, button in enumerate(self.buttons):
            if button.is_hovered():
                self.active_index = index
            button.handle_event(event, self.handle_action)
            
        self.define_buttons()
        
        
        
                
        
    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.title, self.get_text_position(self.title, -3))
        text_render_inst = self.font.render(self.instructions, True, pygame.Color("Black"))
        surface.blit(text_render_inst, self.get_text_position(text_render_inst, -1))
        for button in self.buttons:
            button.draw(surface)
        

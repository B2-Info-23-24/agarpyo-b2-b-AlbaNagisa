import math
import pygame
from states.base import Base
import pygame
import os
import random

class Gameplay(Base):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.totalTime = 60
        self.timeLeft = self.totalTime
        self.elapsed_time = 0
        self.speed = 100
        self.timer = self.font.render(str(self.timeLeft)+"s", True, pygame.Color(os.environ['TextColor']))
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.next_state = "GAME_OVER"
        self.score = 0
        self.enemies = []
        self.foods = []
        
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.next_state = "MENU"
                self.done = True
                
    def reset(self):
        self.elapsed_time = 0
        self.timeLeft = self.totalTime
        self.rect.center = self.screen_rect.center
        self.score = 0
        self.enemies = []
        
    def startup(self, persistent):
        super().startup(persistent)
        self.reset()
        [self.spawn_ennemy() for _ in range(self.persist["ennemy"])]
        print(persistent)
        
    def spawn_ennemy(self):
        radius = random.randint(40, 150)
        x = random.randint(radius, self.screen_rect.width - radius)
        y = random.randint(radius, self.screen_rect.height - radius)
        self.enemies.append(pygame.Rect((x - radius, y - radius), (radius * 2, radius * 2)))
        
    def spawn_food(self):
        radius = 10
        x = random.randint(radius, self.screen_rect.width - radius)
        y = random.randint(radius, self.screen_rect.height - radius)
        self.foods.append(pygame.Rect((x - radius, y - radius), (radius * 2, radius * 2)))
        
    def check_collision(self):
        for enemy in self.enemies:
            distance = math.sqrt((self.rect.x - enemy.x)**2 + (self.rect.y - enemy.y)**2)
            if (distance <= self.rect.width // 2 + enemy.width // 2) and self.rect.width // 2 >= enemy.width // 2:
            
                print("Collision detected!")
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        dt = dt/1000
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed *dt) 
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed *dt)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed *dt, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed *dt, 0)
            
        self.check_collision()    
        
            
        self.elapsed_time += dt
        self.timeLeft = self.totalTime - int(self.elapsed_time)
        self.timer = self.font.render(str(self.timeLeft)+'s', True, pygame.Color(os.environ['TextColor']))
        if self.timeLeft <= 0:
            self.next_state = "GAME_OVER"
            self.done = True
        
    
    def draw(self, surface):
        super().draw(surface)
        pygame.draw.circle(surface, pygame.Color(os.environ["CircleColor"]), self.rect.center, self.rect.width // 2)
        for enemy in self.enemies:
            pygame.draw.circle(surface, pygame.Color(os.environ["EnnemieColor"]), enemy.center, enemy.width // 2)
        
        surface.blit(self.timer, (10, 10))
        

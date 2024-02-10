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
        self.timer = self.font.render("Time left: "+str(self.timeLeft)+'s', True, pygame.Color(os.environ['TextColor']))
        self.rect = pygame.Rect((0, 0), (40, 40))
        self.rect.center = self.screen_rect.center
        self.next_state = "GAME_OVER"
        self.score = 0
        self.enemies = []
        self.foods = []
        self.point = self.font.render("Score: "+str(self.score), True, pygame.Color(os.environ['TextColor']))
        self.difficulty_text = self.font.render("Difficulty: ", True, pygame.Color(os.environ['TextColor']))
        self.size_text = self.font.render("Size: ", True, pygame.Color(os.environ['TextColor']))
        self.speed_text = self.font.render("Speed: ", True, pygame.Color(os.environ['TextColor']))
        
        
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
        self.foods = []
        self.speed = 100
        self.rect.width = 40
        
        
    def startup(self, persistent):
        super().startup(persistent)
        self.reset()
        self.difficulty_text = self.font.render("Difficulty: "+ str(self.persist["difficulty"]), True, pygame.Color(os.environ['TextColor']))
        [self.spawn_ennemy() for _ in range(self.persist["ennemy"])]
        [self.spawn_food() for _ in range(self.persist["food"])]
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
            distance = math.sqrt((self.rect.centerx - enemy.centerx)**2 + (self.rect.centery - enemy.centery)**2)
            if distance <= self.rect.width // 2 + enemy.width // 2 and self.rect.width > enemy.width:
                self.enemies.remove(enemy)
                self.eat_ennemy()
                self.spawn_ennemy()

        for food in self.foods:
            distance = math.sqrt((self.rect.centerx - food.centerx)**2 + (self.rect.centery - food.centery)**2)
            if distance <= self.rect.width // 2 + food.width // 2:
                self.foods.remove(food)
                self.eat()
                self.spawn_food()
                
    def eat(self):
        self.score += 1
        self.speed += 5
        self.rect.width += 2
        if self.rect.width > 400:
            self.rect.width = 400
        if self.speed > 500:
            self.speed = 500
        
    def eat_ennemy(self):
        self.speed //= int(self.persist["difficulty_number"])
        self.rect.width //= int(self.persist["difficulty_number"])
        if self.rect.width < 40:
            self.width = 40
        if self.speed < 100:
            self.speed = 100
        
    def teleport(self):
        if self.rect.x+self.rect.width < 0:
            self.rect.x = self.screen_rect.width
        elif self.rect.x > self.screen_rect.width:
            self.rect.x = 0 - self.rect.width
        if self.rect.y +self.rect.height < 0:
            self.rect.y = self.screen_rect.height
        elif self.rect.y > self.screen_rect.height:
            self.rect.y = 0 - self.rect.height
    
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
     
    def update(self, dt):
        dt/=1000
        self.moving(dt)            
        self.check_collision()    
        self.teleport()
        self.elapsed_time += dt
        self.timeLeft = self.totalTime - int(self.elapsed_time)
        self.timer = self.font.render("Time left: "+str(self.timeLeft)+'s', True, pygame.Color(os.environ['TextColor']))
        self.point = self.font.render("Score: "+str(self.score), True, pygame.Color(os.environ['TextColor']))
        self.size_text = self.font.render("Size: "+str(self.rect.width), True, pygame.Color(os.environ['TextColor']))
        self.speed_text = self.font.render("Speed: "+str(self.speed), True, pygame.Color(os.environ['TextColor']))
        if self.timeLeft <= 0:
            self.next_state = "GAME_OVER"
            self.done = True
        
        
    def draw(self, surface):
        super().draw(surface)
        pygame.draw.circle(surface, pygame.Color(os.environ["CircleColor"]), self.rect.center, self.rect.width // 2)
        for food in self.foods:
            pygame.draw.circle(surface, pygame.Color(os.environ["FoodColor"]), food.center, food.width // 2)
        
        for enemy in self.enemies:
            pygame.draw.circle(surface, pygame.Color(os.environ["EnnemyColor"]), enemy.center, enemy.width // 2)
        
    
        surface.blit(self.timer, (10, 10))
        surface.blit(self.point, (1280-self.point.get_width()-10, 10))
        surface.blit(self.difficulty_text, (1280-self.difficulty_text.get_width()-10, 30))
        surface.blit(self.size_text, (1280-self.size_text.get_width()-10, 50))
        surface.blit(self.speed_text, (1280-self.speed_text.get_width()-10, 70))
                
        
        

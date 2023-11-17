import pygame
import time


# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# 점 정보 클래스
class Dot:
    def __init__(self, x, y, color, radius, alpha=255,):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.alpha = alpha  # 이펙트
        self.creation_time = time.time()  # 현재 시간으로 초기화

    def draw(self):
        # 투명도를 적용한 원 그리기
        dot_surface = pygame.Surface(
            (self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(dot_surface, (self.color[0], self.color[1], self.color[2], self.alpha),
                           (self.radius, self.radius), self.radius)
        screen.blit(dot_surface, (self.x - self.radius, self.y - self.radius))





#난이도 클래스
class Difficulty: # 클래스로 찍어내니까 random값이 한판 내에서 고정값이 되어버림
    def __init__(self, level):
        if level == 1: 
          self.radius = 20 
          self.speed = 5
          self.my_attack = 15 #10~20
          self.enemy_attack = 10 # 5~15
          self.dot_alpha = 200
          self.dot_time = 2

        elif level == 2:
          self.radius = 15
          self.speed = 4
          self.my_attack = 10 #5~15
          self.enemy_attack = 15 #10~20
          self.dot_alpha = 150
          self.dot_time = 1.5
          
        else: #난이도 최상
          self.radius = 10
          self.speed = 3
          self.my_attack = 8 #3~13
          self.enemy_attack = 20 # 15~25
          self.dot_alpha = 100
          self.dot_time = 1.3

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
class Level: # 클래스로 찍어내니까 random값이 한판 내에서 고정값이 되어버림
    def __init__(self, level):
        if level == 1: 
          self.radius = 20 
          self.speed = 5
          self.my_attack = 15 #10~20
          self.enemy_attack = 10 # 5~15
          self.dot_alpha = 200
          self.dot_time = 2
          # level 별 사진
          self.background_image = pygame.transform.scale(pygame.image.load('Images\Level_1.jpg'), (width, height)) if 'Images\Level_1.jpg' else None
          self.background_rect = self.background_image.get_rect()
          self.attacked_image =  pygame.transform.scale(pygame.image.load('Images\Level_1_attacked.png'), (width, height)) if 'Images\Level_1_attacked.png' else None
          self.attacked_rect = self.attacked_image.get_rect()
          self.defend_image =  pygame.transform.scale(pygame.image.load('Images\Level_1_defend.png'), (width, height)) if 'Images\Level_1_defend.png' else None
          self.defend_rect = self.defend_image.get_rect()

        elif level == 2:
          self.radius = 15 
          self.speed = 4
          self.my_attack = 10 #5~15
          self.enemy_attack = 15 #10~20
          self.dot_alpha = 150
          self.dot_time = 1.5

          self.background_image = pygame.transform.scale(pygame.image.load('Images\Level_2.png'), (width, height)) if 'Images\Level_2.png' else None
          self.background_rect = self.background_image.get_rect()
          self.attacked_image = pygame.transform.scale(pygame.image.load('Images\Level_2_attacked.png'), (width, height)) if 'Images\Level_2_attacked.png' else None
          self.attacked_rect = self.attacked_image.get_rect()
          self.defend_image = pygame.transform.scale(pygame.image.load('Images\Level_2_defend.png'), (width, height)) if 'Images\Level_2_defend.png' else None
          self.defend_rect = self.defend_image.get_rect()
          
        else: #난이도 최상
          self.radius = 10
          self.speed = 3
          self.my_attack = 8 #3~13
          self.enemy_attack = 20 # 15~25
          self.dot_alpha = 100
          self.dot_time = 1.3

          self.background_image = pygame.transform.scale(pygame.image.load('Images\Level_3.png'), (width, height)) if 'Images\Level_3.png' else None
          self.background_rect = self.background_image.get_rect()
          self.attacked_image = pygame.transform.scale(pygame.image.load('Images\Level_3_attacked.png'), (width, height)) if 'Images\Level_3_attacked.png' else None
          self.attacked_rect = self.attacked_image.get_rect()
          self.defend_image =pygame.transform.scale(pygame.image.load('Images\Level_3_defend.png'), (width, height)) if 'Images\Level_3_defend.png' else None
          self.defend_rect = self.defend_image.get_rect()

#특수효과음
class Sound:
    def __init__(self):
        self.attacked_sound = pygame.mixer.Sound('SoundTrack/attacked.mp3')
        self.died_sound = pygame.mixer.Sound('SoundTrack/died.wav')
        self.defend_sound = pygame.mixer.Sound('SoundTrack/enemy_attack_defend.wav')
        self.enemy_down_sound = pygame.mixer.Sound('SoundTrack/enemy_down.wav')
        self.my_attack_sound = pygame.mixer.Sound('SoundTrack/my_attack.wav')

        # Set the volume for each sound effect
        self.attacked_sound.set_volume(0.5)
        self.died_sound.set_volume(0.5)
        self.defend_sound.set_volume(0.7)
        self.enemy_down_sound.set_volume(0.5)
        self.my_attack_sound.set_volume(0.5)
    
   

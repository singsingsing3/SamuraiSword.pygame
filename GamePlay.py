import pygame
import sys
import random
import time
from Classes import Dot, Difficulty

# Pygame 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Dots")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 난이도 정의
level = Difficulty(1) #레벨 설정




# 게임 루프
dots = []
my_health = 100
enemy_health = 100
font = pygame.font.Font(None, 36)
next_dot_time_red = time.time() + 1  # 다음 빨간 점이 나타날 시간 초기화
next_dot_time_blue = time.time() + level.speed  # 다음 파란 점이 나타날 시간 초기화
freeze_time = 0  # 화면이 멈춰있는 시간

while enemy_health > 0 and my_health > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 새로운 빨간 점 생성 (1초에 한 번씩)
    if time.time() > next_dot_time_red and time.time() > freeze_time:
        dot = Dot(random.randint(20, width - 20),
                  random.randint(20, height - 20), color=RED, alpha=0, radius=level.radius)
        dots.append(dot)
        next_dot_time_red = time.time() + 1  # 다음 빨간 점이 나타날 시간 업데이트

    # 새로운 파란 점 생성 
    if time.time() > next_dot_time_blue and time.time() > freeze_time:
        # 중복된 파란 점을 방지하기 위해 이미 존재하는 파란 점인지 확인
        existing_blue_dots = [dot for dot in dots if dot.color == BLUE]
        if not existing_blue_dots:
            dot = Dot(random.randint(20, width - 20),  # 점이 화면에 잘리지 않도록 범위 설정
                      random.randint(20, height - 20), color=BLUE,  radius=level.radius,alpha=0)
            dots.append(dot)
            next_dot_time_blue = time.time() + level.speed  # 다음 파란 점이 나타날 시간 업데이트

    # 화면 업데이트
    screen.fill(WHITE)

    # 모든 점 그리기
    for dot in dots:
        dot.draw()
        # 페이드 인 효과
        if dot.color and dot.alpha < level.dot_alpha:
            dot.alpha += 2

    # 점수 표시
    my_text = font.render("Your HP: {}".format(my_health), True, RED)
    enemy_text = font.render("Enemy HP: {}".format(enemy_health), True, BLUE)
    screen.blit(my_text, (10, 10))
    screen.blit(enemy_text, (width-200, 10))

    # 점이 생성된 후 2초 후에 사라짐
    for dot in dots.copy():
        if time.time() - dot.creation_time > level.dot_time:  # 파란점이 제거되지 못하고 사라진 경우
            if dot.color == BLUE:  # 파란 점인 경우
                dots.clear()  # 모든 점 제거                
                my_health -= int(level.enemy_attack + random.uniform(-5, 6))
                freeze_time = time.time() + 2  # 화면을 2초 동안 멈춤
            elif dot.color == RED:  # 빨간 점인 경우
                dots.remove(dot)

    # 마우스 이벤트 처리
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            for dot in dots.copy():
                if dot.color == BLUE and 0 <= mouse_y <= 10:  # 상대 공격 방어
                    dots.clear()  # 모든 점 제거
                    freeze_time = time.time() + 2  # 화면을 2초 동안 멈춤
                elif dot.color == RED:  # 빨간 점이면
                    distance = pygame.math.Vector2(
                        dot.x - mouse_x, dot.y - mouse_y).length()
                    if distance < dot.radius:
                        dots.remove(dot)
                          # 적 체력 감소
                        enemy_health -= int(level.my_attack + random.uniform(-5, 6))

    # 2초동안 화면이 멈춰있는 동안
    if time.time() < freeze_time:
        pygame.display.flip()  # 화면 갱신
        continue  # 게임 루프 반복하지 않음

    # 화면 업데이트
    pygame.display.flip()


if my_health <= 0:   
    lose_font = pygame.font.Font(None, 48)
    lose = font.render("You Died!", True, RED)
    text_rect = lose.get_rect(center=(width // 2, height // 2))
    screen.blit(lose, text_rect.topleft)
    
elif enemy_health <= 0:  
    # Increase font size to 48 (adjust as needed)
    win_font = pygame.font.Font(None, 48)
    win = win_font.render("You Won!", True, BLUE)
    text_rect = win.get_rect(center=(width // 2, height // 2))
    screen.blit(win, text_rect.topleft)

pygame.display.flip()  # Display the game over message

# Event handling loop to keep the screen on
running = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # 키 누를시 게임종료
            running = False

pygame.quit()


import pygame
import sys
import random
import time
from Classes import Dot, Level, Sound

# Pygame initialization
pygame.init()

# Initialize pygame.mixer
pygame.mixer.init()

# Load background music and set volume
pygame.mixer.music.load('SoundTrack\Jim Yosef - Samurai [NCS Release]-[AudioTrimmer.com].mp3')
pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed
game_sound = Sound()

# Start playing background music
pygame.mixer.music.play(-1)  # -1 means play indefinitely

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Dots")

# color definition
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
my_health = 100
attacked = True
touched_bomb = True
defend = True


# Outer loop for game levels
for i in range(1, 4):


    # Difficulty definition
    level = Level(i)  # Level setting

    background_color = (BLACK)  # Black with varying alpha
    text_color = (WHITE)  # White with varying alpha

    screen.fill(background_color)  # Fill the background
    level_font = pygame.font.Font(None, 48)
    level_text = level_font.render("Get Ready For Level {}".format(i), True, text_color)
    text_rect = level_text.get_rect(center=(width // 2, height // 2))
    screen.blit(level_text, text_rect.topleft)

    pygame.display.flip()

    time.sleep(3)

    # game loop
    dots = []

    enemy_health = 100
    font = pygame.font.Font(None, 36)
    next_dot_time_red = time.time() + 1  # Initialize the time when the next red dot will appear
    next_dot_time_blue = time.time() + level.speed  # Initialize the time when the next blue dot will appear
    next_dot_time_bomb = time.time() + 1 # level 3를 위해 추가
    
    freeze_time = 0  # Time the screen is frozen

    while enemy_health > 0 and my_health > 0:
        screen.blit(level.background_image, level.background_rect)  # Draw the background image
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create a new red dot (once per second)
        if time.time() > next_dot_time_red and time.time() > freeze_time:
            dot = Dot(random.randint(20, width - 30),
                      random.randint(20, height - 50), color=RED, alpha=0, radius=level.radius)
            dots.append(dot)
            next_dot_time_red = time.time() + 1  # Update the time when the next red dot will appear

        # Create a new blue dot
        if time.time() > next_dot_time_blue and time.time() > freeze_time:
            # Check if the blue dot already exists to prevent duplicate blue dots
            existing_blue_dots = [dot for dot in dots if dot.color == BLUE]
            if not existing_blue_dots:
                dot = Dot(random.randint(20, width - 20),  # Set the range so that the dot is not cut off on the screen
                          random.randint(20, height - 20), color=BLUE, radius=level.radius, alpha=0)
                dots.append(dot)
                next_dot_time_blue = time.time() + level.speed  # Update the time when the next blue dot will appear

        # Create a new bomb dot (once per 2second)
        if time.time() > next_dot_time_bomb and time.time() > freeze_time and i == 3: # level 3일때 핑크점 추가
            dot = Dot(random.randint(20, width - 20),
                      random.randint(20, height - 20), color=BLACK, alpha=0, radius= 30)
            dots.append(dot)
            
            next_dot_time_bomb = time.time() + 1  # Update the time when the next red dot will appear



        # Draw all points
        for dot in dots:
            dot.draw()
            # Fade in effect
            if dot.color and dot.alpha < level.dot_alpha:
                dot.alpha += 2

        # Display score
        my_text = font.render("Your HP: {}".format(my_health), True, RED)
        enemy_text = font.render("Enemy HP: {}".format(enemy_health), True, BLUE)
        screen.blit(my_text, (10, 10))
        screen.blit(enemy_text, (width - 200, 10))

        # The dot disappears some seconds after it is created
        dots_to_remove = []
        for dot in dots.copy():
            if time.time() - dot.creation_time > level.dot_time:
                if dot.color == BLUE:
                    dots_to_remove.append(dot)
                    my_health -= int(level.enemy_attack + random.uniform(-5, 6))
                    attacked = True
                    touched_bomb = False
                    defend = False
                    freeze_time = time.time() + 1  # Freeze the screen for 2 seconds
                    game_sound.attacked_sound.play()
                elif dot.color == RED:
                    dots_to_remove.append(dot)
                elif dot.color == BLACK: # 폭탄 자동소멸
                    dots_to_remove.append(dot)
                   

        # Remove the dots outside of the loop
        for dot in dots_to_remove:
            if dots:
                dots.remove(dot)

        # Mouse event handling
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                for dot in dots.copy():
                    if dot.color == BLUE and 0 <= mouse_y <= 50:  # Defend opponent's attack
                        game_sound.defend_sound.play()
                        attacked = False
                        touched_bomb = False
                        defend = True
                        if i == 3:
                            my_health -= 5 #레벨 3부터는 방어해도 5데미지를 입는다
                        dots.clear()  # remove all dots
                        freeze_time = time.time() + 1  # Freeze the screen for 2 seconds

                    elif dot.color == RED:  # If red dot
                        distance = pygame.math.Vector2(
                            dot.x - mouse_x, dot.y - mouse_y).length()
                        if distance < dot.radius:
                            if dots: # 점이 있을 경우에만 제거
                                dots.remove(dot)
                            # Reduce enemy health
                            enemy_health -= int(level.my_attack + random.uniform(-5, 6))
                            game_sound.my_attack_sound.play()
                    elif i == 3 and dot.color == BLACK:  # If bomb dot
                        distance = pygame.math.Vector2(
                            dot.x - mouse_x, dot.y - mouse_y).length()
                        if distance < dot.radius:
                            if dots: # 점이 있을 경우에만 제거
                                dots.remove(dot)
                                attacked = False
                                touched_bomb = True
                                defend = False
                                my_health -= 30 #폭탄데미지
                                freeze_time = time.time() + 1  # Freeze the screen for 2 seconds
                                game_sound.touched_bomb_sound.play()


        # While the screen is still for 1 seconds
        if time.time() < freeze_time and attacked and not touched_bomb and not defend:
            screen.blit(level.attacked_image, level.attacked_rect)  # Draw the background image
            pygame.display.flip()  # Screen update
            
            continue  # do not repeat the game loop
        elif time.time() < freeze_time and not attacked and not touched_bomb and defend:
            screen.blit(level.defend_image, level.defend_rect)  # Draw the background image
            pygame.display.flip()  # Screen update
            continue  # do not repeat the game loop

        elif time.time() < freeze_time and not attacked and touched_bomb and not defend:
            screen.blit(level.bomb_image, level.bomb_rect)  # Draw the background image
            
            pygame.display.flip()  # Screen update
            
            continue  # do not repeat the game loop

        # Screen update
        pygame.display.flip()

    # Display the latest health value after the game ends
    screen.fill(WHITE)
    my_text = font.render("Your HP: {}".format(my_health), True, RED)
    enemy_text = font.render("Enemy HP: {}".format(enemy_health), True, BLUE)
    screen.blit(my_text, (10, 10))
    screen.blit(enemy_text, (width - 200, 10))

    if my_health <= 0:
        lose_font = pygame.font.Font(None, 48)
        screen.fill(background_color)
        lose = font.render("You Died!", True, RED)
        game_sound.died_sound.play()
        text_rect = lose.get_rect(center=(width // 2, height // 2))
        screen.blit(lose, text_rect.topleft)

    elif enemy_health <= 0:
        # Increase font size to 48 (adjust as needed)
        win_font = pygame.font.Font(None, 48)
        game_sound.enemy_down_sound.play()
        screen.fill(background_color)
        win = win_font.render("You Won!", True, BLUE)
        text_rect = win.get_rect(center=(width // 2, height // 2))
        screen.blit(win, text_rect.topleft)

    pygame.display.flip()  # Display the game over message
    time.sleep(4)  # Pause for 4 seconds before moving to the next level

# Game Finished
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Game ends when key is pressed
            running = False
pygame.mixer.music.stop()  # Music stops
pygame.quit()

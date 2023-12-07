import sys
import pygame, csv
from Playing_Game_py_Files.Initial_Game_Screen import display_main_menu
from Playing_Game_py_Files.Game_Play import play_game
# Please Read README.md File!
# You can Play Game on this Main.py

# Pygame initialization
pygame.init()

# Initialize pygame.mixer
pygame.mixer.init()

# Load background music and set volume
pygame.mixer.music.load('SoundTrack\VØJ & ATSMXN - Blade Fury [NCS Release].mp3')
pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed


# Start playing background music
pygame.mixer.music.play(-1)  # -1 means play indefinitely



# color definition
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Samurai Sword")

# Main Screen
display_main_menu(screen, width, height)

# Load background music and set volume
pygame.mixer.music.load('SoundTrack\Jim Yosef - Samurai [NCS Release]-[AudioTrimmer.com].mp3')
pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed


# Start playing background music
pygame.mixer.music.play(-1)  # -1 means play indefinitely



# play Game
current = play_game(screen, width, height, BLACK, WHITE, RED, BLUE)

# Hall of Fame
# Step 1: Open the file
score_arr = []

# Open the TXT file for reading
with open('TXT_Files/Hall_Of_Fame.txt', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file, delimiter='|')

    # Skip the header row
    next(reader)

    for line in reader:
        # Extract the values from the current line
        remain_hp = int(line[1].strip())
        clear_time = line[2].strip()
        score_arr.append([remain_hp, clear_time])
    
# Step 3: Append the current score and current time to score_arr
score_arr.append([current[0][0], current[0][1]])

# Step 4: Reverse sort score_arr based on score
score_arr.sort(reverse=True, key=lambda x: x[0])

# Step 5: Save up to 9 scores
score_arr = score_arr[:9]

# Step 6: Load the scores and dates from score_arr and write them in the file and Hall of Fame DisPlay
with open('TXT_Files/Hall_of_Fame.txt', 'w') as file:
    file.write("       Remain_HP    Clear_Time  \n")
    for i, (score, date) in enumerate(score_arr, start=1):
        file.write(f"{i}.  |     {score}      | {date}\n")


# Read the file content
with open('TXT_Files/Hall_Of_Fame.txt', 'r') as file:
    content = file.read()

# Split the content into lines
lines = content.split('\n')

# Main loop

while True:
    # Draw background
    screen.fill(BLACK)
    font = pygame.font.Font(None, 48)
    # Display each line on the screen
    y_position = 100
    for line in lines:
        text_surface = font.render(line, True, WHITE)
        text_rect = text_surface.get_rect(center=(width // 2, y_position))
        screen.blit(text_surface, text_rect.topleft)
        y_position += text_rect.height  # Move down for the next line

    quit_text = font.render("Press 'Any Key' to Quit", True, pygame.Color("blue"))
    quit_rect = quit_text.get_rect(center=(width // 2, height - 50))
    screen.blit(quit_text, quit_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            pygame.mixer.music.stop()  # Music stops
            pygame.quit()
            sys.exit()
            

    









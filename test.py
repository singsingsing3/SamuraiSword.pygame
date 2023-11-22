import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Define the color red
red = (255, 0, 0)

# Calculate the height for the top 80%
top_height = 100

# Create a surface for the top portion and fill it with red
top_surface = pygame.Surface((width, top_height))
top_surface.fill(red)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Blit the top surface onto the screen
    screen.blit(top_surface, (0, 0))

    # Update the display
    pygame.display.flip()
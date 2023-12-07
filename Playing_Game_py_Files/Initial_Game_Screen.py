# Initial_Game_Screen.py

import pygame


def display_main_menu(screen, width, height):
    main_menu = True
    main_image  =pygame.transform.scale(pygame.image.load('Images\Main.png'), (width, height)) if 'Images\Main.png' else None
    main_rect = main_image.get_rect()
    menu_font = pygame.font.Font(None, 48)
    title_font = pygame.font.Font(None, 70)
    # Display menu options
    title_text = title_font.render("Samurai Sword", True, pygame.Color("red"))
    start_text = menu_font.render("1. Start Game", True, pygame.Color("black"))
    instructions_menu_text = menu_font.render("2. Instructions", True, pygame.Color("black"))
    

    title_rect = title_text.get_rect(center=(width // 2, 100))
    start_rect = start_text.get_rect(center=(width // 2, height // 2 ))
    instructions_menu_rect = instructions_menu_text.get_rect(center=(width // 2, height // 2 + 100))
    screen.blit(main_image, main_rect)  # Draw the background image

    while main_menu:  # main menu
        pygame.display.flip()

        screen.blit(title_text, title_rect.topleft)
        screen.blit(start_text, start_rect.topleft)
        screen.blit(instructions_menu_text, instructions_menu_rect.topleft)
        pygame.display.flip()
        # Event handling for the main menu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main_menu = False  # Start the game
                elif event.key == pygame.K_2:
                    with open('TXT_Files/how_to_play.txt', 'r', encoding='utf-8') as file:
                        # Display instructions (you can implement this part)
                        instructions_font = pygame.font.Font(None, 24)
                        y_position = 50
                        screen.blit(main_image, main_rect)  # Draw the background image

                        for line in file:
                            line = line.strip()  # Remove leading/trailing whitespaces

                            instructions_text = instructions_font.render(line, True, pygame.Color("black"))
                            instructions_rect = instructions_text.get_rect(center=(width // 2, y_position))

                            screen.blit(instructions_text, instructions_rect.topleft)
                            pygame.display.flip()

                            y_position += instructions_rect.height  # Move down for the next line

                    quit_text = menu_font.render("Press 'Q' to return to the main menu", True, pygame.Color("blue"))
                    quit_rect = instructions_text.get_rect(center=(width // 2, height - 50))
                    screen.blit(quit_text, quit_rect.topleft)
                    
                    pygame.display.flip()

                    # Wait for 'Q' key to return to the main menu
                    waiting_for_q = True
                    while waiting_for_q:
                        for event_q in pygame.event.get():
                            if event_q.type == pygame.KEYDOWN and event_q.key == pygame.K_q:
                                waiting_for_q = False  # Stop waiting for 'Q'
                                screen.blit(main_image, main_rect)  # Draw the background image
                                pygame.display.flip()
                                main_menu = True  # Return to the main menu
                                break

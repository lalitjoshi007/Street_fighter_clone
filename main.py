# Street Fighter Game
# By: lalit joshi
# Date: 
# Version: 1.0
# Description: This is the main file for the Street Fighter Game.
#             It contains the main game loop and the main game functions.
#             It also contains the main menu and the game over screen.
#             It also contains the high score screen.
#             It also contains the pause screen.
#             It also contains the game over screen.
# Adapted from:
# Coding With Rose
# Youtube URL: https://www.youtube.com/watch?v=s5bd9KMSSW4
# GitHub URL: https://github.com/russs123/brawler_tut


import pygame
import sys
from pygame import mixer
from fighter import Fighter  # Assuming you have a separate file named 'fighter.py' containing the Fighter class
import os  # Required for loading audio files
from moviepy.editor import VideoFileClip
try:
    continue_game_loop = True
    while continue_game_loop:
        # continue_game_loop = True
        
        # Initialize Pygame
        pygame.init()
        # Initialize joystick module
        pygame.joystick.init()


        # Initialize the font module
        pygame.font.init()

        # Get screen width and height
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h


        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Street Fighter!")

        # Set up clock
        clock = pygame.time.Clock()
        FPS = 60

        # Define colors
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        BLACK = (0, 0, 0)
        GRAY = (128, 128, 128)
        volume_on = True  # Initial volume state is on
        # Define fonts
        title_font = pygame.font.Font(None, 80)
        text_font = pygame.font.Font(None, 36)




        # Player details entry
        player1_text = ""
        player2_text = ""
        player1_active = True
        player2_active = False

        CURRENT_DIR = os.path.dirname(__file__)
        selected_background = 0

        # Load the opening music
        pygame.mixer.init()
        opening_music = pygame.mixer.Sound(os.path.join(CURRENT_DIR, "assets\\audio\\stylish-rock-beat-trailer-116346.mp3"))

        # for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             continue_game_loop = False
        #             pygame.quit()
        #         elif event.type == pygame.KEYDOWN:
        #                 if event.key == pygame.K_ESCAPE:
        #                     continue_game_loop = False
        #                     print(continue_game_loop,"Game Loop Flag>>>>>>>>>>>>>>>")
        #                     pygame.quit()

        # Function to draw text input
        def draw_text_input():
            player1_surface = text_font.render(player1_text, True, WHITE)
            player2_surface = text_font.render(player2_text, True, WHITE)

            screen.blit(player1_surface, (SCREEN_WIDTH // 2 - player1_surface.get_width() // 2, 300))
            screen.blit(player2_surface, (SCREEN_WIDTH // 2 - player2_surface.get_width() // 2, 400))

            pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 200, 290, 400, 40), 2)
            pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 200, 390, 400, 40), 2)
        # Load the background selection music
        background_selection_music = pygame.mixer.Sound(os.path.join(CURRENT_DIR, "assets\\audio\\stylish-rock-beat-trailer-116346.mp3"))

        def draw_text(text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))
        volume_on = True  # Initial volume state is on
        def toggle_volume():
            global volume_on 
            volume_on = not volume_on
            pygame.mixer.music.set_volume(0.5 if volume_on else 0)
        def settings_page(screen):
            running_settings = True
            button_font = pygame.font.Font(None, 36)
            # Load the image for the settings page
            settings_image = pygame.image.load("assets\\images\\welcome_page\\welcome.jpg").convert_alpha()
            settings_image = pygame.transform.scale(settings_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            while running_settings:
                screen.fill((0, 0, 0))
                # Blit the settings image onto the screen
                screen.blit(settings_image, (0, 0))
                draw_text("Settings Page", title_font, WHITE, SCREEN_WIDTH // 2, 100)

                # Draw "Volume On" and "Volume Off" buttons
                volume_text = "Volume On" if volume_on else "Volume Off"
                volume_button_text = button_font.render(volume_text, True, WHITE)
                volume_button_rect = volume_button_text.get_rect()
                volume_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                pygame.draw.rect(screen, GRAY, volume_button_rect, 2)
                screen.blit(volume_button_text, volume_button_rect)
                
                # Draw the "Back" button
                back_button_text = button_font.render("Back", True, WHITE)
                back_button_rect = back_button_text.get_rect()
                back_button_rect.topleft = (20, SCREEN_HEIGHT - 50)
                pygame.draw.rect(screen, GRAY, (10, SCREEN_HEIGHT - 60, back_button_rect.width + 20, back_button_rect.height + 10))
                screen.blit(back_button_text, (20, SCREEN_HEIGHT - 50))

                # Handle events for the settings page
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            # continue_game_loop = False
                            running_settings = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if back_button_rect.collidepoint(mouse_x, mouse_y):
                            running_settings = False
                        elif volume_button_rect.collidepoint(mouse_x, mouse_y):
                            toggle_volume()

                pygame.display.flip()
                clock.tick(FPS)

        def reset_game():
            global intro_count, last_count_update, score, round_over, fighter_1, fighter_2
            intro_count = 3
            last_count_update = pygame.time.get_ticks()
            score = [0, 0]
            round_over = False
            fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
            fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, staff_fx)



        # Background selection function
        def background_selection(screen):
            background_selection_music.play()
            # Define background images
            backgrounds = [
                pygame.image.load("assets/images/background/1.jpg").convert_alpha(),
                pygame.image.load("assets/images/background/2.jpg").convert_alpha(),
                pygame.image.load("assets/images/background/3.jpg").convert_alpha()
            ]

            selected_background = 0  # Default selected background
            selection_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, 200, 600, 450)  # Rectangle for background selection
            # Draw background selection menu
            screen.fill((0, 0, 0))
            title_text = title_font.render("Select Background:", True, RED)
            screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
            

            # Handle background selection
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if selection_rect.collidepoint(mouse_x, mouse_y):
                            for i in range(len(backgrounds)):
                                if 200 + i * 150 <= mouse_y <= 200 + i * 150 + backgrounds[i].get_height():
                                    selected_background = i
                                    background_selection_music.stop()
                                    return backgrounds[selected_background]
                for i, bg in enumerate(backgrounds):
                    screen.blit(bg, (SCREEN_WIDTH // 2 - bg.get_width() // 2, 200 + i * 150))
                    if selection_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 302, 198 + i * 150, 604, 154), 2)
                # Draw the selection rectangle
                pygame.draw.rect(screen, WHITE, selection_rect, 2)

                pygame.display.flip()
                clock.tick(FPS)


        # Load the MP4 video file
        backstory_video = VideoFileClip("assets\\video\\video.mp4")

        #Play the video (you may need to install the necessary video player)
        backstory_video.preview()



        welcome_image = pygame.image.load("assets/images/welcome page/welcome.jpg").convert_alpha()
        welcome_image = pygame.transform.scale(welcome_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        button_font = pygame.font.Font(None, 36)
        # Welcome page loop
        welcome_page = True
        running = True
        while welcome_page:
            screen.fill((0, 0, 0))
            # Draw the welcome image
            screen.blit(welcome_image, (0, 0))
            # Play the opening music
            background_selection_music.play()

            # Draw the "Settings" button
            settings_button_text = button_font.render("Settings", True, WHITE)
            settings_button_rect = settings_button_text.get_rect()
            settings_button_rect.topright = (SCREEN_WIDTH - 20, 20)
            pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - settings_button_rect.width - 30, 10, settings_button_rect.width + 20, settings_button_rect.height + 10))
            screen.blit(settings_button_text, (SCREEN_WIDTH - settings_button_rect.width - 20, 20))

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    welcome_page = False
                    running = False
                    continue_game_loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if player1_active:
                            if len(player1_text) > 0:  # Check if player 1 name is not empty
                                player1_active = False
                                player2_active = True
                        elif player2_active:
                            if len(player2_text) > 0:  # Check if player 2 name is not empty
                                welcome_page = False  # Both players entered their names, exit welcome page
                    elif event.key == pygame.K_BACKSPACE:
                        if player1_active:
                            player1_text = player1_text[:-1]
                        elif player2_active:
                            player2_text = player2_text[:-1]
                    else:
                        if player1_active and len(player1_text) < 15:  # Limiting player name length to 15 characters
                            player1_text += event.unicode
                        elif player2_active and len(player2_text) < 15:
                            player2_text += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if settings_button_rect.collidepoint(mouse_x, mouse_y):
                        settings_page(screen)

            
            # Stop the opening music after the welcome page
            opening_music.stop()
            # Draw welcome page
            title_text = title_font.render("Street Fighter", True, RED)
            screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

            instructions_text = text_font.render("Enter Player Names and Press Enter to Start", True, RED)
            screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, 200))

            draw_text_input()
        
            # Toggle active player
            if player1_active:
                pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 202, 288, 404, 44), 2)
            elif player2_active:
                pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 202, 388, 404, 44), 2)

            pygame.display.flip()
            clock.tick(FPS)


        round_selection_image = pygame.image.load("assets\\images\\round image\\rounds.jpg").convert_alpha()
        round_selection_image = pygame.transform.scale(round_selection_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


        # Round selection loop
        rounds_selected = False
        while not rounds_selected:
            # Draw welcome page and buttons for selecting rounds
            screen.fill((0, 0, 0))
            # Blit the round selection image onto the screen
            screen.blit(round_selection_image, (0, 0))
            title_text = title_font.render("Select Number of Rounds", True, RED)
            screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

            # Draw the "3 Rounds" and "5 Rounds" buttons
            pygame.draw.rect(screen, GRAY, (350, 300, 300, 50))
            pygame.draw.rect(screen, GRAY, (350, 400, 300, 50))
            draw_text("3 Rounds", button_font, WHITE, 400, 310)
            draw_text("5 Rounds", button_font, WHITE, 400, 410)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    continue_game_loop = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 350 <= mouse_x <= 650 and 300 <= mouse_y <= 350:  # Check if the "3 Rounds" button is clicked
                        rounds = 3
                        rounds_selected = True
                    elif 350 <= mouse_x <= 650 and 400 <= mouse_y <= 450:  # Check if the "5 Rounds" button is clicked
                        rounds = 5
                        rounds_selected = True

            pygame.display.flip()
            clock.tick(FPS)

            
        # Main game loop
        if running:

            # Get the selected background image
            bg_image = background_selection(screen)
            background_selection_music.stop()
            
            pygame.mixer.music.set_volume(0.5 if volume_on else 0)
            # Set up game variables
            # SCREEN_WIDTH = 1000
            # SCREEN_HEIGHT = 600
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Street Fighter!")

            # Set Framerate
            FPS = 60

            # Define colors
            RED = (255, 0, 0)
            YELLOW = (255, 255, 0)
            WHITE = (255, 255, 255)

            # Define Game Intro Count Variables
            intro_count = 3
            last_count_update = pygame.time.get_ticks()

            # Define Variables For Player Game Score
            score = [0, 0]
            round_over = False
            ROUND_OVER_COOLDOWN = 2000

            # Define Fighter Sprite Sheet Image Variables dynamically based on screen size
            # WARRIOR_BASE_SIZE = 162
            # WARRIOR_BASE_SCALE = 2
            # WARRIOR_BASE_OFFSET = [72, 56]

            # WIZARD_BASE_SIZE = 250
            # WIZARD_BASE_SCALE = 1
            # WIZARD_BASE_OFFSET = [112, 107]

            # Define Fighter Sprite Sheet Image Variables
            WARRIOR_SIZE = 162  # Adjusted size for the warrior sprite
            WARRIOR_SCALE = 4   # Adjusted scale for the warrior sprite
            WARRIOR_OFFSET = [72, 56]  # Adjusted offset for the warrior sprite

            WIZARD_SIZE = 250  # Adjusted size for the wizard sprite
            WIZARD_SCALE = 3   # Adjusted scale for the wizard sprite
            WIZARD_OFFSET = [112, 107]  # Adjusted offset for the wizard sprite
            WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
            WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

            # # Calculate scaled values based on screen size
            # WARRIOR_SIZE = int((SCREEN_WIDTH / 1000) * WARRIOR_BASE_SIZE)  # Adjusted size for the warrior sprite
            # WARRIOR_SCALE = int((SCREEN_WIDTH / 1000) * WARRIOR_BASE_SCALE)  # Adjusted scale for the warrior sprite
            # WARRIOR_OFFSET = [int((SCREEN_WIDTH / 1000) * offset) for offset in WARRIOR_BASE_OFFSET]  # Adjusted offset for the warrior sprite
            # 
            # WIZARD_SIZE = int((SCREEN_WIDTH / 1000) * WIZARD_BASE_SIZE)  # Adjusted size for the wizard sprite
            # WIZARD_SCALE = int((SCREEN_WIDTH / 1000) * WIZARD_BASE_SCALE)  # Adjusted scale for the wizard sprite
            # WIZARD_OFFSET = [int((SCREEN_WIDTH / 1000) * offset) for offset in WIZARD_BASE_OFFSET]  # Adjusted offset for the wizard sprite
            # 

            # Load music and sounds
            pygame.mixer.music.load("assets/audio/music.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, 0.0, 5000)

            # Load warrior sword and wizard staff sound effect
            sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
            sword_fx.set_volume(0.75)
            staff_fx = pygame.mixer.Sound("assets/audio/magic.wav")
            staff_fx.set_volume(0.75)

            # Load Warrior Sprite sheets Of Images
            warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
            # Load Wizard Sprite sheets Of Images
            wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

        
        # Implement Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    continue_game_loop = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

            # Update Display
            pygame.display.update()
        
        # Load Victory Image
        victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

        # Define number of steps in each animation for Warrior and Wizard Player
        WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
        WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

        # Define Fonts
        count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
        score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

        # Function for drawing text
        def draw_text(text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))

        # Function For Drawing Background
        def draw_bg():
            scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(scaled_bg, (0, 0))

        # Function For Drawing Fighter Health Bar
        def draw_health_bar(health, x, y):
            BAR_COLOR = (255, 0, 0)  # Red color for the health bar
            BACKGROUND_COLOR = (64, 64, 64)  # Dark gray color for the background
            BORDER_COLOR = (128, 128, 128)  # Gray color for the border

            # Define dimensions for the health bar
            BAR_LENGTH = 700
            BAR_HEIGHT = 40
            BORDER_WIDTH = 2
            ratio = health / 100
            # Draw the background rectangle
            pygame.draw.rect(screen, BACKGROUND_COLOR, (x - BORDER_WIDTH, y - BORDER_WIDTH, BAR_LENGTH + 2 * BORDER_WIDTH, BAR_HEIGHT + 2 * BORDER_WIDTH))

            # Draw the border rectangle
            pygame.draw.rect(screen, BORDER_COLOR, (x - BORDER_WIDTH, y - BORDER_WIDTH, BAR_LENGTH + 2 * BORDER_WIDTH, BAR_HEIGHT + 2 * BORDER_WIDTH), BORDER_WIDTH)

            # Draw the health bar
            pygame.draw.rect(screen, BAR_COLOR, (x, y, int(BAR_LENGTH * ratio), BAR_HEIGHT))
        # Create Two Instances Of Fighter
        fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
        fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, staff_fx)

        # Create Game Loop
        run = True

        # Game loop flags
        in_game = True
        on_welcome_page = False


        # Initialize round count and wins for each player
        round_count = 0
        player1_wins = 0
        player2_wins = 0

        winner_page = False  # Define winner_page variable


        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False  #
                            continue_game_loop = False
                
                
        
            # Draw Background
            draw_bg()

            # Create a button surface and font for the button text
            button_font = pygame.font.Font(None, 36)
            button_text = button_font.render("Back to Welcome", True, WHITE)
            button_rect = button_text.get_rect()
            button_rect.topright = (20, SCREEN_HEIGHT - 50)

            # Replace with your specific button coordinates and text
            game_page_button_text = "Welcome Page"
            game_page_button_rect = button_font.render(game_page_button_text, True, WHITE).get_rect()
            game_page_button_rect.topleft = (20, SCREEN_HEIGHT - 50)

            welcome_page_button_text = "Go to Game"
            welcome_page_button_rect = button_font.render(welcome_page_button_text, True, WHITE).get_rect()
            welcome_page_button_rect.topleft = (80, SCREEN_HEIGHT - 50)

            # Draw the button
            pygame.draw.rect(screen, GRAY, (10, SCREEN_HEIGHT - 60, button_rect.width + 20, button_rect.height + 10))
            screen.blit(button_text, (20, SCREEN_HEIGHT - 50))

            # Show Player Stats
            draw_health_bar(fighter_1.health, 20, 20)
            draw_health_bar(fighter_2.health, 1200, 20)
            draw_text(player1_text + str(score[0]), score_font, WHITE, 20, 60)
            draw_text(player2_text + str(score[1]), score_font, WHITE, 1200, 60)

            # Update Countdown
            if intro_count <= 0:
                # Move Fighters
                fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
                fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
            else:
                # display count timer
                draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
                # Update count timer
                if (pygame.time.get_ticks() - last_count_update) >= 1000:
                    intro_count -= 1
                    last_count_update = pygame.time.get_ticks()




            # Update Fighters
            fighter_1.update()
            fighter_2.update()

            # Draw Fighters
            fighter_1.draw(screen)
            fighter_2.draw(screen)

            # Check for player defeat
            if not round_over:
                if not fighter_1.alive:
                    score[1] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
                elif not fighter_2.alive:
                    score[0] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
            else:
                # Display "Victory" Image
                screen.blit(victory_img, (800, 150))
                if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                    round_over = False
                    intro_count = 3
                    round_count += 1
                    # Update player wins based on the current round outcome
                    if fighter_1.alive:
                        player1_wins += 1
                    elif fighter_2.alive:
                        player2_wins += 1
                    # Check if all rounds are completed
                    if round_count >= rounds:
                        run = False  # Exit game loop
                        # Determine winner
                        if player1_wins > player2_wins:
                            winner = player1_text
                        elif player2_wins > player1_wins:
                            winner = player2_text
                        else:
                            winner = "It's a tie!"
                    
                        # Exit the game loop and go to the winning page loop
                        run = False
                        winner_page = True
                    
                    # Create Two Instances Of Fighter
                    fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx,)  # Set fighter_1 as AI-controlled
                    fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, staff_fx,)  # Set fighter_2 as human-controlled
            
            
            
            
            # Implement Event Handler
            #for event in pygame.event.get():
                
            #   if event.type == pygame.QUIT:
            #      run = False
            #  elif event.type == pygame.MOUSEBUTTONDOWN:
            #      print('Inside the mouse button')
            #      mouse_x, mouse_y = pygame.mouse.get_pos()
            #     print('Inside the mouse button collide button',mouse_x,'---',mouse_y)
            #     if button_rect.collidepoint(mouse_x, mouse_y):
                #        print('Inside the mouse button collide button')
                #        welcome_page = True
                        
                    
            
            # Update the display
            pygame.display.flip()


        # Winning page loop
        while winner_page:
            clock.tick(FPS)

            
            # Draw Background
            # draw_bg()
            winner_image = pygame.image.load("assets\\images\\winner_image\\winner.jpg").convert_alpha()
            winner_image = pygame.transform.scale(winner_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(winner_image, (0, 0))
            # Draw winner text
            winner_text = title_font.render("Winner: " + winner, True, RED)
            screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, 300))

            # Draw the "Back" button
            back_button_text = button_font.render("Back", True, WHITE)
            back_button_rect = back_button_text.get_rect()
            back_button_rect.topleft = (20, SCREEN_HEIGHT - 50)
            pygame.draw.rect(screen, GRAY, (10, SCREEN_HEIGHT - 60, back_button_rect.width + 20, back_button_rect.height + 10))
            screen.blit(back_button_text, (20, SCREEN_HEIGHT - 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    winner_page = False
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running_settings = False
                            continue_game_loop = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_x, mouse_y):
                        # reset_game()
                        running = True
                        winner_page = False  # Exit the winner page loop
                        welcome_page = True  # Enter the welcome page loop
                        pygame.display.flip()

            pygame.display.flip()

        # Reset the game state before returning to the welcome page
        # reset_game()

        # Go back to the welcome page loop
        welcome_page = True


        # Exit PyGame
        pygame.quit()
except Exception as e:
    print("An error occurred:", e)
        #   You can add code here to handle the exception, such as logging the error or displaying an error message to the user.



import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter")

# Set up clock
clock = pygame.time.Clock()
FPS = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define fonts
font = pygame.font.Font(None, 36)

# Player details entry
player1_text = ""
player2_text = ""
player1_active = True
player2_active = False

# Character selection
character_index = 0
characters = ["Warrior", "Wizard", "Ninja"]  # List of character options

# Function to draw text input
def draw_text_input():
    player1_surface = font.render(player1_text, True, WHITE)
    player2_surface = font.render(player2_text, True, WHITE)

    screen.blit(player1_surface, (SCREEN_WIDTH // 2 - player1_surface.get_width() // 2, 300))
    screen.blit(player2_surface, (SCREEN_WIDTH // 2 - player2_surface.get_width() // 2, 400))

    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 200, 290, 400, 40), 2)
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 200, 390, 400, 40), 2)

# Function to draw character selection
def draw_character_selection():
    character_surface = font.render("Select Character: " + characters[character_index], True, WHITE)
    screen.blit(character_surface, (SCREEN_WIDTH // 2 - character_surface.get_width() // 2, 200))

# Welcome page loop
welcome_page = True
running = True
while welcome_page:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            welcome_page = False
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if player1_active:
                    player1_active = False
                    player2_active = True
                elif player2_active:
                    welcome_page = False  # Both players entered their names, exit welcome page
            elif event.key == pygame.K_BACKSPACE:
                if player1_active:
                    player1_text = player1_text[:-1]
                elif player2_active:
                    player2_text = player2_text[:-1]
            elif event.key == pygame.K_UP:  # Navigate character selection upwards
                character_index = (character_index - 1) % len(characters)
            elif event.key == pygame.K_DOWN:  # Navigate character selection downwards
                character_index = (character_index + 1) % len(characters)

    # Draw welcome page
    welcome_text = font.render("Welcome to Street Fighter!", True, RED)
    screen.blit(welcome_text, (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, 100))

    instructions_text = font.render("Enter Player Names and Press Enter to Start", True, WHITE)
    screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, 150))

    draw_text_input()
    draw_character_selection()

    # Toggle active player
    if player1_active:
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 202, 288, 404, 44), 2)
    elif player2_active:
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 202, 388, 404, 44), 2)

    pygame.display.flip()
    clock.tick(FPS)

# Main game loop
if running:
    # Rest of your game code goes here...
    pass

# Quit Pygame
pygame.quit()
sys.exit()

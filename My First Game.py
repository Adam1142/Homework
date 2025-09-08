import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("my first game")

# Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # rectangle color

# Rectangle settings
rect_width, rect_height = 100, 60
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Font settings
font = pygame.font.SysFont(None, 48)
text = font.render("Hello, Game!", True, (0, 0, 0))  # Black text
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 4))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rect)

    # Draw text
    screen.blit(text, text_rect)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()

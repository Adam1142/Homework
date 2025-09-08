import pygame
import sys

# Initialize pygame
pygame.init()

# Window settings
WINDOW_SIZE = (500, 500)
BACKGROUND_COLOR = (58, 58, 58)
pygame.display.set_caption("my first game screen")

# Create the screen
screen = pygame.display.set_mode(WINDOW_SIZE)

# Load and resize image
image = pygame.image.load("python.jpg")
image = pygame.transform.scale(image, (300, 300))

# Get image rect and center it
image_rect = image.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw image
    screen.blit(image, image_rect)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()

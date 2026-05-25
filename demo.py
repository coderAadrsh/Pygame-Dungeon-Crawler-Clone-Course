import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Position Display")

# Set up font for displaying text
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    # Fill the screen with a color (black)
    screen.fill((0, 0, 0))

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Render the mouse position text
    text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (255, 255, 255))
    
    # Blit the text to the screen
    screen.blit(text, (20, 20))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

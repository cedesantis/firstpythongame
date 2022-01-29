#Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT, 
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame

#initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

#Game loop
while running:
    for event in pygame.event.get():
        #did user hit a key?
        if event.type == KEYDOWN:
        #was it the escape key?  end execution if it was
            if event.key == K_ESCAPE:
                running = False
            #Close if the user clicked the window close button
            elif event.type == QUIT:
                running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    surf = pygame.Surface((50,50))
    # Create a surface and pass in a tuple containing its length and width
    surf.fill((0,0,0))
    rect = surf.get_rect()

    # Put the center of surf at the center of the display
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)


# This line says "Draw surf onto the screen at the center"
screen.blit(surf, surf_center)
pygame.display.flip()

            

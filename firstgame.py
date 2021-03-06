# learning from https://realpython.com/pygame-a-primer/#background-and-setup
#Import the pygame module
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT, 
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

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
    def update (self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
            # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect=self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randin(5,20)
        
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

#initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

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
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))
    
       # Draw the player on the screen
    screen.blit(player.surf, player.rect)
    
    pygame.display.flip()

    

            

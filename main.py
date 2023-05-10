# Importing modules
import pygame
import random
import math
# Initializing pygame
pygame.init()
# Setting up pygame screen
pygame.display.set_caption('src/Fish Game')
icon = pygame.image.load('src/fishIcon.png')
pygame.display.set_icon(icon)
# Screen size
width = 960
height = 540
screen = pygame.display.set_mode((width, height))
# Background
background = pygame.image.load('src/background.jpg')
backgroundX = 0
backgroundWidth = 1920
# Game Components
# Bubbles
green_30 = pygame.image.load('src/green_30.png')
green_30X = 970
green_30Y = random.randint(20, 500)
green_40 = pygame.image.load('src/green_40.png')
green_40X = 1200
green_40Y = random.randint(20, 500)
green_50 = pygame.image.load('src/green_50.png')
green_50X = 1500
green_50Y = random.randint(20, 500)
red = pygame.image.load('src/red.png')
redX = 1500
redY = random.randint(20, 500)


def bubbleGenerator(bubble, x, y):
    screen.blit(bubble, (x, y))


# Fish
fish = pygame.image.load('src/fish.png')
fishX = 20
fishX_change = 0
fishY = 200
fishY_change = 0


def fishPosition(x, y):
    screen.blit(fish, (x, y))


# Score
score = 0
colour = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 20)


def scoreGenerator(text, font):
    text = font.render(text, True, colour)
    screen.blit(text, (700, 15))


# Game over
gameover = pygame.image.load('src/gameover.png')


def distance(x1, y1, x2, y2):
    answer = math.sqrt(((x2 - (x1+50))**2) + ((y2 - (y1+50))**2))
    return answer


# Running pygame screen until escape condition
running = True
while running:
    # For filling screen with any colour using RGB
    screen.fill((0, 0, 0))
    # Adding and moving background image
    screen.blit(background, (backgroundX, 0))
    backgroundWidth -= 0.5
    screen.blit(background, (backgroundWidth, 0))
    backgroundX -= 0.5
    if backgroundX <= -1920:
        backgroundX = 0
        backgroundWidth = 1920
    # Checking all the event occurred while single iteration of while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Events of pressing keys
        if event.type == pygame.KEYDOWN:
            # Changes fishs co-ordinates on pressing respective keys
            if event.key == pygame.K_SPACE:
                fishY_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                fishY_change = 0.98
    # Limiting fish movement in the screen
    if fishY+fishY_change <= 0 or fishY+fishY_change >= 440:
        fishY_change = 0
    # Generating bubbles
    bubbleGenerator(green_30, green_30X, green_30Y)
    bubbleGenerator(green_40, green_40X, green_40Y)
    bubbleGenerator(green_50, green_50X, green_50Y)
    bubbleGenerator(red, redX, redY)
    # Changing fish position
    fishY += fishY_change
    fishPosition(fishX, fishY)
    fishPosition(fishX, fishY)
    # Checking for collisions by calculating distance b/w fish and the bubbles
    distanceGreen_30 = distance(fishX, fishY, green_30X, green_30Y)
    distanceGreen_40 = distance(fishX, fishY, green_40X, green_40Y)
    distanceGreen_50 = distance(fishX, fishY, green_50X, green_50Y)
    distanceRed = distance(fishX, fishY, redX, redY)
    if distanceGreen_30 <= 40:
        score += 50
    if distanceGreen_40 <= 40:
        score += 100
    if distanceGreen_50 <= 40:
        score += 150
    # Updating score
    text = "Score: " + str(score)
    scoreGenerator(text, font)
    # Controlling speed and reseting bubbles on no NO collision
    green_30X -= 1.5
    if green_30X <= 0 or distanceGreen_30 <= 40:
        green_30X = random.randint(960, 1500)
        green_30Y = random.randint(15, 500)
    green_40X -= 2
    if green_40X <= 0 or distanceGreen_40 <= 40:
        green_40X = random.randint(960, 1500)
        green_40Y = random.randint(15, 500)
    green_50X -= 2.5
    if green_50X <= 0 or distanceGreen_50 <= 40:
        green_50X = random.randint(960, 1500)
        green_50Y = random.randint(15, 500)
    redX -= 3
    if redX <= 0:
        redX = random.randint(960, 1500)
        redY = random.randint(15, 500)
    if distanceRed <= 30:
        screen.blit(gameover, (350, 200))
        pygame.display.update()
        running = False
        pygame.time.delay(1000)
    # Updating screen on each iteration
    pygame.display.update()

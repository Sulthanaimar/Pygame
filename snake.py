import pygame
import sys
import time
import random
import os
import pathlib

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

pygame.init()

death_sound = pygame.mixer.Sound("Dark Souls ' You Died ' Sound Effect.wav")
eat_sound = pygame.mixer.Sound("Eat _ Munch 2 Sound Effect (download).wav")

easy = 15
medium = 25
hard = 40

white = (255, 255, 255)
yellow = (255, 255, 105)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

displaywidth = 800
displayheight = 600

display = pygame.display.set_mode((displaywidth, displayheight))
display.fill(black)
pygame.display.set_caption('Snake')
pygame.display.update()

fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (displaywidth//10)) * 10, random.randrange(1, (displayheight//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU SUCK', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (displaywidth/2, displayheight/4)
    pygame.mixer.Sound.play(death_sound)
    display.fill(black)
    display.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (displaywidth/10, 15)
    else:
        score_rect.midtop = (displaywidth/2, displayheight/1.25)
    display.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        pygame.mixer.Sound.play(eat_sound)
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (displaywidth//10)) * 10, random.randrange(1, (displayheight//10)) * 10]
    food_spawn = True

    # GFX
    display.fill(black)
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(display, red, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(display, green, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > displaywidth-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > displayheight-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    if score <= 10:
        fps_controller.tick(easy)
    elif score >= 10:
        fps_controller.tick(medium)
    elif score >= 20:
        fps_controller.tick(hard)







snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0




heart_image = pygame.image.load('heart.jpg')
snake_head = [250, 250]
snake_position = [[250, 250],[240, 250],[230,250]]
heart_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)

def display_snake(snake_position):
    for position in snake_position:
        pygame.draw.rect(display, red,pygame.Rect(position[0], position[1],10,10))

def display_heart(display, heart_position, heart):
    display.bilt(heart,(heart_position[0], heart_position[1]))



# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')
import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF
import time
import sys

pygame.init()

display_info = pygame.display.Info()
display_width = display_info.current_w//2
display_height = display_info.current_h//2
display_bgcolor = (180, 180, 200)
snake_color = (120, 0, 0)
screen = pygame.display.set_mode((display_width, display_height), HWSURFACE|DOUBLEBUF)
drawing_width, drawing_height = 500, 500
drawing = pygame.surface.Surface((drawing_width, drawing_height))
pygame.display.set_caption("Snakes!!!")
pygame.key.set_repeat(15)
snake_x = 100
snake_y = 100
snake_speed = 5

def draw_snake():
    snake_cell_size = 10
    pygame.draw.rect(drawing, snake_color, pygame.Rect(snake_x, snake_y, snake_cell_size, snake_cell_size))

def draw_food():
    pass

myfont = pygame.font.SysFont("monospace", 15)

def draw_text(drawing, text, x, y):
    # render text
    label = myfont.render(text, 1, (255,255,0))
    drawing.blit(label, (x, y))

def main():
    global snake_x, snake_y, snake_speed
    frame_count = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == "q":
                    return

                if event.unicode <= '9' and event.unicode > '0':
                    snake_speed = int(event.unicode)

        frame_count += 1

        pressed = pygame.key.get_pressed()

        #print(frame_count, len(events), pressed[pygame.K_LEFT])

        if pressed[pygame.K_LEFT]:
            snake_x -= snake_speed
        if pressed[pygame.K_RIGHT]:
            snake_x += snake_speed
        if pressed[pygame.K_DOWN]:
            snake_y += snake_speed
        if pressed[pygame.K_UP]:
            snake_y -= snake_speed

        if snake_x > drawing_width:
            snake_x = 0
        if snake_y > drawing_height:
            snake_y = 0
        if snake_x < 0:
            snake_x = drawing_width
        if snake_y < 0:
            snake_y = drawing_height

        # draw on the surface
        drawing.fill(display_bgcolor)

        draw_snake()
        draw_food()

        draw_text(drawing, "speed %s"%snake_speed, 10, 10)

        # paste our drawing on screen
        sd = pygame.transform.scale(drawing, (display_width-10, display_height-10))
        screen.blit(sd, (0, 0))

        # put whatever we draw on drawing
        pygame.display.flip()

        time.sleep(.05)

main()

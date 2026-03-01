import pygame
import sys


pygame.init()
pygame.font.init()


WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("黑板涂鸦）")


canvas = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
canvas.fill((0, 0, 0, 0)) 


BLACKBOARD = (0, 20, 0) 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)


pen_color = WHITE
pen_width = 5
min_width = 2
max_width = 15
drawing = False
last_x, last_y = 0, 0


font = pygame.font.SysFont(["SimHei", "Arial"], 28, bold=True)


min_btn = (WIDTH - 110, 25, 50, 50)  # x,y,w,h
close_btn = (WIDTH - 55, 25, 50, 50)

color_btns = {
    "red": (25, HEIGHT - 75, 60, 60),
    "white": (95, HEIGHT - 75, 60, 60),
    "yellow": (165, HEIGHT - 75, 60, 60),
    "blue": (235, HEIGHT - 75, 60, 60),
    "pink": (305, HEIGHT - 75, 60, 60),
    "plus": (375, HEIGHT - 75, 60, 60),
    "minus": (445, HEIGHT - 75, 60, 60),
    "tip": (515, HEIGHT - 75, 120, 60)
}

def draw_buttons():
   
    pygame.draw.rect(screen, (50,50,50), min_btn, border_radius=8)
    text = font.render("-", True, WHITE)
    text_rect = text.get_rect(center=(min_btn[0]+25, min_btn[1]+25))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, (180,0,0), close_btn, border_radius=8)
    text = font.render("×", True, WHITE)
    text_rect = text.get_rect(center=(close_btn[0]+25, close_btn[1]+25))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, RED, color_btns["red"], border_radius=8)
    pygame.draw.rect(screen, WHITE, color_btns["white"], border_radius=8)
    pygame.draw.rect(screen, YELLOW, color_btns["yellow"], border_radius=8)
    pygame.draw.rect(screen, BLUE, color_btns["blue"], border_radius=8)
    pygame.draw.rect(screen, PINK, color_btns["pink"], border_radius=8)

    pygame.draw.rect(screen, (30,30,30), color_btns["plus"], border_radius=8)
    text = font.render("＋", True, WHITE)
    text_rect = text.get_rect(center=(color_btns["plus"][0]+30, color_btns["plus"][1]+30))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, (30,30,30), color_btns["minus"], border_radius=8)
    text = font.render("－", True, WHITE)
    text_rect = text.get_rect(center=(color_btns["minus"][0]+30, color_btns["minus"][1]+30))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, (20,20,20), color_btns["tip"], border_radius=8)
    text = font.render(f"粗细：{pen_width}", True, WHITE)
    text_rect = text.get_rect(center=(color_btns["tip"][0]+60, color_btns["tip"][1]+30))
    screen.blit(text, text_rect)

def check_click(x, y):
    global pen_color, pen_width
    
    if min_btn[0] < x < min_btn[0]+min_btn[2] and min_btn[1] < y < min_btn[1]+min_btn[3]:
        pygame.display.iconify()
        return True
    if close_btn[0] < x < close_btn[0]+close_btn[2] and close_btn[1] < y < close_btn[1]+close_btn[3]:
        pygame.quit()
        sys.exit()
        return True

    
    if color_btns["red"][0] < x < color_btns["red"][0]+60 and color_btns["red"][1] < y < color_btns["red"][1]+60:
        pen_color = RED
        return True
    if color_btns["white"][0] < x < color_btns["white"][0]+60 and color_btns["white"][1] < y < color_btns["white"][1]+60:
        pen_color = WHITE
        return True
    if color_btns["yellow"][0] < x < color_btns["yellow"][0]+60 and color_btns["yellow"][1] < y < color_btns["yellow"][1]+60:
        pen_color = YELLOW
        return True
    if color_btns["blue"][0] < x < color_btns["blue"][0]+60 and color_btns["blue"][1] < y < color_btns["blue"][1]+60:
        pen_color = BLUE
        return True
    if color_btns["pink"][0] < x < color_btns["pink"][0]+60 and color_btns["pink"][1] < y < color_btns["pink"][1]+60:
        pen_color = PINK
        return True

    if color_btns["plus"][0] < x < color_btns["plus"][0]+60 and color_btns["plus"][1] < y < color_btns["plus"][1]+60:
        pen_width = min(pen_width + 1, max_width)
        return True
    if color_btns["minus"][0] < x < color_btns["minus"][0]+60 and color_btns["minus"][1] < y < color_btns["minus"][1]+60:
        pen_width = max(pen_width - 1, min_width)
        return True

    
    return False


running = True
while running:
  
    screen.fill(BLACKBOARD)

    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            if not check_click(mx, my):
                drawing = True
                last_x, last_y = mx, my

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            mx, my = event.pos
            # 线条画在canvas上，不是screen上！
            pygame.draw.line(canvas, pen_color, (last_x, last_y), (mx, my), pen_width)
            last_x, last_y = mx, my

    draw_buttons()

    pygame.display.update()

pygame.quit()
sys.exit()
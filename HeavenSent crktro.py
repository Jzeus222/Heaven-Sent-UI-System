import pygame
import math
import random
import sys
import os
import ctypes
from BlurWindow.blurWindow import blur

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heaven SENT")
clock = pygame.time.Clock()

hwnd = pygame.display.get_wm_info()["window"]
blur(hwnd, hexColor="#29252500", Acrylic=True, Dark=True)
user32 = ctypes.windll.user32

style = user32.GetWindowLongW(hwnd, -20)
user32.SetWindowLongW(hwnd, -20, style | 0x00080000 | 0x00000001)

user32.SetLayeredWindowAttributes(hwnd, 0xFF0000, 0, 0x00000001)

TRANSPARENT_COLOR = (1, 1, 1)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

NUM_STARS = 150
stars = []
for _ in range(NUM_STARS):
    
    stars.append([random.randint(-WIDTH, WIDTH), random.randint(-HEIGHT, HEIGHT), random.randint(1, WIDTH)])

script_dir = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(script_dir, "Razor1911 - GTA IV launcher [Keygen Music] [yjbe5wih_Fs].mp3")

pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

try:
    font = pygame.font.Font("PressStart2P-Regular", 18)
    logo_font = pygame.font.Font("PressStart2P-Regular", 48)
except IOError:
    font = pygame.font.SysFont("PressStart2P-Regular", 18, bold=True)
    logo_font = pygame.font.SysFont("PressStart2P-Regular", 48, bold=True)


SCROLL_TEXT = "          WELCOME TO HEAVEN SENT     GOD IS GREAT     IRON SHARPENS IRON     TO LIVE IS CHRIST,TO DIE IS GAIN!          "


char_surfaces = [font.render(char, True, WHITE) for char in SCROLL_TEXT]
char_widths = [surf.get_width() for surf in char_surfaces]

scroll_x = WIDTH
scroll_speed = 4
sine_amplitude = 40
sine_frequency = 0.03
wave_timer = 0


YOUR_LOGO_TEXT = "HEAVEN SENT"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    
    screen.fill((0, 0, 0))

    
    for star in stars:
        star[2] -= 4  
        if star[2] <= 0:  
            star[0] = random.randint(-WIDTH, WIDTH)
            star[1] = random.randint(-HEIGHT, HEIGHT)
            star[2] = WIDTH

        
        k = 400.0 / star[2]
        px = int(star[0] * k + WIDTH / 2)
        py = int(star[1] * k + HEIGHT / 2)

        
        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
            
            size = max(1, int((WIDTH - star[2]) / 100))
            brightness = min(255, int((WIDTH - star[2]) / WIDTH * 255))
            pygame.draw.circle(screen, (brightness, brightness, brightness), (px, py), size)

    
    glitch_offset = int(5 * math.sin(pygame.time.get_ticks() * 0.04))
    
    logo_cyan = logo_font.render("HEAVEN SENT", True, CYAN)
    logo_magenta = logo_font.render("HEAVEN SENT", True, MAGENTA)
    logo_white = logo_font.render("HEAVEN SENT", True, WHITE)
    
    logo_rect = logo_white.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    
    
    screen.blit(logo_cyan, (logo_rect.x - glitch_offset, logo_rect.y))
    screen.blit(logo_magenta, (logo_rect.x + glitch_offset, logo_rect.y))
    screen.blit(logo_white, logo_rect)


    current_x = scroll_x
    wave_timer += 0.05

    for i, char_surf in enumerate(char_surfaces):
        
        if current_x + char_widths[i] > 0 and current_x < WIDTH:
            
            y_offset = int(math.sin(wave_timer + current_x * sine_frequency) * sine_amplitude)
            char_y = int(HEIGHT * 0.75) + y_offset
            
            screen.blit(char_surf, (current_x, char_y))
        
        current_x += char_widths[i]

    
    scroll_x -= scroll_speed
    
    
    total_text_width = sum(char_widths)
    if scroll_x < -total_text_width:
        scroll_x = WIDTH

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
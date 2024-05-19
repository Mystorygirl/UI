import pygame
import sys


# Инициализируем pygame
pygame.init()


# Создаем основные объекты
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Menu")
font = pygame.font.Font(None, 36)


# Задаем опции меню
menu_options = ["Start", "FreePlay", "Settings", "Exit", ]
selected_option = 0


# Задаем основные параметры
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)




class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color


    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.x < mouse_pos[0] < self.x + self.width  \
            and self.y < mouse_pos[1] < self.y + self.height:
            pygame.draw.rect(screen, self.hover_color,
                             (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color,
                             (self.x, self.y, self.width, self.height))
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(
            center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text, text_rect)




buttons = []
for i, option in enumerate(menu_options):
    button = Button(option, 400 - 100, 200 + i * 50, 200, 50, BLACK, RED)
    buttons.append(button)




game_state = "menu"


# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and game_state == "menu":
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    # Start option selected
                    game_state = "game"
                elif selected_option == 1:
                    game_state = "settings"
                elif selected_option == 2:
                    game_state = "exit"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "menu"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, button in enumerate(buttons):
                if button.x < mouse_pos[0] < button.x + button.width \
                        and  button.y < mouse_pos[1] < button.y + button.height:
                    if i == 0:
                        game_state = "game"
                    elif i == 1:
                        game_state = "level select"
                    elif i == 2:
                        game_state = "settings"
                    elif i == 3:
                        game_state = "exit"
   
    screen.fill(BLACK)


    if game_state == "exit":
        pygame.quit()
        sys.exit()
    if game_state == "menu":
        for i, button in enumerate(buttons):
            if i == selected_option:
                button.color = GREEN
            else:
                button.color = BLACK
            button.draw(screen)
    elif game_state == "game":
        screen.fill(WHITE)
        text = font.render("Game", True, BLACK)
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
    elif game_state == "settings":
        screen.fill(WHITE)
        text = font.render("Settings", True, BLACK)
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
    elif game_state == "level select":
        screen.fill(WHITE)
        text = font.render("NEVER GONNA GIVE YOU UP", True, BLACK)
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)

   
    # Update the display
    pygame.display.update()
    clock.tick(FPS)

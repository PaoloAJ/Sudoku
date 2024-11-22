import pygame, sys
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = self.initialize_board()
        self.difficulty = difficulty
        self.cells = [
            [Cell(self.board[i][j], i , j, self.screen) for j in range(3)]
            for i in range(3)
        ]
    def initialize_board(self):
        return [["-" for i in range(3)]for j in range(3)]

    def reset_board(self):
        self.board = self.initialize_board()

    def draw(self):
        #horizontal lines
        for i in range(1, 4):
            pygame.draw.line(
                self.screen,
                "black",
                (0, i*210),
                (630, i*210),
                10
            )
        #vertical lines
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                "black",
                (i*210, 0),
                (i*210, 630),
                10
            )
        for row in self.cells:
            for cell in row:
                cell.draw()

class Display:
    def __init__(self, image_path, width, height):
        self.image_path = image_path
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.resized_image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.resized_image.get_rect(center=(width // 2, height // 2))

    def save_resized_image(self, save_path):
        pygame.image.save(self.resized_image, save_path)

    def bg_render(self, screen):
        screen.blit(self.resized_image, self.rect)
        pygame.display.flip()

    def button_render(self, screen, pos):
        self.rect = self.resized_image.get_rect(center=pos)
        screen.blit(self.resized_image, self.rect)
        pygame.display.flip()

    def text_render(self, text, color, size, pos):
        font = pygame.font.Font(None, size)

        surf = font.render(text, 0, color)
        rect = surf.get_rect(center=pos)
        screen.blit(surf, rect)

def draw_welcome():
    welcome_bg = Display("pink_wall.png", 630, 700)

    welcome_bg.bg_render(screen)
    welcome_bg.text_render("Welcome to Sudoku", 30, 60, (630 // 2, 700 // 2 - 50))
    welcome_bg.text_render("Select Game Mode", 30, 45, (630 // 2, 700 // 2 + 100))

def game_buttons():
    reset_but.button_render(screen, (170, 665))
    restart_but.button_render(screen, (315, 665))
    exit_but.button_render(screen, (460, 665))

def difficulty_buttons():
    easy_but.button_render(screen, (170, 500))
    med_but.button_render(screen, (315, 500))
    hard_but.button_render(screen, (460, 500))

def draw_easy_board():
    board3 = pygame.image.load("wildcatjan17p.gif")
    width2= 630
    height2 = 630
    resizeimage10 = pygame.transform.scale(board3, (width2, height2))
    pygame.image.save(resizeimage10, "wildcatjan17p.resized.gif")
    board3_rect = resizeimage10.get_rect(topleft=(0, 0))
    screen.blit(resizeimage10, board3_rect)
    pygame.display.flip()

'''
    def select(self, row, col):

    def click(self, row, col):

    def clear(self):

    def sketch(self, value):

    def place_number(self, value):

    def reset_to_original(self):

    def is_full(self):

    def update_board(self):
    def find_empty(self):
    def check_board(self):
'''


#put main in sudoku.py file
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((630, 700))
    pygame.display.set_caption('Sudoku')
    screen.fill("white")

    board = Board(3, 3, screen, 0)

    easy_but = Display("easy_button.png", 200, 150)
    med_but = Display("medium_button.png", 200, 150)
    hard_but = Display("hard_button.png", 200, 150)

    reset_but = Display("reset_button.png", 200, 150)
    restart_but = Display("restart_button.png", 200, 150)
    exit_but = Display("exit_button.png", 200, 150)

    draw_welcome()
    difficulty_buttons()
    pygame.display.update()

game_in_progress = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_in_progress:
            x,y = event.pos
            mouse_pos = x,y
            print(x, y)
            if (easy_but.rect.left <= mouse_pos[0] <= easy_but.rect.right
                    and easy_but.rect.top <= mouse_pos[1] <= easy_but.rect.bottom):
                empty_cells = 30
                game_in_progress = True

            elif(med_but.rect.left <= mouse_pos[0] <= med_but.rect.right
                    and med_but.rect.top <= mouse_pos[1] <= med_but.rect.bottom):
                empty_cells = 40
                game_in_progress = True

            elif(hard_but.rect.left <= mouse_pos[0] <= hard_but.rect.right
                    and hard_but.rect.top <= mouse_pos[1] <= hard_but.rect.bottom):
                empty_cells = 30
                game_in_progress = True

        if game_in_progress:
            screen.fill("light pink")
            #draw_easy_board()
            board.draw()
            game_buttons()
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass










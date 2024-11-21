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



def draw_welcome():
    screen.fill("white")
    welcome_font = pygame.font.Font(None, 60)
    welcome_text = "Welcome to Sudoku"

    welc_surf = welcome_font.render(welcome_text, 0, "black")
    welc_rect = welc_surf.get_rect(center=(630//2, 700//2 - 50))
    screen.blit(welc_surf, welc_rect)

    select_font = pygame.font.Font(None, 45)
    select_text = "Select Game Mode:"

    select_surf = select_font.render(select_text, 0, "black")
    select_rect = select_surf.get_rect(center=(630//2, 700//2 + 100))
    board.screen.blit(select_surf, select_rect)

    easy_image = pygame.image.load("easy_button.png")
    easy_width, easy_height = easy_image.get_size()
    easy_rect = easy_image.get_rect(center=(630 // 2, 700 // 2 + 100))
    screen.blit(easy_image, easy_rect)
    pygame.display.flip()


    #add buttons
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

# cat_image = pygame.image.load("olli-the-polite-cat.jpg")
# cat_width, cat_height = cat_image.get_size()
# cat_rect = cat_image.get_rect(center=(630//2, 700//2 + 100))
# screen.blit(cat_image, cat_rect)
# pygame.display.flip()




#put main in sudoku.py file
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((630, 700))
    pygame.display.set_caption('Sudoku')
    screen.fill("white")
    board = Board(3, 3, screen, 0)
    draw_welcome()
    pygame.display.update()

# cat_rect = cat_image.get_rect(center=(630//2, 700//2 + 100))
# screen.blit(cat_image, cat_rect)
# pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("light pink")
            board.draw()
            pygame.display.update()
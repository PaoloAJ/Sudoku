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
    pink_wall = pygame.image.load("pink_wall.png")
    width = 630
    height = 700
    resizeimage5 = pygame.transform.scale(pink_wall, (width, height))
    pygame.image.save(resizeimage5, "pink_wall_resized.png")
    pink_rect = resizeimage5.get_rect(center=(630 // 2, 700 // 2))
    screen.blit(resizeimage5, pink_rect)
    pygame.display.flip()

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

def draw_buttons():
    #easy Button + placement below
    easy_image = pygame.image.load("easy_button.png")
    width = 200
    height = 150
    resizeimage = pygame.transform.scale(easy_image, (width, height))
    pygame.image.save(resizeimage, "easy_button_resized.png")
    resized_width, resized_height = resizeimage.get_size()
    easy_rect = resizeimage.get_rect(center=(170,500))
    screen.blit(resizeimage, easy_rect)
    pygame.display.flip()

    #medium button + placement below
    medium_image = pygame.image.load("medium_button.png")
    width = 200
    height = 150
    resizeimage1 = pygame.transform.scale(medium_image, (width, height))
    pygame.image.save(resizeimage1, "medium_button_resized.png")
    resized_width1, resized_height1 = resizeimage1.get_size()
    medium_rect = resizeimage1.get_rect(center=(315,500))
    screen.blit(resizeimage1, medium_rect)
    pygame.display.flip()

    #hard button +placement below
    hard_image = pygame.image.load("hard_button.png")
    width = 200
    height = 150
    resizeimage2 = pygame.transform.scale(hard_image, (width, height))
    pygame.image.save(resizeimage2, "hard_button_resized.png")
    resized_width2, resized_height2 = resizeimage2.get_size()
    hard_rect = resizeimage2.get_rect(center=(460,500))
    screen.blit(resizeimage2, hard_rect)
    pygame.display.flip()
def game_buttons():
    #reset button
    reset_image = pygame.image.load("reset_button.png")
    width = 200
    height = 150
    resizeimage1 = pygame.transform.scale(reset_image, (width, height))
    pygame.image.save(resizeimage1, "reset_button_resized.png")
    reset_rect = resizeimage1.get_rect(center=(170,665))
    screen.blit(resizeimage1, reset_rect)
    pygame.display.flip()

    #restart button
    restart_image = pygame.image.load("restart_button.png")
    width = 200
    height = 150
    resizeimage2 = pygame.transform.scale(restart_image, (width, height))
    pygame.image.save(resizeimage2, "restart_button_resized.png")
    restart_rect = resizeimage2.get_rect(center=(315,665))
    screen.blit(resizeimage2, restart_rect)
    pygame.display.flip()

    #exit button
    exit_image = pygame.image.load("exit_button.png")
    width = 200
    height = 150
    resizeimage3 = pygame.transform.scale(exit_image, (width, height))
    pygame.image.save(resizeimage3, "exit_button_resized.png")
    exit_rect = resizeimage3.get_rect(center=(460,665))
    screen.blit(resizeimage3, exit_rect)
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
    draw_welcome()
    draw_buttons()
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("light pink")
            board.draw()
            game_buttons()
            pygame.display.update()
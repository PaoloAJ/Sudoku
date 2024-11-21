
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
    board = Board(3,3, screen,0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        board.draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
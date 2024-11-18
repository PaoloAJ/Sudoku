import pygame, sys
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

    def set_cell_value(self,value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        pass
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = self.initialize_board()
        self.difficulty = difficulty
        self.cells = [
            [Cell(self.board[i][j], i , j) for j in range(3)]
            for i in range(3)
        ]
    def initialize_board(self):
        return [["-" for i in range(3)]for j in range(3)]

    def draw(self):
        #horizontal lines
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                "black",
                (0, i*200),
                (600, i*200),
                15
            )
        #vertical lines
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                "black",
                (i*200, 0),
                (i*200, 600),
                15
            )
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)
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
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Sudoku')
    screen.fill("white")
    board = Board(3,3, screen,0)
    board.draw()

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
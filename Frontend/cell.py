
'''class Cell:
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
    '''
#chat
import pygame
import sys

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        # Draw the cell border
        rect = pygame.Rect(self.col * 200, self.row * 200, 200, 200)
        pygame.draw.rect(self.screen, "black", rect, 2)

        # Draw the value if it exists
        if self.value != "-":
            font = pygame.font.Font(None, 100)
            text = font.render(str(self.value), True, "black")
            self.screen.blit(text, (self.col * 200 + 50, self.row * 200 + 50))

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = self.initialize_board()
        self.difficulty = difficulty
        self.cells = [
            [Cell(self.board[i][j], i, j, self.screen) for j in range(3)]
            for i in range(3)
        ]

    def initialize_board(self):
        return [["-" for _ in range(3)] for _ in range(3)]

    def draw(self):
        # Horizontal lines
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                "black",
                (0, i * 200),
                (600, i * 200),
                15
            )
        # Vertical lines
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                "black",
                (i * 200, 0),
                (i * 200, 600),
                15
            )
        # Draw cells
        for row in self.cells:
            for cell in row:
                cell.draw()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Sudoku')
    screen.fill("white")
    board = Board(3, 3, screen, 0)

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

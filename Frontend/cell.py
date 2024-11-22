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
        rect = pygame.Rect(self.col * 210, self.row * 210, 210, 210)
        pygame.draw.rect(self.screen, "black", rect, 2)

        small_cell_size = 70
        #horizontal lines for smaller grid
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                "black",
                (self.col * 210, self.row * 210 + i * small_cell_size),
                (self.col * 210 + 210, self.row * 210 + i * small_cell_size),
                3
            )
        # vertical lines for smaller grid
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                "black",
                (self.col * 210 + i * small_cell_size, self.row * 210),
                (self.col * 210 + i * small_cell_size, self.row * 210 + 210),
                3
            )

        #draw value in cell
        if self.value != '-':
            font = pygame.font.Font(None, 100)
            text = font.render(str(self.value), True, "black")
            self.screen.blit(text, (self.col * 210 + 50, self.row * 210 + 50))







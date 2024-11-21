import pygame, sys
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
        #creates the cell border walls
        rect = pygame.Rect(self.col *200, self.row *200, 200, 200)
        pygame.draw.rect(self.screen, "black", rect, 2)
        if self.value != '-':
            font = pygame.font.Font(None, 100)
            text = font.render(str(self.value), True, "black")
            self.screen.blit(text, (self.col * 200 + 50, self.row * 200 + 50))
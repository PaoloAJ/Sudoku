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

    def text_render(self, text, color, size, pos, screen):
        font = pygame.font.Font(None, size)

        surf = font.render(text, 0, color)
        rect = surf.get_rect(center=pos)
        screen.blit(surf, rect)

def draw_welcome(screen):
    welcome_bg = Display("./Frontend/pink_wall.png", 630, 700)

    welcome_bg.bg_render(screen)
    welcome_bg.text_render("Welcome to Sudoku", 30, 60, (630 // 2, 700 // 2 - 50), screen)
    welcome_bg.text_render("Select Game Mode", 30, 45, (630 // 2, 700 // 2 + 100), screen)

def text_render( text, color, size, pos, screen):
    text = str(text)
    font = pygame.font.Font(None, size)

    surf = font.render(text, 0, color)
    rect = surf.get_rect(center=pos)
    screen.blit(surf, rect)




# def draw_easy_board(screen):
#     board3 = pygame.image.load("wildcatjan17p.gif")
#     width2= 630
#     height2 = 630
#     resizeimage10 = pygame.transform.scale(board3, (width2, height2))
#     pygame.image.save(resizeimage10, "wildcatjan17p.resized.gif")
#     board3_rect = resizeimage10.get_rect(topleft=(0, 0))
#     screen.blit(resizeimage10, board3_rect)
#     pygame.display.flip()


#put main in sudoku.py file

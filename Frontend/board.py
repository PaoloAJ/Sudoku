import pygame
from Backend.sudoku_generator import *
from Frontend.cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board, self.solution_board = generate_sudoku(9, difficulty)
        self.original_board = [row[:] for row in self.board]
        self.cells = []
        self.selected_cell = None
        for row in range(len(self.board)):
            cells_in_row = []
            for col in range(len(self.board[row])):
                cell = Cell(self.board[row][col], row, col, self.screen)
                cells_in_row.append(cell)
            self.cells.append(cells_in_row)

    def draw(self):
        # Delineate lines
        for i in range(2):
            # Horizontal Lines
            pygame.draw.line(
                self.screen,
                "black",
                (0, (i * 210) + 210),
                (self.width, (i * 210) + 210),
                5,
            )

            # Vertical Lines
            pygame.draw.line(
                self.screen,
                "black",
                ((i * 210) + 210, 0),
                ((i * 210) + 210, self.height),
                5,
            )

        # # Draws board
        for row in range(len(self.cells)):
            for col in range(len(self.cells)):
                self.cells[row][col].draw()

    def click(self, x, y):
        if (0 <= x <= self.width) and (0 <= y <= self.height):
            row = y // 70
            col = x // 70
            return row, col
        else:
            return None, None

    def select(self, row, col):
        # Deselect previously selected cell
        if self.selected_cell:
            prev_row, prev_col = self.selected_cell
            self.cells[prev_row][prev_col].selected = False

        # Select the new cell
        if (row != None) and (col != None):
            self.selected_cell = (row, col)
            self.cells[row][col].selected = True

    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.cells[row][col].value == 0:
                self.cells[row][col].set_sketched_value(value)
                return True
            else:
                return False

        return False

    def place_number(self, value):
        row, col = self.selected_cell
        self.board[row][col] = value
        self.cells[row][col].set_cell_value(value)

    def clear(self):
        for cell_objects in self.cells:
            for cell in cell_objects:
                if cell.sketched != 0:
                    cell.set_sketched_value(0)
                else:
                    continue

    def reset_to_original(self):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if (
                    self.cells[row][col].value != self.original_board[row][col]
                    or self.cells[row][col].sketched != 0
                ):
                    self.board[row][col] = self.original_board[row][col]
                    self.cells[row][col].set_cell_value(self.original_board[row][col])
                    self.cells[row][col].set_sketched_value(0)
                else:
                    continue

    def is_full(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return False

        return True

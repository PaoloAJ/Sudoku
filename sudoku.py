import pygame
from pygame import mixer
import sys
from Frontend.board import Board
from Frontend.buttons import Button

pygame.init()

bg_music = mixer.Sound("barbie.mp3")
sparkle = mixer.Sound("sparkle.mp3")
bg_music.play(-1)


def draw_welcome(screen):

    text_render("Welcome to Sudoku", 30, 60, (630 // 2, 700 // 2 - 50), screen)
    text_render("Select Game Mode", 30, 45, (630 // 2, 700 // 2 + 100), screen)


def text_render(text, color, size, pos, screen):
    text = str(text)
    font = pygame.font.Font(None, size)

    surf = font.render(text, 0, color)
    rect = surf.get_rect(center=pos)
    screen.blit(surf, rect)


def main():
    # Constants
    SCREEN_WIDTH, BOARD_WIDTH = 630, 630
    SCREEN_HEIGHT = 700
    BOARD_HEIGHT = 630
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 150
    board = []

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Loading images
    bg_image = pygame.image.load("./Images/pink_wall.png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    easy_button_image = pygame.image.load("./Images/easy_button.png").convert_alpha()
    medium_button_image = pygame.image.load("./Images/medium_button.png").convert_alpha()
    hard_button_image = pygame.image.load("./Images/hard_button.png").convert_alpha()

    easy_button = Button(40, 500, easy_button_image, screen)
    medium_button = Button(240, 500, medium_button_image, screen)
    hard_button = Button(430, 500, hard_button_image, screen)

    reset_button_image = pygame.image.load("./Images/reset_button.png").convert_alpha()
    restart_button_image = pygame.image.load("./Images/restart_button.png").convert_alpha()
    exit_button_image = pygame.image.load("./Images/exit_button.png").convert_alpha()

    reset_button = Button(40, 640, reset_button_image, screen)
    restart_button = Button(240, 640, restart_button_image, screen)
    exit_button = Button(430, 640, exit_button_image, screen)

    # States
    game_menu = True
    game_running = False
    cell_selected = False
    entered = False
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if easy_button.rect.collidepoint(mouse_pos):
                        sparkle.play()
                        board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, 30)
                        game_menu = False
                        game_running = True
                    elif medium_button.rect.collidepoint(mouse_pos):
                        sparkle.play()
                        board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, 40)
                        game_menu = False
                        game_running = True
                    elif hard_button.rect.collidepoint(mouse_pos):
                        sparkle.play()
                        board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, 50)
                        game_menu = False
                        game_running = True

            if game_running:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = board.click(x, y)
                    if (row != None) or (col != None):
                        cell_selected = True
                    else:
                        if exit_button.rect.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                        elif reset_button.rect.collidepoint(event.pos):
                            board.reset_to_original()
                        elif restart_button.rect.collidepoint(event.pos):
                            game_running = False
                            game_menu = True


                # Handles key press
                if event.type == pygame.KEYDOWN and cell_selected:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        number = event.key - pygame.K_0
                        if board.sketch(number):
                            entered = True
                        else:
                            print("Can't change the cell's value")
                            entered = False
                    elif event.key == pygame.K_UP and 0 <= row - 1 <= 8:
                        row -= 1
                    elif event.key == pygame.K_DOWN and 0 <= row + 1 <= 8:
                        row += 1
                    elif event.key == pygame.K_LEFT and 0 <= col - 1 <= 8:
                        col -= 1
                    elif event.key == pygame.K_RIGHT and 0 <= col + 1 <= 8:
                        col += 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and entered:
                        board.place_number(number)
                        entered = False
                    elif (
                        event.key == pygame.K_RETURN
                        and board.cells[row][col].sketched != 0
                    ):
                        board.place_number(board.cells[row][col].sketched)
                    elif event.key == pygame.K_ESCAPE:
                        cell_selected = False

        # Display update (Out of event listening loop)
        if game_menu:
            screen.blit(bg_image, (0, 0))
            draw_welcome(screen)
            easy_button.draw()
            medium_button.draw()
            hard_button.draw()

        if game_running:
            if board.is_full():
                if board.board == board.solution_board:
                    game_over = True
                    winner1 = 1
                    break
                else:
                    game_over = True
                    winner1 = 2
                    break
            screen.fill("pink")
            board.draw()
            reset_button.draw()
            restart_button.draw()
            exit_button.draw()
            if cell_selected:
                board.select(row, col)
            else:
                prev_row, prev_col = board.selected_cell
                board.cells[prev_row][prev_col].selected = False

        pygame.display.update()
        clock.tick(60)

    # Game over check
    if game_over:
        SCREEN_WIDTH, SCREEN_HEIGHT = 630, 700

        if winner1 == 1:
            game_over_bg = pygame.image.load("./Images/smiling_cat.jpg").convert_alpha()
            game_over_bg = pygame.transform.scale(game_over_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            end_text = "Game Won!"
            exit_button_image = pygame.image.load("./Images/exit_button.png").convert_alpha()
            exit_button = Button(240, 500, exit_button_image, screen)
            button = exit_button
        else:
            game_over_bg = pygame.image.load("./Images/sad_mj.jpg").convert_alpha()
            game_over_bg = pygame.transform.scale(game_over_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            end_text = "YOU LOSE"
            restart_button_image = pygame.image.load("./Images/restart_button.png").convert_alpha()
            restart_button = Button(240, 500, restart_button_image, screen)
            button = restart_button

        while True:
            screen.blit(game_over_bg, (0, 0))
            text_render(end_text, "white", 60, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50), screen)
            button.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.rect.collidepoint(event.pos):
                        if button == exit_button:
                            pygame.quit()
                            sys.exit()
                        elif button == restart_button:
                            main()





if __name__ == "__main__":
    main()
